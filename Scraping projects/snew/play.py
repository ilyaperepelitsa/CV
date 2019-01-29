import re

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Enum
from sqlalchemy.sql import select

import pandas as pd

# import shelve
import re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

# import re
import selenium

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

import time
# from scrapy.exceptions import DropItem
#
# import json
# # Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

def init_driver():
    path_to_chromedriver = "/Users/ilyaperepelitsa/chromedriver"
    # PROXY = "localhost:8118"
    # options = webdriver.ChromeOptions()
    # options.add_argument('--proxy-server=http://%s' % PROXY)
    driver = webdriver.Chrome(executable_path = path_to_chromedriver)
    # driver.get("http://check.torproject.org/")
    # driver.get("http://www.whatismyip.com")

    driver.wait = WebDriverWait(driver, 5)
    return driver



def inst_to_dict(inst, delete_id = False):
    dat = {}
    for column in inst.__table__.columns:
        dat[column.name] = getattr(inst, column.name)
    if delete_id:
        dat.pop("num")
    return dat


engine_article = create_engine("sqlite:////Users/ilyaperepelitsa/quant/snew/articles.db", echo = False)
Base_articles = declarative_base()

class Article_entry(Base_articles):
    __tablename__ = "crawled"
    url = Column(String, primary_key = True)
    data_type = Column(String)
    section = Column(String)
    sections = Column(String)
    top_level_section = Column(String)
    section_url = Column(String)
    tone = Column(String)
    headline = Column(String)
    kicker = Column(String)
    author = Column(String)
    time = Column(String)
    description = Column(String)
    body = Column(String)


    def __repr__(self):
        return "<Base_articles(url='%s', data_type='%s', section='%s', sections='%s', top_level_section='%s', section_url='%s', \
                                tone='%s', headline='%s', kicker='%s', author='%s', time='%s', description='%s', body='%s')>"\
        %(self.url, self.data_type, self.section, self.sections, self.top_level_section, self.section_url,
            self.tone, self.headline, self.kicker, self.author, self.time, self.description, self.body)

Base_articles.metadata.create_all(engine_article)
Session_article = sessionmaker(bind = engine_article)
session_article = Session_article()






first_table = pd.DataFrame([inst_to_dict(w) for w in session_article.query(Article_entry)])
first_table.to_csv("~/quant/well.csv")
first_table.shape
#
#
# first_table.loc[first_table["body"] == "nan, nan", "lat"]


first_table.loc[first_table["body"].isin(["", "NA"])].shape
# first_table.loc[first_table["body"].isin(["", "NA"])]["body"]
first_table.loc[first_table["body"].isin(["", "NA"])]
# first_table.replace(first_table.loc[first_table["body"].isin(["", "NA"])]["body"], "NaN", inplace = True)
# first_table.loc[first_table["body"].isin(["", "NA"])].shape
# first_table.loc[first_table["body"] == "NA"].shape
#
# first_table.loc[first_table["data_type"].isin(["", "NA"])].shape
# first_table.loc[first_table["data_type"] == "NA"].shape
#
#
# first_table.loc[first_table["section"].isin(["", "NA"])].shape
# first_table.loc[first_table["section"] == "NA"].shape
#
#
# first_table.loc[first_table["sections"].isin(["", "NA"])].shape
# first_table.loc[first_table["sections"] == "NA"].shape
#
# first_table.loc[first_table["top_level_section"].isin(["", "NA"])].shape
# first_table.loc[first_table["top_level_section"] == "NA"].shape
#
# first_table.loc[first_table["section_url"].isin(["", "NA"])].shape
# first_table.loc[first_table["section_url"] == "NA"].shape
#
#
# first_table.loc[first_table["tone"].isin(["", "NA"])].shape
# first_table.loc[first_table["tone"] == "NA"].shape
#
#
# first_table.loc[first_table["headline"].isin(["", "NA"])].shape
# first_table.loc[first_table["headline"] == "NA"].shape
#
#
# first_table.loc[first_table["kicker"].isin(["", "NA"])].shape
# first_table.loc[first_table["kicker"] == "NA"].shape
#
#
# first_table.loc[first_table["author"].isin(["", "NA"])].shape
# first_table.loc[first_table["author"] == "NA"].shape
#
#
# first_table.loc[first_table["time"].isin(["", "NA"])].shape
# first_table.loc[first_table["time"] == "NA"].shape
#
#
# first_table.loc[first_table["description"].isin(["", "NA"])].shape
# first_table.loc[first_table["description"] == "NA"].shape
first_table.loc[first_table["body"].isin(["", "NA"])].shape
first_table.loc[first_table["body"].isin(["", "NA"])].iloc[1,]["body"]
first_table.loc[first_table["body"].isin(["", "NA"])].iloc[1,]["url"]

browser = init_driver()
browser.wait = WebDriverWait(browser, 5)

doask = True

for article in range(0, first_table.loc[first_table["body"].isin(["", "NA"])].shape[0]):
    if doask == True:
        print(first_table.loc[first_table["body"].isin(["", "NA"])].iloc[article,])
        print("==============================================")
        browser.get(first_table.loc[first_table["body"].isin(["", "NA"])].iloc[article,]["url"])
        some_response = input("What to do next?: ")
        if some_response == "":
            continue
        elif some_response == "quit":
            doask = False
