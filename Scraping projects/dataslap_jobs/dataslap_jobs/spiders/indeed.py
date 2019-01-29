# -*- coding: utf-8 -*-
import scrapy
from scrapy.utils.response import open_in_browser

from scrapy.linkextractors import LinkExtractor

from dataslap_jobs.items import JobItem
from dataslap_jobs.pipelines import ProcessIndeed
from scrapy.loader import ItemLoader

import re
from datetime import datetime,tzinfo,timedelta

from pytz import timezone
import pytz

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Enum
from sqlalchemy.sql import select
import itertools


from dataslap_jobs.models import *


class IndeedSpider(scrapy.Spider):
    name = "indeed"
    allowed_domains = ["indeed.com"]
    start_urls = ["https://www.indeed.com"]
    search_terms = ["data scientist", "web scraping", "data aggregation"]
    locations = ["New York, NY", "Boston, MA"]
    full_search = list(itertools.product(search_terms, locations))


    avoid_page = []
    avoid_job = []
    duplicate_counter = 0
    duplicate_count_limit = 300
    follow_pagination = True

    custom_settings = {
        'ITEM_PIPELINES': {
            'dataslap_jobs.pipelines.ProcessIndeed': 300,
            'dataslap_jobs.pipelines.RecordJob': 400
        }
    }

    script = """
    function main(splash, args)

        function focus(sel)
            splash:select(sel):focus()
        end

        function wait_to_load(time)
            local initial_check = true
            local initial_html = splash:html()

            while initial_check do
                assert(splash:wait(time))
                local new_html = splash:html()
                if (initial_html == new_html) then
                    initial_check = false
                else
                    initial_html = new_html
                end
            end
        end

				wait_to_load(2)
				assert(splash:go(args.url))
        wait_to_load(2)

        return {
        html = splash:html()
        }
    end
    """


    def parse(self, response):
        for search_term in self.full_search:
            yield scrapy.FormRequest.from_response(
                response,
                formdata={"q" : search_term[0],
                            "l" : search_term[1]},
                callback = self.after_search,
                dont_filter = True
            )


    def after_search(self, response):

        next_page = LinkExtractor(allow=(),
                                  restrict_xpaths='//div[@class="pagination"]',
                                  unique=True).extract_links(response)

        job_links = LinkExtractor(allow=(),
                                  restrict_xpaths='//div[@data-jk]//a[@data-tn-element="jobTitle"]',
                                  unique=True).extract_links(response)

        job_links = [
            job_link.url for job_link in job_links if job_link.url not in self.avoid_job]
        next_page = [
            next_link.url for next_link in next_page if next_link.url not in self.avoid_page]


        for next_link in next_page:
            if self.follow_pagination:
                if next_link not in self.avoid_page:
                    self.avoid_page.append(next_link)
                    next_page_request = scrapy.Request(
                        next_link, callback=self.after_search)
                yield next_page_request

        for job_link in job_links:
            if self.duplicate_counter < self.duplicate_count_limit:
                job_link_request = scrapy.Request(
                    job_link, callback=self.parse_job)
                yield job_link_request
            else:
                self.follow_pagination = False



    def parse_job(self, response):
        url_exists = session_test.query(exists().where(Url_entry.url==response.url)).scalar()
        if not url_exists:
            self.duplicate_counter = 0
            job = ItemLoader(item = JobItem(), response = response)
            job.add_value("url", response.url)

            job.add_xpath(
                "job_company", '//*[@class="company" and preceding-sibling::*[@class="jobtitle"]]//text()')

            job.add_xpath("job_position", '//*[@class="jobtitle"]//text()')
            job.add_xpath("job_text", '//*[@id="job_summary"]//text()')

            job.add_xpath("location", '//div[@data-tn-component]//*[@class="location"]//text()')
            job.add_value('country', "United States")


            extracted = response.xpath('//*[@class = "result-link-bar"]//*[@class = "date"]//text()').extract()
            extracted = "".join(extracted)

            if re.findall("hour", extracted) or re.findall("day", extracted):
                if re.findall("hour", extracted):
                    hours_num = re.findall("\d+", extracted)
                    hours_num = "".join(hours_num)
                    date_output = datetime.now(timezone('US/Eastern')) - timedelta(hours=int(hours_num))
                    job.add_value('date_added', date_output)
                elif re.findall("day", extracted):
                    days_num = re.findall("\d+", extracted)
                    days_num = "".join(days_num)
                    date_output = datetime.now(timezone('US/Eastern')) - timedelta(days=int(days_num))
                    job.add_value('date_added', date_output)

                days_since_posted = (datetime.now(timezone('US/Eastern')) - date_output).days


                job.add_value('date_scraped', datetime.now(timezone('US/Eastern')))

                job.add_value('source', "indeed")

                # job.add_value('page_source_html', response.body)
                job.add_xpath("page_source_text", '//text()')

                if days_since_posted < 28:

                    external_check = response.xpath('//div[@id = "apply-button-container"]//a//@href').extract()
                    if external_check:
                        external_url = "https://www.indeed.com" + "".join(external_check)
                        job.add_value('external_url', external_url)


                        yield scrapy.Request(external_url, self.check_external, meta={
                            'job': job,
                            'splash': {
                                'args': {
                                    'lua_source': self.script,
                                    'html': 1,
                                    },
                                'endpoint': 'execute'}}, dont_filter=True)
                    else:
                        item = job.load_item()
                        yield(item)
        else:
            self.duplicate_counter += 1

    def check_external(self, response):
        job = response.meta['job']
        # job.add_value('page_external_source_html', str(response.body))
        job.add_xpath("page_external_source_text", '//text()')
        item = job.load_item()
        # yield({"pew================": response.body.encode('UTF-8')})

        yield(item)
