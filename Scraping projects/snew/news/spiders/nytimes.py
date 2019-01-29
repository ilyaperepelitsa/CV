# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from news.items import ArticleItem
from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose, Join

import json

json_thingy = {}
ignore_sections = set()

class NytttSpider(CrawlSpider):
    name = 'nytimes'
    allowed_domains = ['nytimes.com']
    start_urls = ['http://nytimes.com/']

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




    rules = (
        Rule(LinkExtractor(allow=('section'),
                            restrict_xpaths = '//ul[@class="mini-navigation-menu"]/li',
                            unique = True),
                callback='parse_section', follow=True),
    )



    def parse_section(self, response):

        ignore_sections.add(response.url)
        pewdict = {}


        # json_thingy = set()
        # json_thingy[response.url] = response.url.split("/section/")[1]
        # json_thingy.add(response.url)
        # print(len(json_thingy))
        # pewdict["pew"] = len(json_thingy)


        find_section_headers = LinkExtractor(allow=(),
                        restrict_xpaths = '//main//header[contains(@class, "section-header")]',
                        unique = True).extract_links(response)

        section_links = [link.url for link in find_section_headers]
        for section_link in section_links:
            if section_link not in ignore_sections:
                ignore_sections.add(section_link)
                section_request = scrapy.Request(section_link, callback = self.parse_section)
                yield section_request





        find_headlines = LinkExtractor(allow=(),
                        restrict_xpaths = '//div[contains(@class, "featured")]',
                        unique = True).extract_links(response)

        headline_links = [headline_link.url for headline_link in find_headlines]
        for headline in headline_links:
            headline_request = scrapy.Request(headline, callback = self.parse_article)
        # pewdict[response.url] = len(headline_links)



        json_init_url = "https://www.nytimes.com/svc/collections/v1/publish/" + response.url.split("https://")[1] + "?q=&sort=newest&page=0&dom=www.nytimes.com&dedupe_hl=y"
        init_json_request = scrapy.Request(json_init_url, callback = self.get_json)
        yield init_json_request


    def get_json(self, response):
        # init_json = response.xpath("//pre/text()").extract()
        # init_json = init_json[1:-1]
        init_json = json.loads(response.text)

        # init_json = json.load(response.body_as_unicode().replace("'", '"'))
        meta_container = init_json["members"]
        for page_num in range(0, int(meta_container["total_pages"])):
            json_to_parse = str(response.url.split("0")[0] + str(page_num) + response.url.split("0")[1])
            final_json_request = scrapy.Request(json_to_parse, callback = self.parse_json)
            yield final_json_request


    def parse_json(self, response):
        # final_json = response.xpath("//pre/text()").extract()
        # final_json = final_json[1:-1]
        final_json = json.loads(response.text)
        try:
            first_container = final_json[[i for i in list(final_json.keys()) if i.startswith("container")][0]]
            first_final_label = list(final_json[[i for i in list(final_json.keys()) if i.startswith("container")][0]].keys())[0]
            for featured_article in first_container[first_final_label]["items"]:
                first_url_to_parse = str(featured_article["url"])
                first_article_request = scrapy.Request(first_url_to_parse, callback = self.parse_article)
                yield first_article_request

        except IndexError:
            pass


        try:
            second_container = final_json["members"]
            for regular_article in second_container["items"]:
                second_url_to_parse = str(regular_article["url"])
                second_article_request = scrapy.Request(second_url_to_parse, callback = self.parse_article)
                yield second_article_request

        except IndexError:
            pass


    def parse_article(self, response):
        article = ItemLoader(item = ArticleItem(), response = response)

        # article.add_xpath("url", '//meta[@property = "og:url"]/@content')
        article.add_value('url', response.url)
        article.add_xpath("data_type", '//meta[@property = "og:type"]/@content')
        article.add_xpath("section", '//meta[@property = "article:section"]/@content')
        # article.add_xpath("sections", '//script[(@id = "page-config-data") and (@type = "text/json")]/text()',
        #                     MapCompose(lambda extracted_json: json.loads(extracted_json),
        #                                lambda loaded_json: loaded_json[0]["pageconfig"]["collections"]["sections"]),
        #                     Join(", "))
        #
        article.add_xpath("sections", '//script[(@id = "page-config-data") and (@type = "text/json")]/text()')

        article.add_xpath("top_level_section", '//meta[@property = "article:top-level-section"]/@content')
        article.add_xpath("section_url", '//meta[@property = "article:section_url"]/@content')
        article.add_xpath("tone", '//meta[@name = "tone"]/@content')
        article.add_xpath("headline", '//meta[@name = "hdl"]/@content')
        article.add_xpath("kicker", '//meta[@name = "col"]/@content')

        article.add_xpath("author", '//meta[@name = "author"]/@content')
        article.add_xpath("author", '//span[@itemprop = "author creator"]/span[@itemprop = "name"]/text()')

        article.add_xpath("time", '//meta[@itemprop = "datePublished"]/@content')
        article.add_xpath("description", '//meta[@property = "og:description"]/@content', Join())

        article.add_xpath("body", '//div[contains(@class, "story-body")]/p[contains(@class, "story-body-text")]/text()', Join())
        article.add_xpath("body", '//p[contains(@itemprop, "articleBody")]/text()', Join())
        article.add_xpath("body", '//p[contains(@itemprop, "reviewBody")]/text()', Join())

        item = article.load_item()
        # return item
        yield(item)

        # # try_headlines = LinkExtractor(allow=(),
        # #                 restrict_xpaths = '//ancestor::h2[contains(@class, "headline")]',
        # #                 unique = True).extract_links(response)
        #
        # try_headlines = LinkExtractor(allow=(),
        #                 restrict_xpaths = '//div[contains(@class, "featured")]',
        #                 unique = True).extract_links(response)
        #
        # try_headlines_not_featured = LinkExtractor(allow=(),
        #                 restrict_xpaths = '//div[not(contains(@class, "featured")) and contains(@class, "rank-template")]',
        #                 unique = True).extract_links(response)
        #
        # try_articles_stream = LinkExtractor(allow=(),
        #                 restrict_xpaths = '//div[contains(@class, "stream")]/ol[not(contains(@class, "hidden"))]',
        #                 unique = True).extract_links(response)
        #
        # find_section_headers = LinkExtractor(allow=(),
        #                 restrict_xpaths = '//main//header[contains(@class, "section-header")]',
        #                 unique = True).extract_links(response)


