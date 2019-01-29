# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field


# class ArticleItem(Item):
#     # Meta data
#     url = Field()
#     data_type = Field()
#     section = Field()
#     sections = Field()
#     top_level_section = Field()
#     section_url = Field()
#     tone = Field()
#
#     # Content
#     headline = Field()
#     kicker = Field()
#     author = Field()
#     time = Field()
#     description = Field()
#     body = Field()
#     pass


class ArticleItem(Item):
    # Meta data
    url = Field()
    article_text = Field()
    article_title = Field()
    author_name = Field()
    author_name_alt = Field()
    date_published = Field()
    date_scraped = Field()
    source_spider = Field()
    source_domain = Field()

    pass
# import json


# from scrapy.loader.processors import MapCompose, Join
#
# pew = '{"pageconfig":{"ledeMediaSize":"jumbo","keywords":["A Good Appetite","a-good-appetite","article-medium","has-embedded-interactive"],"collections":{"columns":["agoodappetite"],"sections":["personaltechnology","food"]}}}'
#
#
# sentence = ['this','is','a','sentence']
# '-'.join(sentence)
#
# parser = MapCompose(lambda extracted_json: json.loads(extracted_json),
#                     lambda loaded_json: loaded_json["pageconfig"]["collections"]["sections"])
# parser(pew)
#
# pewpew = parser(pew)
# Join(", ")(pewpew)
#
# json.loads(pew)
