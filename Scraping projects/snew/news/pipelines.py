# -*- coding: utf-8 -*-
import re

from news.models import *

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Enum
from sqlalchemy.sql import select

from scrapy.exceptions import DropItem
import dateutil.parser
import json
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

def inst_to_dict(inst, delete_id = True):
    dat = {}
    for column in inst.__table__.columns:
        dat[column.name] = getattr(inst, column.name)
    # if delete_id:
    #     dat.pop("num")
    return dat
#

from datetime import datetime,tzinfo,timedelta


class Zone(tzinfo):
    def __init__(self,offset,isdst,name):
        self.offset = offset
        self.isdst = isdst
        self.name = name
    def utcoffset(self, dt):
        return timedelta(hours=self.offset) + self.dst(dt)
    def dst(self, dt):
            return timedelta(hours=1) if self.isdst else timedelta(0)
    def tzname(self,dt):
         return self.name

PST = Zone(0,False,'EST')
EST = Zone(+3,False,'PST')



#
# engine_article = create_engine("sqlite:////Users/ilyaperepelitsa/quant/snew/articles.db", echo = False)
# Base_articles = declarative_base()
#
# class Article_entry(Base_articles):
#     __tablename__ = "crawled"
#     url = Column(String, primary_key = True)
#     data_type = Column(String)
#     section = Column(String)
#     sections = Column(String)
#     top_level_section = Column(String)
#     section_url = Column(String)
#     tone = Column(String)
#     headline = Column(String)
#     kicker = Column(String)
#     author = Column(String)
#     time = Column(String)
#     description = Column(String)
#     body = Column(String)
#
#
#     def __repr__(self):
#         return "<Base_articles(url='%s', data_type='%s', section='%s', sections='%s', top_level_section='%s', section_url='%s', \
#                                 tone='%s', headline='%s', kicker='%s', author='%s', time='%s', description='%s', body='%s')>"\
#         %(self.url, self.data_type, self.section, self.sections, self.top_level_section, self.section_url,
#             self.tone, self.headline, self.kicker, self.author, self.time, self.description, self.body)
#
# Base_articles.metadata.create_all(engine_article)
# Session_article = sessionmaker(bind = engine_article)
# session_article = Session_article()




