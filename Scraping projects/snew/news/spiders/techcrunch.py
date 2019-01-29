# -*- coding: utf-8 -*-
############################
from scrapy.utils.response import open_in_browser
############################
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from news.items import ArticleItem
from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose, Join
from news.models import *

# from scrapy.extensions.closespider import CloseSpider
class TechcrunchSpider(scrapy.Spider):
    name = 'techcrunch'
    custom_settings = {
        "HTTP_PROXY":'127.0.0.1:8118',
        "DOWNLOAD_DELAY": 0,
        "ITEM_PIPELINES": {
            'news.pipelines.ProcessArticleGeneric': 300,
            'news.pipelines.RecordAlt': 305,
        }
        # "DOWNLOADER_MIDDLEWARES": {
        #     'myproject.middlewares.RandomUserAgentMiddleware': 400,
        #     'myproject.middlewares.ProxyMiddleware': 410,
        #     'scrapy.contrib.downloadermiddleware.useragent.UserAgentMiddleware': None}
        }

    allowed_domains = ['techcrunch.com']
    start_urls = ['https://techcrunch.com']

    article_count = 0
    article_count_limit = 100
    follow_pagination = True

    def parse(self, response):

        find_articles = LinkExtractor(allow=(),
                        restrict_xpaths = "//div[@class='block-content']//h2[@class='post-title']",
                        unique = True).extract_links(response)

        found_links = [found_link.url for found_link in find_articles]
        # yield {"===========" : found_links}
        for link in found_links:
            url_exists = session_test.query(exists().where(Url_entry.url==link)).scalar()
            if not url_exists :
                if self.article_count < self.article_count_limit:
                    article_request = scrapy.Request(link, callback = self.parse_item)
                    yield article_request
                else:
                    self.follow_pagination = False

            else:
                self.article_count += 1

        found_paginations = LinkExtractor(allow=(),
                        restrict_xpaths = "//*[@class='pagination']//li[@class='next']",
                        unique = True).extract_links(response)

        found_paginations = [found_pagination.url for found_pagination in found_paginations]
        for pagination in found_paginations:
            if self.follow_pagination:
                parse_pagination_request = scrapy.Request(pagination, callback = self.parse)
                yield parse_pagination_request
            else:
                pass



    # def parse_pagination(self, response):



    def parse_item(self, response):
        # return {"====================pew" : response.url}
        # open_in_browser(response)
        article = ItemLoader(item = ArticleItem(), response = response)
        article.add_value('url', response.url)
        article.add_xpath("article_text", '//div[contains(@class, "article-entry text")]// \
                            *[self::p or self::li or self::h1 or self::h2 or \
                                self::h3 or self::h4 or self::h5]//text()', Join())
        article.add_xpath("article_title", '//h1/text()', Join())
        article.add_xpath("author_name", '//div[@class = "byline"]/a[@rel="author"]/text()')
        article.add_xpath("author_name_alt", '//div[@class = "byline"]/text()')

        article.add_xpath("date_published", '//meta[@name = "sailthru.date"]/@content', Join())

        item = article.load_item()
        # i = {}
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        return item

# <meta name="sailthru.title" content="Ripcord CEO faces allegations of improper&nbsp;behavior">
