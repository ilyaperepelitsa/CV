# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.utils.response import open_in_browser

class CheckipSpider(CrawlSpider):
    name = 'checkip'
    custom_settings = {
        "HTTP_PROXY":'127.0.0.1:8118',
        "DOWNLOAD_DELAY" : 0,
        "ITEM_PIPELINES" : {
               # 'news.pipelines.ProcessArticle': 300,
               # 'news.pipelines.RecordArticle': 400,
            }
        # "DOWNLOADER_MIDDLEWARES": {
        #     'myproject.middlewares.RandomUserAgentMiddleware': 400,
        #     'myproject.middlewares.ProxyMiddleware': 410,
        #     'scrapy.contrib.downloadermiddleware.useragent.UserAgentMiddleware': None}
    }

    allowed_domains = ['whatsmyip.org']
    start_urls = ['http://www.whatsmyip.org']

    # rules = (
    #     Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=False),
    # )

    def parse(self, response):
        i = {}
        # i['domain_id'] = response.xpath('//*[@id="hostname"]').extract()
        i['domain_id'] = response.xpath('//h1/span/text()').extract()

        # open_in_browser(response)
        # i["++++++++++"] = '____________________________________________'
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        return i
        # return {"pew___________________________" : "tratatatat"}