class ProcessArticle(object):
    def process_item(self, item, spider):

        # item["body"] = [re.sub('\t+', '', body_par).strip() for body_par in item["body"]]
        # item["body"] = [re.sub('\s+', ' ', body_par).strip() for body_par in item["body"]]
        # item["body"] = [body_par for body_par in item["body"] if body_par != ""]
        # item["body"] = [body_par for body_par in item["body"] if body_par != " "]
        # item["body"] = ' '.join(item["body"])
        ########################################################################
        item["url"] = "".join(item["url"])
        if item["url"] == "":
            item["url"] = "NA"
        ########################################################################
        try:
            if len(item["data_type"]) == 1:
                item["data_type"] = "".join(item["data_type"])
            else:
                item["data_type"] = ", ".join(item["data_type"])
        except (KeyError, TypeError):
            item["data_type"] = "NA"

        if item["data_type"] == "":
            item["data_type"] = "NA"
        ########################################################################
        try:
            if len(item["section"]) == 1:
                item["section"] = "".join(item["section"])
            else:
                item["section"] = ", ".join(item["section"])

        except (KeyError, TypeError):
            item["section"] = "NA"

        if item["section"] == "":
            item["section"] = "NA"
        ########################################################################

        try:
            item["sections"] = "".join([block for block in item["sections"] if block not in ["\n", ""]])
            item["sections"] = json.loads(item["sections"])
            item["sections"] = item["pageconfig"]["collections"]["sections"]

            if len(item["sections"]) == 1:
                item["sections"] = "".join(item["sections"])
            else:
                item["sections"] = ", ".join(item["sections"])

        except (KeyError, TypeError):
            item["sections"] = "NA"

        if item["sections"] == "":
            item["sections"] = "NA"
        ########################################################################
        try:
            if len(item["top_level_section"]) == 1:
                item["top_level_section"] = "".join(item["top_level_section"])
            else:
                item["top_level_section"] = ", ".join(item["top_level_section"])
        except (KeyError, TypeError):
            item["top_level_section"] = "NA"

        if item["top_level_section"] == "":
            item["top_level_section"] = "NA"
        ########################################################################
        # item["section_url"] = "".join(item["section_url"])
        try:
            if len(item["section_url"]) == 1:
                item["section_url"] = "".join(item["section_url"])
            else:
                item["section_url"] = ", ".join(item["section_url"])

        except (KeyError, TypeError):
            item["section_url"] = "NA"

        if item["section_url"] == "":
            item["section_url"] = "NA"
        ########################################################################
        # item["tone"] = "".join(item["tone"])
        try:
            if len(item["tone"]) == 1:
                item["tone"] = "".join(item["tone"])
            else:
                item["tone"] = ", ".join(item["tone"])
        except (KeyError, TypeError):
            item["tone"] = "NA"

        if item["tone"] == "":
            item["tone"] = "NA"
        ########################################################################
        item["headline"] = [re.sub('\t+', '', headline_par).strip() for headline_par in item["headline"]]
        item["headline"] = [re.sub('\s+', ' ', headline_par).strip() for headline_par in item["headline"]]
        item["headline"] = [headline_par for headline_par in item["headline"] if headline_par != ""]
        item["headline"] = [headline_par for headline_par in item["headline"] if headline_par != " "]


        # item["headline"] = ' '.join(item["headline"])
        try:
            if len(item["headline"]) == 1:
                item["headline"] = "".join(item["headline"])
            else:
                item["headline"] = ", ".join(item["headline"])
        except (KeyError, TypeError):
            item["headline"] = "NA"


        if item["headline"] == "":
            item["headline"] = "NA"
        ########################################################################
        try:
            item["kicker"] = "".join(item["kicker"])
        except (KeyError, TypeError):
            item["kicker"] = "NA"
        # if len(item["headline"]) == 1:
        #     item["headline"] = "".join(item["headline"])
        # else:
        #     item["headline"] = ", ".join(item["headline"])

        if item["kicker"] == "":
            item["kicker"] = "NA"
        ########################################################################

        # item["author"] = "".join(item["author"])
        try:
            if len(item["author"]) == 1:
                item["author"] = "".join(item["author"])
            else:
                item["author"] = ", ".join(item["author"])
        except (KeyError, TypeError):
            item["author"] = "NA"

        if item["author"] == "":
            item["author"] = "NA"
        ########################################################################
        try:
            item["time"] = "".join(item["time"])
        except (KeyError, TypeError):
            item["time"] = "NA"
        # if len(item["headline"]) == 1:
        #     item["headline"] = "".join(item["headline"])
        # else:
        #     item["headline"] = ", ".join(item["headline"])

        if item["time"] == "":
            item["time"] = "NA"
        ########################################################################
        try:
            item["description"] = [re.sub('\t+', '', description_par).strip() for description_par in item["description"]]
            item["description"] = [re.sub('\s+', ' ', description_par).strip() for description_par in item["description"]]
            item["description"] = [description_par.strip() for description_par in item["description"] if description_par != ""]
            item["description"] = [description_par.strip() for description_par in item["description"] if description_par != " "]
            item["description"] = ''.join(item["description"])
        except (KeyError, TypeError):
            item["description"] = "NA"
        # if len(item["description"]) == 1:
        #     item["description"] = "".join(item["description"])
        # else:
        #     item["description"] = ", ".join(item["description"])

        if item["description"] == "":
            item["description"] = "NA"
        ########################################################################
        try:
            item["body"] = [re.sub('\t+', '', body_par).strip() for body_par in item["body"]]
            item["body"] = [re.sub('\\n', '', body_par).strip() for body_par in item["body"]]
            item["body"] = [re.sub('\s+', ' ', body_par).strip() for body_par in item["body"]]
            item["body"] = [body_par.strip() for body_par in item["body"] if body_par != ""]
            item["body"] = [body_par.strip() for body_par in item["body"] if body_par != " "]
            item["body"] = ''.join(item["body"])
        except (KeyError, TypeError):
            item["body"] = "NA"
        # if len(item["headline"]) == 1:
        #     item["headline"] = "".join(item["headline"])
        # else:
        #     item["headline"] = ", ".join(item["headline"])
        if item["body"] == "":
            item["body"] = "NA"


        # ["pageconfig"]["collections"]["sections"]

        # item["sections"] = [block for block in item["sections"] if block != "/\n"]
        # ["pageconfig"]["collections"]["sections"]

        # item["sections"] = json.loads(item["sections"][0])["pageconfig"]["collections"]["sections"]
        # item["sections"] = item["sections"]["pageconfig"]["collections"]["sections"]
        # item["sections"] = item["sections"]["collections"]
        # item["sections"] = item["sections"]["sections"]
        # ["pageconfig"]["collections"]["sections"]

        # item["headers"] = [re.sub( '\t+', '', header).strip() for header in item["headers"]]
        # item["headers"] = [re.sub( '\s+', ' ', header).strip() for header in item["headers"]]
        # item["headers"] = [header for header in item["headers"] if header != ""]
        # item["headers"] = ' '.join(item["headers"])
        #
        # item["paragraphs"] = [re.sub( '\t+', '', paragraph).strip() for paragraph in item["paragraphs"]]
        # item["paragraphs"] = [re.sub( '\s+', ' ', paragraph).strip() for paragraph in item["paragraphs"]]
        # item["paragraphs"] = [paragraph for paragraph in item["paragraphs"] if paragraph != ""]
        # item["paragraphs"] = ' '.join(item["paragraphs"])
        #
        # item["links_text"] = [re.sub( '\t+', '', link_text).strip() for link_text in item["links_text"]]
        # item["links_text"] = [re.sub( '\s+', ' ', link_text).strip() for link_text in item["links_text"]]
        # item["links_text"] = [link_text for link_text in item["links_text"] if link_text != ""]
        # item["links_text"] = ' '.join(item["links_text"])
        #
        # item["time"] = item["time"][0]
        #
        # item["url"] = item["url"][0]
        #
        # # item["domain"] = item["url"][0].replace("http://","").replace("https://","").replace("www.", "").replace("ww2.", "").strip()
        # item["domain"] = item["url"].replace("http://","").replace("https://","").replace("www.", "").replace("ww2.", "").strip().split("/")[0]
        #
        #
        # if item['paragraphs'] == "":
        #     raise DropItem("Missing paragraph in %s" % item)
        # else:
        #     return item

        return item