# //span[contains(text(),'someText')]/ancestor::div[contains(@class, 'measure-tab')]


        # LinkExtractor(restrict_xpaths="//*[not(contains(text(),'@'))]")

        # json_thingy = {}
        # json_thingy[response.url] = len(try_headlines_not_featured)

        # json_thingy = {}
        # json_thingy[response.url] = len(try_articles_stream)

        # json_thingy = {}


        # json_thingy[response.url] = [link.url for link in try_section_headers]
        #
        # #
        # # return response.meta
        #
        #
        # return json_thingy


#
#
# "https://www.nytimes.com/svc/collections/v1/publish/www.nytimes.com/section/technology/personaltech?q=&sort=newest&page=0&dom=www.nytimes.com&dedupe_hl=y".split("0")
#
# list(range(0, 5))
#
# for i in range(0, 6):
#     print(i)
#
# init_json = json.load(response.body)
#
#
# from urllib.request import urlopen
# pew = urlopen("http://www.nytimes.com/1981/07/19/business/l-predicting-profits-198384.html")
# print(pew.getcode())
# import json

# urlopen("https://www.nytimes.com/svc/collections/v1/publish/www.nytimes.com/section/technology/personaltech?q=&sort=newest&page=0&dom=www.nytimes.com&dedupe_hl=y")
# result = json.load(urlopen("https://www.nytimes.com/svc/collections/v1/publish/www.nytimes.com/section/technology/personaltech?q=&sort=newest&page=0&dom=www.nytimes.com&dedupe_hl=y"))
# # result = json.load(urlopen("https://www.nytimes.com/svc/collections/v1/publish/www.nytimes.com/column/trilobites?q=&sort=newest&page=0&dom=www.nytimes.com&dedupe_hl=y"))
#
# # result["container355290000"]
# try:
#
#
# first_container = result[[i for i in list(result.keys()) if i.startswith("container")][0]]
# first_final_label = list(result[[i for i in list(result.keys()) if i.startswith("container")][0]].keys())[0]
# for featured_article in first_container[first_final_label]["items"]:
#     featured_article_to_parse = featured_article["url"]
#
#
# except IndexError:
#     pass
#
#
#
# first_final_label = list(result[[i for i in list(result.keys()) if i.startswith("container")][0]].keys())[0]
#
# # almost_featured_label
#
# len(first_container[first_final_label])
# first_container[first_final_label].keys()
#
#
# first_container[first_final_label]["count"]
#
# len(first_container[first_final_label]["items"])
#
# second_container = result["members"]
# second_container.keys()
# len(second_container)
# second_container["total_pages"]
# len(second_container["items"])
#
# second_one["items"][0]

#
#
#
# <div class="story-body story-body-1">
# <p class="story-body-text story-content" data-para-count="##" data-total-count="##">

# json.loads("https://www.nytimes.com/svc/collections/v1/publish/www.nytimes.com/section/technology/personaltech?q=&sort=newest&page=0&dom=www.nytimes.com&dedupe_hl=y")
#
# pewset = set()
# pewset.add(5)
# pewset.add(3)
# pewset
# 3 in pewset
# for i in pewset:
#     print(i)


    # def parse_section(self, response):
    #
    #     json_thingy = {}
    #     json_thingy[response.url] = response.url.split("/section/")[1]
    #     return json_thingy

        # i = {}
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        # pass


# //*[@id="mini-navigation"]/ul/li[20]
#mini-navigation > ul > li.shortcuts-D9C94A2B-0364-4D25-8383-592CC66F82D4.domestic


# from urllib.request import urlopen
# pew = urlopen("http://www.nytimes.com/1981/07/19/business/l-predicting-profits-198384.html")
#
# pew.read()
# pew = {"pageconfig":{"ledeMediaSize":"large","keywords":["Brantley in Britain","brantley-in-britain","article-medium","has-embedded-interactive"],"collections":{"columns":["brantleyinbritain"],"sections":["world","europe","arts","theater"]}}}
# pew["pageconfig"]["collections"]["sections"]
