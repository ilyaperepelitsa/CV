# from datetime import datetime,tzinfo,timedelta
# import json
# import os
#
# from sqlalchemy.orm import sessionmaker
# from sqlalchemy import create_engine
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy import Column, Integer, String, Enum, ForeignKey
# from sqlalchemy.dialects.postgresql import TEXT, VARCHAR, INTEGER
# from sqlalchemy.dialects.postgresql import TIMESTAMP, ARRAY
# from sqlalchemy import Boolean
#
# from sqlalchemy.sql import select
# from sqlalchemy.sql import exists
#
# from pytz import timezone
# import pytz
#
# class Zone(tzinfo):
#     def __init__(self,offset,isdst,name):
#         self.offset = offset
#         self.isdst = isdst
#         self.name = name
#     def utcoffset(self, dt):
#         return timedelta(hours=self.offset) + self.dst(dt)
#     def dst(self, dt):
#             return timedelta(hours=1) if self.isdst else timedelta(0)
#     def tzname(self,dt):
#          return self.name
#
# PST = Zone(0,False,'EST')
# EST = Zone(+3,False,'PST')
#
#
# # import keys
# import pkg_resources
# # json_path = pkg_resources.resource_filename('credentials', 'passwords.json')
#
#
# # data = json.load(open(json_path))
#
# def inst_to_dict(inst, delete_id = True):
#     dat = {}
#     for column in inst.__table__.columns:
#         dat[column.name] = getattr(inst, column.name)
#     # if delete_id:
#     #     dat.pop("num")
#     return dat
#
# # json.loads(s)
#
# # dataslap_postgres = data["aws"]["personal"]["dataslap"]["postgres"]["free_20gb"]["dataslap_user"]
# # dataslap_postgres = keys.get_dataslap_postgres()
#
#
# engine_test = create_engine('postgres://%(username)s:%(password)s@%(host)s:%(port)s/job_search' %
#                             {"username": "dataslap_user",
#                              "password": "7867booba11OI2",
#                              "host": "dataslap.c55v1zqbho3l.us-east-2.rds.amazonaws.com",
#                              "port": 5432})
# Base_item = declarative_base()
#
#
#
# class Url_entry(Base_item):
#     __tablename__ = "urls"
#     url_id = Column(INTEGER, primary_key=True)
#     url = Column(TEXT, unique=True)
#
#     def __repr__(self):
#         return "<Base_item(url_id='%s', url='%s')>"\
#             % (self.url_id, self.url)
#
# class External_url_entry(Base_item):
#     __tablename__ = "external_urls"
#     external_url_id = Column(INTEGER, primary_key=True)
#     external_url = Column(TEXT, unique=True)
#
#     def __repr__(self):
#         return "<Base_item(external_url_id='%s', external_url='%s')>"\
#             % (self.external_url_id, self.external_url)
#
#
# class Company_entry(Base_item):
#     __tablename__ = "companies"
#     company_id = Column(INTEGER, primary_key=True)
#     company_name = Column(TEXT, unique=True)
#
#     def __repr__(self):
#         return "<Base_item(company_id='%s', company_name='%s')>"\
#             % (self.company_id, self.company_name)
#
#
# class Title_entry(Base_item):
#     __tablename__ = "titles"
#     title_id = Column(INTEGER, primary_key=True)
#     job_title = Column(TEXT, unique=True)
#
#     def __repr__(self):
#         return "<Base_item(title_id='%s', job_title='%s')>"\
#             % (self.title_id, self.job_title)
#
# class Job_description_entry(Base_item):
#     __tablename__ = "job_descriptions"
#     job_description_id = Column(INTEGER, primary_key=True)
#     job_description = Column(TEXT, nullable=False)
#
#     def __repr__(self):
#         return "<Base_item(job_description_id='%s', job_description='%s')>"\
#             % (self.job_description_id, self.job_description)
#
# class Job_entry(Base_item):
#     __tablename__ = "jobs"
#     job_id = Column(INTEGER, primary_key=True)
#     url_id = Column(INTEGER, ForeignKey("urls.url_id"), nullable=False)
#     external_url_id = Column(INTEGER, ForeignKey("external_urls.external_url_id"), nullable=True)
#     company_id = Column(INTEGER, ForeignKey(
#         "companies.company_id"), nullable=False)
#
#     title_id = Column(INTEGER, ForeignKey(
#         "titles.title_id"), nullable=False)
#     job_description_id = Column(INTEGER, ForeignKey(
#         "job_descriptions.job_description_id"), nullable=False)
#     location_id = Column(INTEGER, ForeignKey(
#         "locations.location_id"), nullable=False)
#     country_id = Column(INTEGER, ForeignKey(
#         "countries.country_id"), nullable=False)
#     date_published = Column(TIMESTAMP, nullable=False)
#     # '2016-06-22 19:10:25-07'
#     date_scraped = Column(TIMESTAMP, nullable=False)
#     source_id = Column(INTEGER, ForeignKey(
#         "sources.source_id"), nullable=False)
#     page_source_id = Column(INTEGER, ForeignKey(
#         "page_sources.page_source_id"), nullable=False)
#     page_external_source_id = Column(INTEGER, ForeignKey(
#         "page_external_sources.page_external_source_id"), nullable=True)
#
#     def __repr__(self):
#         return "<Base_item(job_id='%s', url_id='%s', external_url_id='%s', company_id='%s',\
#                             title_id='%s', job_description_id='%s', location_id='%s',\
#                             country_id='%s', date_published='%s', date_scraped='%s',\
#                             source_id='%s', page_source_id='%s',\
#                             page_external_source_id='%s')>"\
#         % (self.job_id, self.url_id, self.external_url_id, self.company_id, self.title_id, self.job_description_id,
#             self.location_id, self.country_id, self.date_published, self.date_scraped,
#             self.source_id, self.page_source_id, self.page_external_source_id)
#
#
# class Location_entry(Base_item):
#     __tablename__ = "locations"
#     location_id = Column(INTEGER, primary_key=True)
#     location_name = Column(VARCHAR(50), unique=True)
#
#     def __repr__(self):
#         return "<Base_item(location_id='%s', location_name='%s')>"\
#             % (self.location_id, self.location_name)
#
#
# class Country_entry(Base_item):
#     __tablename__ = "countries"
#     country_id = Column(INTEGER, primary_key=True)
#     country_name = Column(VARCHAR(50), unique=True)
#
#     def __repr__(self):
#         return "<Base_item(country_id='%s', country_name='%s')>"\
#             % (self.country_id, self.country_name)
#
#
# class Source_entry(Base_item):
#     __tablename__ = "sources"
#     source_id = Column(INTEGER, primary_key=True)
#     source_name = Column(VARCHAR(20), unique=True)
#
#     def __repr__(self):
#         return "<Base_item(source_id='%s', source_name='%s')>"\
#             % (self.source_id, self.source_name)
#
#
# class Page_source_entry(Base_item):
#     __tablename__ = "page_sources"
#     page_source_id = Column(INTEGER, primary_key=True)
#     page_source_html = Column(TEXT, nullable=False)
#     page_source_text = Column(TEXT, nullable=False)
#
#     def __repr__(self):
#         return "<Base_item(page_source_id='%s', page_source_html='%s',\
#                             page_source_text='%s')>"\
#         % (self.page_source_id, self.page_source_html, self.page_source_text)
#
#
# class Page_external_source_entry(Base_item):
#     __tablename__ = "page_external_sources"
#     page_external_source_id = Column(INTEGER, primary_key=True)
#     page_external_source_html = Column(TEXT, nullable=False)
#     page_external_source_text = Column(TEXT, nullable=False)
#
#     def __repr__(self):
#         return "<Base_item(page_external_source_id='%s', page_external_source_html='%s',\
#                             page_external_source_text='%s')>"\
#         % (self.page_external_source_id, self.page_external_source_html,
#            self.page_external_source_text)
#
#
# class Job_label_entry(Base_item):
#     __tablename__ = "labeled_jobs"
#     label_id = Column(INTEGER, primary_key=True)
#     job_id = Column(INTEGER, ForeignKey("jobs.job_id"), nullable=False)
#     apply_label = Column(Boolean)
#     apply_timestamp = Column(TIMESTAMP)
#     skill_focus = Column(ARRAY(INTEGER, dimensions=1), nullable=True)
#
#     def __repr__(self):
#         return "<Base_item(label_id='%s', job_id='%s',\
#                             apply_label='%s', apply_timestamp='%s',\
#                              skill_focus='%s')>"\
#         % (self.job_id, self.apply_label, self.apply_label, self.apply_timestamp, self.skill_focus)
#
# class Job_apply_entry(Base_item):
#     __tablename__ = "applied_jobs"
#     applied_id = Column(INTEGER, primary_key=True)
#     job_id = Column(INTEGER, ForeignKey("jobs.job_id"), nullable=False)
#     applied_timestamp = Column(TIMESTAMP)
#
#     def __repr__(self):
#         return "<Base_item(applied_id='%s', job_id='%s',\
#                             applied_timestamp='%s')>"\
#         % (self.applied_id, self.job_id, self.applied_timestamp)
#
#
# class Skill_focus_entry(Base_item):
#     __tablename__ = "skill_focuses"
#     skill_id = Column(INTEGER, primary_key=True)
#     skill_label = Column(VARCHAR(20), nullable=False, unique=True)
#
#     def __repr__(self):
#         return "<Base_item(skill_id='%s', skill_label='%s')>"\
#             % (self.skill_id, self.skill_label)
#
#
# class Skill_paragraph_entry(Base_item):
#     __tablename__ = "skill_paragraphs"
#     paragraph_id = Column(INTEGER, primary_key=True)
#     skill_label = Column(VARCHAR(20), ForeignKey(
#         "skill_focuses.skill_label"), nullable=False)
#     skill_paragraph_text = Column(TEXT, nullable=False)
#     skill_paragraph_added = Column(TIMESTAMP)
#
#     def __repr__(self):
#         return "<Base_item(paragraph_id='%s', skill_label='%s', skill_paragraph_text='%s',\
#                                 skill_paragraph_added='%s')>"\
#         % (self.paragraph_id, self.skill_label, self.skill_paragraph_text, self.skill_paragraph_added)
#
#
# Base_item.metadata.create_all(engine_test)
# Session_test = sessionmaker(bind=engine_test)
# session_test = Session_test()
#
#
# for i in list(range(1, 100)):
#
#     second_query = session_test.query(Job_entry).\
#                         filter(Job_entry.company_id == i,
#                                 Job_entry.title_id == 1,
#                                 Job_entry.location_id == 1,
#                                 Job_entry.country_id == 1)
#
#     # print(second_query)
#     if len([inst_to_dict(q) for q in second_query]) > 1:
#         print(i)
#
#
#
#
# if session_test.query(Job_entry).\
#                     filter(Job_entry.company_id == 1,
#                             Job_entry.title_id == 1,
#                             Job_entry.location_id == 1,
#                             Job_entry.country_id == 1).scalar():
#     print("pew")
#
#
#
#
#
#
#
#
# len([inst_to_dict(q) for q in second_query])
#
# tz = pytz.timezone('Asia/Taipei')
# d = d.replace(tzinfo=tz)
#
#
# date_output = datetime.now(timezone('US/Eastern')) - timedelta(days=int(5))
# # job.add_value('date_added', date_output)
#
# (datetime.now(timezone('US/Eastern')) - date_output).days
# engine_test.dispose()