class ProcessArticleGeneric(object):
    def process_item(self, item, spider):
        ########################################################################
        item["url"] = "".join(item["url"])
        if item["url"] == "":
            item["url"] = "NA"

        ########################################################################
        try:
            item["article_text"] = [re.sub('\t+', '', body_par).strip() for body_par in item["article_text"]]
            item["article_text"] = [re.sub('\s+', ' ', body_par).strip() for body_par in item["article_text"]]
            item["article_text"] = [body_par for body_par in item["article_text"] if body_par != ""]
            item["article_text"] = [body_par for body_par in item["article_text"] if body_par != " "]
            item["article_text"] = ' '.join(item["article_text"])
        except KeyError:
            raise DropItem("___________________Article has no text %s" % item["url"])

        if item["article_text"].strip() == "":
            raise DropItem("___________________Article has no text %s" % item["url"])

        ########################################################################
        item["article_title"] = [re.sub('\t+', '', headline_par).strip() for headline_par in item["article_title"]]
        item["article_title"] = [re.sub('\s+', ' ', headline_par).strip() for headline_par in item["article_title"]]
        item["article_title"] = [headline_par for headline_par in item["article_title"] if headline_par != ""]
        item["article_title"] = [headline_par for headline_par in item["article_title"] if headline_par != " "]


        # item["headline"] = ' '.join(item["headline"])
        try:
            if len(item["article_title"]) == 1:
                item["article_title"] = "".join(item["article_title"])
            else:
                item["article_title"] = ", ".join(item["article_title"])
        except (KeyError, TypeError):
            item["article_title"] = "NA"


        if item["article_title"] == "":
            item["article_title"] = "NA"
        ########################################################################
        # try:
        #     item["kicker"] = "".join(item["kicker"])
        # except (KeyError, TypeError):
        #     item["kicker"] = "NA"
        # # if len(item["headline"]) == 1:
        # #     item["headline"] = "".join(item["headline"])
        # # else:
        # #     item["headline"] = ", ".join(item["headline"])
        #
        # if item["kicker"] == "":
        #     item["kicker"] = "NA"
        ########################################################################

        # item["author"] = "".join(item["author"])
        # try:
        #     if len(item["author_name"]) == 1:
        #         item["author_name"] = "".join(item["author_name"])
            # else:
            #     item["author_name"] = ", ".join(item["author_name"])
        # except (KeyError, TypeError):
        #     item["author_name"] = "NA"
        try:
            if item["author_name"] == "" or len(item["author_name"]) < 1 :
                item["author_name"] = "NA"
        except KeyError:
            try:
                item["author_name"] = list(map(lambda x: x.replace("by ", "").strip(), item["author_name_alt"]))
                item["author_name"] = list(map(lambda x: x.replace("\n", "").strip(), item["author_name"]))
                item["author_name"] = list(map(lambda x: x.replace("\t", "").strip(), item["author_name"]))
                item["author_name"] = list(map(lambda x: re.sub('^by\s', '', x), item["author_name"]))
                item["author_name"].remove("Posted")
                item["author_name"] = [author_name for author_name in item["author_name"] if author_name.strip() != ""]
                item["author_name"].remove("Posted")
            except (KeyError, NameError):
                raise DropItem("___________________Article has no author %s" % item["url"])

        if item["author_name"] == "NA":
            raise DropItem("___________________Article has no author %s" % item["url"])
        ########################################################################
        try:
            item["date_published"] = "".join(item["date_published"])
        except (KeyError, TypeError):
            item["date_published"] = "NA"
            raise DropItem("___________________No date - no article %s" % item["url"])
        # if len(item["headline"]) == 1:
        #     item["headline"] = "".join(item["headline"])
        # else:
        #     item["headline"] = ", ".join(item["headline"])

        if item["date_published"] == "":
            item["date_published"] = "NA"
            raise DropItem("___________________No date - no article %s" % item["url"])

        # yourdate = dateutil.parser.parse(datestring)

        parsed_date = dateutil.parser.parse(item["date_published"])
        parsed_date = parsed_date.replace(tzinfo=PST)
        parsed_date = parsed_date.astimezone(EST).replace(tzinfo=None)
        item["date_published"] = parsed_date

        ########################################################################

        item["date_scraped"] = datetime.now()
        item["source_spider"] = "techcrunch"
        item["source_domain"] = "techcrunch.com"


        ########################################################################
        item["author_name_alt"] = ""
        return item




