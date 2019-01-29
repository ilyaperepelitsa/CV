# -*- coding: utf-8 -*-
import scrapy


class MydomainSpider(scrapy.Spider):
    name = "mydomain"
    allowed_domains = ["whatsmyip.org"]
    start_urls = ['http://www.whatsmyip.org']

    def parse(self, response):
        i = {}
        i['domain_id'] = response.xpath('//*[@id="ip"]').extract()
        return i
        # pass
