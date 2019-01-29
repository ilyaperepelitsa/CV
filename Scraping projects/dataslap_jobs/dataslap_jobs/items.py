# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html
from scrapy.item import Item, Field
import json

class JobItem(Item):
    # Meta data

    url = Field()

    # company website irrelevant
    job_company = Field()
    # company_website = Field()

    job_position = Field()
    job_text = Field()

    # NEW > ADD TO SPIDER
    location = Field()
    country = Field()
    date_added = Field()
    date_scraped = Field()


    #BACK TO OLD
    source = Field()

    # NEW > ADD TO SPIDER
    # page_source_html = Field()
    page_source_text = Field()

    # NEW > ADD TO SPIDER
    external_url = Field()
    # page_external_source_html = Field()
    page_external_source_text = Field()


    # def __repr__(self):
    #         """Only print out certain elements"""
    #         return {"url": self.url, "job_company": self.job_company,
    #         "job_position": self.job_position, "job_text": self.job_text[0:200],
    #         "location": self.location, "country": self.country,
    #         "date_added": self.date_added, "date_scraped": self.date_scraped,
    #         "source": self.source, "page_source_text": len(self.page_source_text),
    #         "external_url": self.external_url, "page_external_source_text": len(self.page_external_source_text)}
    def __repr__(self):
        r = {}
        for attr, value in self.__dict__["_values"].items():
            if attr in ["page_external_source_text", "page_source_text"]:
                try:
                    r[attr] = len(value)
                except TypeError:
                    r[attr] = None
            elif attr in ["job_text"]:
                r[attr] = value[0:200]
            else:
                r[attr] = str(value)
        return json.dumps(r, sort_keys = True, indent = 4, separators = (",", ": "), default = str)