class RecordArticle(object):
    def process_item(self, item, spider):

        article_entry = {"url" : item["url"],
                        "data_type" : item["data_type"],
                        "section" : item["section"],
                        "sections" : item["sections"],
                        "top_level_section" : item["top_level_section"],
                        "section_url" : item["section_url"],
                        "tone" : item["tone"],
                        "headline" : item["headline"],
                        "kicker" : item["kicker"],
                        "author" : item["author"],
                        "time" : item["time"],
                        "description" : item["description"],
                        "body" : item["body"]}

        session_article.add(Article_entry(**article_entry))
        session_article.commit()
        yield item


class RecordAlt(object):
    def process_item(self, item, spider):

        url_entry = {"url" : item["url"]}

        url_exists = session_test.query(exists().where(Url_entry.url==item["url"])).scalar()
        if not url_exists:
            adding_url = Url_entry(**url_entry)
            session_test.add(adding_url)
            session_test.commit()
            session_test.refresh(adding_url)
            url_id = adding_url.url_id
            # article_entry["source_id"] = url_id


            article_entry = {"url_id" : url_id,
                            "article_text" : item["article_text"],
                            "article_title" : item["article_title"],
                            "author_id" : [],
                            "date_published" : item["date_published"],
                            "date_scraped" : item["date_scraped"],
                            # "source_spider" : item["source_spider"],
                            "source_id" : ""}

        # article_exists = session_test.query(exists().where(Article_entry.url==item["url"])).scalar()
        # if not article_exists:
        # list(set(t))
            for author in list(set(item["author_name"])):
                author_entry = {"author_name" : author}
                author_exists = session_test.query(exists().where(Author_entry.author_name==author)).scalar()
                if author_exists:
                    author_query = session_test.query(Author_entry).filter(Author_entry.author_name == author).one()
                    author_result = inst_to_dict(author_query)["author_id"]
                    article_entry["author_id"].append(author_result)
                else:
                    adding_author = Author_entry(**author_entry)
                    session_test.add(adding_author)
                    session_test.commit()
                    session_test.refresh(adding_author)
                    author_id = adding_author.author_id
                    article_entry["author_id"].append(author_id)

            source_entry = {"source_spider" : item["source_spider"],
                            "source_domain" : item["source_domain"]}
            source_exists = session_test.query(exists().where(Source_entry.source_spider==item["source_spider"])).scalar()
            if source_exists:
                source_query = session_test.query(Source_entry).filter(Source_entry.source_spider == item["source_spider"]).one()
                # source_result = inst_to_dict(source_query)
                source_result = inst_to_dict(source_query)["source_id"]
                article_entry["source_id"] = source_result

            else:
                adding_source = Source_entry(**source_entry)
                session_test.add(adding_source)
                session_test.commit()
                session_test.refresh(adding_source)
                source_id = adding_source.source_id
                article_entry["source_id"] = source_id

            session_test.add(Article_entry(**article_entry))
            session_test.commit()
            return item
        else:
            raise DropItem("Article already exists %s" % item["url"])


        # ret = session_test.query(exists().where(Article_entry.url=="google.com")).scalar()

        # session_job.query(Job_entry).filter(Job_entry.job_text == item["job_text"]).first()
        #
        # if len([inst_to_dict(w) for w in session_article.query(Article_entry).filter(Article_entry.url == item["url"])]) == 0:
        #     session_article.add(Article_entry(**article_entry))
        #     session_article.commit()
        #     return item
        # else:
        #     raise DropItem("Article already exists %s" % item)



# pew = ['\n','{"pageconfig":{"ledeMediaSize":"none","keywords":["THE 2004 ELECTIONS: THE NEW YORK REGION","article-short"],"collections":[]}}']
