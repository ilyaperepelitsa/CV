

# -*- coding: utf-8 -*-

import re
#pew
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Enum
from sqlalchemy.sql import select
from sqlalchemy import desc
# import dateutil.parser
# from dateutil import tz, parser
from datetime import datetime,tzinfo,timedelta, time
from pytz import timezone


from scrapy.exceptions import DropItem

from dataslap_jobs.models import *

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


# class ProcessJob(object):
#     def process_item(self, item, spider):
#         ########################################################################
#         # item["url"] = [re.sub('\t+', '', list_item).strip() for list_item in item["url"]]
#         # item["url"] = [re.sub('\s+', ' ', list_item).strip() for list_item in item["url"]]
#         # # item["url"] = "".join(item["url"])
#         # if item["url"] == "":
#         #     item["url"] = "NA"
#         item["source"] = "".join(item["source"])
#         item["url"] = "".join(item["url"])
#         ###############
#         ###############
#         ###############
#         ###############
#         try:
#             item["job_position"] = [
#                 re.sub('\t+', '', list_item).strip() for list_item in item["job_position"]]
#             item["job_position"] = [
#                 re.sub('\s+', ' ', list_item).strip() for list_item in item["job_position"]]
#             item["job_position"] = item["job_position"][0]
#         except (KeyError, TypeError):
#             item["job_position"] = "NA"
#         ########################################################################
#         # try:
#         #     item["job_salary_med"] = [
#         #         re.sub('\t+', '', list_item).strip() for list_item in item["job_salary_med"]]
#         #     item["job_salary_med"] = [
#         #         re.sub('\s+', ' ', list_item).strip() for list_item in item["job_salary_med"]]
#         #     item["job_salary_med"] = item["job_salary_med"][0]
#         #     item["job_salary_med"] = re.search(
#         #         'salary is \$(.+?). ', item["job_salary_med"])
#         #     item["job_salary_med"] = item["job_salary_med"][1].replace(
#         #         ".00", "").replace(",", "")
#         # except (KeyError, TypeError):
#         #     item["job_salary_med"] = "NA"
#         ########################################################################
#         try:
#             item["job_company"] = [
#                 re.sub('\t+', '', list_item).strip() for list_item in item["job_company"]]
#             item["job_company"] = [
#                 re.sub('\s+', ' ', list_item).strip() for list_item in item["job_company"]]
#             item["job_company"] = item["job_company"][0]
#             item["job_company"] = re.search(
#                 '(.+) is now hiring', item["job_company"])
#             item["job_company"] = item["job_company"][1]
#         except (KeyError, TypeError):
#             item["job_company"] = "NA"
#         ########################################################################
#         try:
#             item["job_text"] = [re.sub('\t+', '', list_item).strip()
#                                 for list_item in item["job_text"]]
#             item["job_text"] = [re.sub('\s+', ' ', list_item).strip()
#                                 for list_item in item["job_text"]]
#             item["job_text"] = " ".join(item["job_text"])
#         except (KeyError, TypeError):
#             item["job_text"] = "NA"
#         ########################################################################
#         try:
#             item["job_lists"] = [re.sub('\t+', '', list_item).strip()
#                                  for list_item in item["job_lists"]]
#             item["job_lists"] = [re.sub('\s+', ' ', list_item).strip()
#                                  for list_item in item["job_lists"]]
#             item["job_lists"] = "***|||***".join(item["job_lists"])
#         except KeyError:
#             item["job_lists"] = "NA"
#
#         ########################################################################
#         try:
#             item["job_apply_link"] = [
#                 re.sub('\t+', '', list_item).strip() for list_item in item["job_apply_link"]]
#             item["job_apply_link"] = [
#                 re.sub('\s+', ' ', list_item).strip() for list_item in item["job_apply_link"]]
#             item["job_apply_link"] = "https://www.glassdoor.com" + \
#                 item["job_apply_link"][0]
#         except (KeyError, TypeError):
#             item["job_apply_link"] = "NA"
#         ########################################################################
#         try:
#             item["job_apply_text"] = [
#                 re.sub('\t+', '', list_item).strip() for list_item in item["job_apply_text"]]
#             item["job_apply_text"] = [
#                 re.sub('\s+', ' ', list_item).strip() for list_item in item["job_apply_text"]]
#             item["job_apply_text"] = item["job_apply_text"][0]
#         except (KeyError, TypeError):
#             item["job_apply_text"] = "NA"
#         ###############
#         ###############
#         ###############
#         ###############
#         # item["company_website"] = [re.sub('\t+', '', list_item).strip() for list_item in item["company_website"]]
#         # item["company_website"] = [re.sub('\s+', ' ', list_item).strip() for list_item in item["company_website"]]
#         # item["company_website"] = item["company_website"][0]
#         try:
#             item["company_website"] = ''.join(item["company_website"])
#         except (KeyError, TypeError):
#             item["company_website"] = "NA"
#         ########################################################################
#         try:
#             item["company_size"] = [
#                 re.sub('\t+', '', list_item).strip() for list_item in item["company_size"]]
#             item["company_size"] = [
#                 re.sub('\s+', ' ', list_item).strip() for list_item in item["company_size"]]
#             item["company_size"] = item["company_size"][0]
#             item["company_size"] = re.search(
#                 '(to)*(.+?) employees', item["company_size"])
#             item["company_size"] = item["company_size"][2].replace(
#                 "+", "").split('to')[-1].strip()
#         except (KeyError, TypeError):
#             item["company_size"] = "NA"
#         ########################################################################
#         try:
#             item["company_type"] = [
#                 re.sub('\t+', '', list_item).strip() for list_item in item["company_type"]]
#             item["company_type"] = [
#                 re.sub('\s+', ' ', list_item).strip() for list_item in item["company_type"]]
#             item["company_type"] = item["company_type"][0].replace(
#                 "\n", "").strip()
#         except (KeyError, TypeError):
#             item["company_type"] = "NA"
#         ########################################################################
#         try:
#             item["company_revenue"] = [
#                 re.sub('\t+', '', list_item).strip() for list_item in item["company_revenue"]]
#             item["company_revenue"] = [
#                 re.sub('\s+', ' ', list_item).strip() for list_item in item["company_revenue"]]
#             item["company_revenue"] = item["company_revenue"][0]
#             item["company_revenue"] = item["company_revenue"].replace(
#                 "\n", "").strip()
#             item["company_revenue"] = item["company_revenue"].replace(
#                 "Unknown / Non-Applicable", "NA")
#
#             if type(re.search('(to)?(.+?) \(', item["company_revenue"])) is not type(None):
#                 item["company_revenue"] = re.search(
#                     '(to)?(.+?) \(', item["company_revenue"])
#                 item["company_revenue"] = item["company_revenue"][2].split(
#                     "to")[-1].strip()
#                 if type(re.search(' million', item["company_revenue"])) is not type(None):
#                     item["company_revenue"] = item["company_revenue"].replace(
#                         ' million', "000000")
#                 elif type(re.search(' billion', item["company_revenue"])) is not type(None):
#                     item["company_revenue"] = item["company_revenue"].replace(
#                         ' billion', "000000000")
#                 if type(re.search('$', item["company_revenue"])) is not type(None):
#                     item["company_revenue"] = item["company_revenue"].replace(
#                         '$', "")
#         except (KeyError, TypeError):
#             item["company_revenue"] = "NA"
#
#         ########################################################################
#         try:
#             item["company_headquarters"] = [re.sub(
#                 '\t+', '', list_item).strip() for list_item in item["company_headquarters"]]
#             item["company_headquarters"] = [re.sub(
#                 '\s+', ' ', list_item).strip() for list_item in item["company_headquarters"]]
#             item["company_headquarters"] = item["company_headquarters"][0]
#         except (KeyError, TypeError):
#             item["company_headquarters"] = "NA"
#         ########################################################################
#         try:
#             item["company_founded"] = [
#                 re.sub('\t+', '', list_item).strip() for list_item in item["company_founded"]]
#             item["company_founded"] = [
#                 re.sub('\s+', ' ', list_item).strip() for list_item in item["company_founded"]]
#             item["company_founded"] = item["company_founded"][0]
#             item["company_founded"] = item["company_founded"].replace(
#                 "\n", "").strip()
#         except (KeyError, TypeError):
#             item["company_founded"] = "NA"
#         ########################################################################
#         try:
#             item["company_industry"] = [
#                 re.sub('\t+', '', list_item).strip() for list_item in item["company_industry"]]
#             item["company_industry"] = [
#                 re.sub('\s+', ' ', list_item).strip() for list_item in item["company_industry"]]
#             item["company_industry"] = item["company_industry"][0]
#             item["company_industry"] = item["company_industry"].replace(
#                 "\n", "").strip()
#         except (KeyError, TypeError):
#             item["company_industry"] = "NA"
#         ########################################################################
#         try:
#             item["company_description"] = [re.sub(
#                 '\t+', '', list_item).strip() for list_item in item["company_description"]]
#             item["company_description"] = [re.sub(
#                 '\s+', ' ', list_item).strip() for list_item in item["company_description"]]
#             item["company_description"] = item["company_description"][0]
#         except (KeyError, TypeError):
#             item["company_description"] = "NA"
#         ###############
#         ###############
#         ###############
#         ###############
#         # item["rating_rating"] = [re.sub('\t+', '', list_item).strip() for list_item in item["rating_rating"]]
#         # item["rating_rating"] = [re.sub('\s+', ' ', list_item).strip() for list_item in item["rating_rating"]]
#         try:
#             item["rating_rating"] = item["rating_rating"][0]
#             item["rating_rating"] = item["rating_rating"].replace(
#                 "-1", "NA").strip()
#         except (KeyError, TypeError):
#             item["rating_rating"] = "NA"
#         ########################################################################
#         # item["rating_recommend"] = [re.sub('\t+', '', list_item).strip() for list_item in item["rating_recommend"]]
#         # item["rating_recommend"] = [re.sub('\s+', ' ', list_item).strip() for list_item in item["rating_recommend"]]
#         try:
#             item["rating_recommend"] = item["rating_recommend"][0]
#             item["rating_recommend"] = item["rating_recommend"].replace(
#                 "-1", "NA").strip()
#         except (KeyError, TypeError):
#             item["rating_recommend"] = "NA"
#         ########################################################################
#         # item["rating_approve"] = [re.sub('\t+', '', list_item).strip() for list_item in item["rating_approve"]]
#         # item["rating_approve"] = [re.sub('\s+', ' ', list_item).strip() for list_item in item["rating_approve"]]
#         try:
#             item["rating_approve"] = item["rating_approve"][0]
#             item["rating_approve"] = item["rating_approve"].replace(
#                 "-1", "NA").strip()
#         except (KeyError, TypeError):
#             item["rating_approve"] = "NA"
#
#         return item


class ProcessIndeed(object):
    def process_item(self, item, spider):

        # item["source"] = item["source"]
        item["source"] = "".join(item["source"])
        # item["url"] = item["url"]
        item["url"] = "".join(item["url"])

        try:
            item["job_company"] = [
                re.sub('\t+', '', list_item).strip() for list_item in item["job_company"]]
            item["job_company"] = [
                re.sub('\s+', ' ', list_item).strip() for list_item in item["job_company"]]
            item["job_company"] = "".join(item["job_company"])
        except (KeyError, TypeError):
            item["job_company"] = None


        try:
            item["job_position"] = [
                re.sub('\t+', '', list_item).strip() for list_item in item["job_position"]]
            item["job_position"] = [
                re.sub('\s+', ' ', list_item).strip() for list_item in item["job_position"]]
            item["job_position"] = "".join(item["job_position"])
        except (KeyError, TypeError):
            item["job_position"] = None


        try:
            item["job_text"] = [re.sub('\t+', '', list_item).strip()
                                for list_item in item["job_text"]]
            item["job_text"] = [re.sub('\s+', ' ', list_item).strip()
                                for list_item in item["job_text"]]
            item["job_text"] = "".join(item["job_text"])
        except (KeyError, TypeError):
            item["job_text"] = None


        try:
            item["location"] = [re.sub('\t+', '', list_item).strip()
                                for list_item in item["location"]]
            item["location"] = [re.sub('\s+', ' ', list_item).strip()
                                for list_item in item["location"]]
            item["location"] = "".join(item["location"])
        except (KeyError, TypeError):
            item["location"] = None



        item["country"] = "".join(item["country"])

        try:
            item["date_added"] = item["date_added"][0]
        except (KeyError, TypeError):
            raise DropItem("No date no job %s" % item["url"])

        item["date_scraped"] = item["date_scraped"][0]


        try:
            item["page_source_text"] = [re.sub('\t+', '', list_item).strip()
                                for list_item in item["page_source_text"]]
            item["page_source_text"] = [re.sub('\s+', ' ', list_item).strip()
                                for list_item in item["page_source_text"]]
            item["page_source_text"] = ". ".join(item["page_source_text"])
        except (KeyError, TypeError):
            item["page_source_text"] = None

        # item["page_source_html"] = "".join(item["page_source_html"])
        # item["page_source_html"] = str(item["page_source_html"])
        # try:
        #     item["page_source_html"] = "".join(item["page_source_html"])
        # except (KeyError, TypeError):
        #     item["page_source_html"] = None

        try:
            item["external_url"] = "".join(item["external_url"])
        except (KeyError, TypeError):
            item["external_url"] = None

        # item["page_source_html"] = "".join(item["page_source_html"])
        # try:
        #     item["page_external_source_html"] = "".join(item["page_external_source_html"])
        # except (KeyError, TypeError):
        #     item["page_external_source_html"] = None

        try:
            item["page_external_source_text"] = [re.sub('\t+', '', list_item).strip()
                                for list_item in item["page_external_source_text"]]
            item["page_external_source_text"] = [re.sub('\s+', ' ', list_item).strip()
                                for list_item in item["page_external_source_text"]]
            item["page_external_source_text"] = ". ".join(item["page_external_source_text"])
        except (KeyError, TypeError):
            item["page_external_source_text"] = None

        return item


class RecordJob(object):
    def process_item(self, item, spider):






        # first_query = session_job.query(Job_entry).filter(Job_entry.job_text == item["job_text"]).first()
        # second_query = session_job.query(Job_entry).\
        #                     filter(Job_entry.job_company == item["job_company"],
        #                             Job_entry.job_text == item["job_text"]).first()
        #
        # if (not first_query) and (not second_query):
        #
        #     session_job.add(Job_entry(**job_entry))
        #     try:
        #         session_job.commit()
        #     except:
        #         session_job.rollback()
        #     return item
        # else:
        #     raise DropItem("Article already exists %s" % item)



        ##### RECORDING JOB POSTING URL
        ########################################################################

        url_entry = {"url" : item["url"]}

        url_exists = session_test.query(exists().where(Url_entry.url==item["url"])).scalar()

        if not url_exists:
            adding_url = Url_entry(**url_entry)
            session_test.add(adding_url)
            session_test.commit()
            session_test.refresh(adding_url)
            url_id = adding_url.url_id
            # article_entry["source_id"] = url_id

            ##### RECORDING COMPANY
            ########################################################################

            if item["job_company"]:

                company_entry = {"company_name": item["job_company"]}
                company_exists = session_test.query(exists().where(Company_entry.company_name==item["job_company"])).scalar()

                if company_exists:
                    company_query = session_test.query(Company_entry).filter(Company_entry.company_name == item["job_company"]).one()
                    # source_result = inst_to_dict(source_query)
                    company_result = inst_to_dict(company_query)["company_id"]
                    company_id = company_result

                else:
                    adding_company = Company_entry(**company_entry)
                    session_test.add(adding_company)
                    session_test.commit()
                    session_test.refresh(adding_company)
                    company_id = adding_company.company_id
                    # external_url_entry["external_url_id"] = external_url_id
            else:
                raise DropItem("No company no job %s" % item["url"])


            ##### RECORDING JOB TITLE
            ########################################################################

            if item["job_position"]:

                title_entry = {"job_title": item["job_position"]}
                title_exists = session_test.query(exists().where(Title_entry.job_title==item["job_position"])).scalar()

                if title_exists:
                    title_query = session_test.query(Title_entry).filter(Title_entry.job_title == item["job_position"]).one()
                    # source_result = inst_to_dict(source_query)
                    title_result = inst_to_dict(title_query)["title_id"]
                    title_id = title_result

                else:
                    adding_title = Title_entry(**title_entry)
                    session_test.add(adding_title)
                    session_test.commit()
                    session_test.refresh(adding_title)
                    title_id = adding_title.title_id
                    # external_url_entry["external_url_id"] = external_url_id
            else:
                raise DropItem("No title no job %s" % item["url"])


            ##### RECORDING LOCATION
            ########################################################################

            if item["location"]:

                location_entry = {"location_name": item["location"]}
                location_exists = session_test.query(exists().where(Location_entry.location_name==item["location"])).scalar()

                if location_exists:
                    location_query = session_test.query(Location_entry).filter(Location_entry.location_name == item["location"]).one()
                    # source_result = inst_to_dict(source_query)
                    location_result = inst_to_dict(location_query)["location_id"]
                    location_id = location_result

                else:
                    adding_location = Location_entry(**location_entry)
                    session_test.add(adding_location)
                    session_test.commit()
                    session_test.refresh(adding_location)
                    location_id = adding_location.location_id
                    # external_url_entry["external_url_id"] = external_url_id
            else:
                raise DropItem("No location no job %s" % item["url"])


            ##### RECORDING COUNTRY
            ########################################################################

            if item["country"]:

                country_entry = {"country_name": item["country"]}
                country_exists = session_test.query(exists().where(Country_entry.country_name==item["country"])).scalar()

                if country_exists:
                    country_query = session_test.query(Country_entry).filter(Country_entry.country_name == item["country"]).one()
                    # source_result = inst_to_dict(source_query)
                    country_result = inst_to_dict(country_query)["country_id"]
                    country_id = country_result

                else:
                    adding_country = Country_entry(**country_entry)
                    session_test.add(adding_country)
                    session_test.commit()
                    session_test.refresh(adding_country)
                    country_id = adding_country.country_id
                    # external_url_entry["external_url_id"] = external_url_id
            else:
                raise DropItem("No country no job %s" % item["url"])

            ########################################################################
            ##### TESTING DUPLICATES
            ########################################################################

            jobs_exists = session_test.query(Job_entry).\
                                filter(Job_entry.company_id == company_id,
                                        Job_entry.title_id == title_id,
                                        Job_entry.location_id == location_id,
                                        Job_entry.country_id == country_id).scalar()

            if jobs_exists:

                most_recent_job_entry = session_test.query(Job_entry).\
                                    filter(Job_entry.company_id == company_id,
                                            Job_entry.title_id == title_id,
                                            Job_entry.location_id == location_id,
                                            Job_entry.country_id == country_id).order_by(desc(Job_entry.date_published)).first()



                days_since = (datetime.now(timezone('US/Eastern')) - most_recent_job_entry.date_published.replace(tzinfo = timezone('US/Eastern'))).days

                if days_since > 30:

                    ##### RECORDING EXTERNAL URL
                    ########################################################################

                    if item["external_url"]:

                        external_url_entry = {"external_url": item["external_url"]}
                        external_url_exists = session_test.query(exists().where(External_url_entry.external_url==item["external_url"])).scalar()

                        if external_url_exists:
                            external_url_query = session_test.query(External_url_entry).filter(External_url_entry.external_url == item["external_url"]).one()
                            # source_result = inst_to_dict(source_query)
                            external_url_result = inst_to_dict(external_url_query)["external_url_id"]
                            external_url_id = external_url_result

                        else:
                            adding_external_url = External_url_entry(**external_url_entry)
                            session_test.add(adding_external_url)
                            session_test.commit()
                            session_test.refresh(adding_external_url)
                            external_url_id = adding_external_url.external_url_id
                            # external_url_entry["external_url_id"] = external_url_id
                    else:
                        external_url_id = None



                    ##### RECORDING JOB DESCRIPTION
                    ########################################################################

                    if item["job_text"]:

                        job_description_entry = {"job_description": item["job_text"]}
                        # job_description_exists = session_test.query(exists().where(Job_description_entry.job_description==item["job_text"])).scalar()

                        # if job_description_exists:
                        #     job_description_query = session_test.query(Job_description_entry).filter(Job_description_entry.job_description == item["job_text"]).one()
                        #     # source_result = inst_to_dict(source_query)
                        #     job_description_result = inst_to_dict(job_description_query)["job_description_id"]
                        #     job_description_id = job_description_result
                        #
                        # else:
                        adding_job_description = Job_description_entry(**job_description_entry)
                        session_test.add(adding_job_description)
                        session_test.commit()
                        session_test.refresh(adding_job_description)
                        job_description_id = adding_job_description.job_description_id
                            # external_url_entry["external_url_id"] = external_url_id
                    else:
                        raise DropItem("No job description no job %s" % item["url"])




                    ##### RECORDING SOURCE
                    ########################################################################

                    if item["source"]:

                        source_entry = {"source_name": item["source"]}
                        source_exists = session_test.query(exists().where(Source_entry.source_name==item["source"])).scalar()

                        if source_exists:
                            source_query = session_test.query(Source_entry).filter(Source_entry.source_name == item["source"]).one()
                            # source_result = inst_to_dict(source_query)
                            source_result = inst_to_dict(source_query)["source_id"]
                            source_id = source_result

                        else:
                            adding_source = Source_entry(**source_entry)
                            session_test.add(adding_source)
                            session_test.commit()
                            session_test.refresh(adding_source)
                            source_id = adding_source.source_id
                            # external_url_entry["external_url_id"] = external_url_id
                    else:
                        raise DropItem("No source no job %s" % item["url"])


                    ##### RECORDING PAGE SOURCE
                    ########################################################################

                    if item["page_source_text"]:

                        page_source_entry = {
                                     # "page_source_html": item["page_source_html"],
                                     "page_source_text": item["page_source_text"]}

                        # page_source_exists = session_test.query(exists().where(Page_source_entry.page_source_text==item["page_source_text"])).scalar()
                        #
                        # if page_source_exists:
                        #     page_source_query = session_test.query(Page_source_entry).filter(Page_source_entry.page_source_text == item["page_source_text"]).one()
                        #     # source_result = inst_to_dict(source_query)
                        #     page_source_result = inst_to_dict(page_source_query)["page_source_id"]
                        #     page_source_id = page_source_result
                        #
                        # else:
                        adding_page_source = Page_source_entry(**page_source_entry)
                        session_test.add(adding_page_source)
                        session_test.commit()
                        session_test.refresh(adding_page_source)
                        page_source_id = adding_page_source.page_source_id
                            # external_url_entry["external_url_id"] = external_url_id
                    else:
                        raise DropItem("No page source no job %s" % item["url"])


                    ##### RECORDING EXTERNAL PAGE SOURCE
                    ########################################################################

                    if item["page_external_source_text"]:

                        page_external_source_entry = {
                                     # "page_external_source_html": item["page_external_source_html"],
                                     "page_external_source_text": item["page_external_source_text"]}

                        # page_external_source_exists = session_test.query(exists().where(Page_external_source_entry.page_external_source_text==item["page_external_source_text"])).scalar()
                        #
                        # if page_external_source_exists:
                        #     page_external_source_query = session_test.query(Page_external_source_entry).filter(Page_external_source_entry.page_external_source_text == item["page_external_source_text"]).one()
                        #     # source_result = inst_to_dict(source_query)
                        #     page_external_source_result = inst_to_dict(page_external_source_query)["page_external_source_id"]
                        #     page_external_source_id = page_external_source_result
                        #
                        # else:
                        adding_page_external_source = Page_external_source_entry(**page_external_source_entry)
                        session_test.add(adding_page_external_source)
                        session_test.commit()
                        session_test.refresh(adding_page_external_source)
                        page_external_source_id = adding_page_external_source.page_external_source_id
                            # external_url_entry["external_url_id"] = external_url_id
                    else:
                        page_external_source_id = None


                    job_entry = {
                                 "url_id": url_id,
                                 "external_url_id": external_url_id,
                                 "company_id": company_id,
                                 "title_id": title_id,
                                 "job_description_id": job_description_id,

                                 "location_id": location_id,
                                 "country_id": country_id,

                                 "date_published": item["date_added"],
                                 "date_scraped": item["date_scraped"],

                                 "source_id": source_id,

                                 "page_source_id": page_source_id,
                                 "page_external_source_id": page_external_source_id}


                    # jobs_exist = session_test.query(exists().where(
                    #         Job_entry.company_id == company_id &
                    #         Job_entry.title_id == title_id &
                    #         Job_entry.location_id == location_id &
                    #         Job_entry.country_id == country_id)).scalar()


                    session_test.add(Job_entry(**job_entry))
                    session_test.commit()
                else:
                    raise DropItem("Already seen this in the past 30 days %s" % item["url"])

            else:

                ##### RECORDING EXTERNAL URL
                ########################################################################

                if item["external_url"]:

                    external_url_entry = {"external_url": item["external_url"]}
                    external_url_exists = session_test.query(exists().where(External_url_entry.external_url==item["external_url"])).scalar()

                    if external_url_exists:
                        external_url_query = session_test.query(External_url_entry).filter(External_url_entry.external_url == item["external_url"]).one()
                        # source_result = inst_to_dict(source_query)
                        external_url_result = inst_to_dict(external_url_query)["external_url_id"]
                        external_url_id = external_url_result

                    else:
                        adding_external_url = External_url_entry(**external_url_entry)
                        session_test.add(adding_external_url)
                        session_test.commit()
                        session_test.refresh(adding_external_url)
                        external_url_id = adding_external_url.external_url_id
                        # external_url_entry["external_url_id"] = external_url_id
                else:
                    external_url_id = None



                ##### RECORDING JOB DESCRIPTION
                ########################################################################

                if item["job_text"]:

                    job_description_entry = {"job_description": item["job_text"]}
                    # job_description_exists = session_test.query(exists().where(Job_description_entry.job_description==item["job_text"])).scalar()

                    # if job_description_exists:
                    #     job_description_query = session_test.query(Job_description_entry).filter(Job_description_entry.job_description == item["job_text"]).one()
                    #     # source_result = inst_to_dict(source_query)
                    #     job_description_result = inst_to_dict(job_description_query)["job_description_id"]
                    #     job_description_id = job_description_result
                    #
                    # else:
                    adding_job_description = Job_description_entry(**job_description_entry)
                    session_test.add(adding_job_description)
                    session_test.commit()
                    session_test.refresh(adding_job_description)
                    job_description_id = adding_job_description.job_description_id
                        # external_url_entry["external_url_id"] = external_url_id
                else:
                    raise DropItem("No job description no job %s" % item["url"])




                ##### RECORDING SOURCE
                ########################################################################

                if item["source"]:

                    source_entry = {"source_name": item["source"]}
                    source_exists = session_test.query(exists().where(Source_entry.source_name==item["source"])).scalar()

                    if source_exists:
                        source_query = session_test.query(Source_entry).filter(Source_entry.source_name == item["source"]).one()
                        # source_result = inst_to_dict(source_query)
                        source_result = inst_to_dict(source_query)["source_id"]
                        source_id = source_result

                    else:
                        adding_source = Source_entry(**source_entry)
                        session_test.add(adding_source)
                        session_test.commit()
                        session_test.refresh(adding_source)
                        source_id = adding_source.source_id
                        # external_url_entry["external_url_id"] = external_url_id
                else:
                    raise DropItem("No source no job %s" % item["url"])


                ##### RECORDING PAGE SOURCE
                ########################################################################

                if item["page_source_text"]:

                    page_source_entry = {
                                 # "page_source_html": item["page_source_html"],
                                 "page_source_text": item["page_source_text"]}

                    # page_source_exists = session_test.query(exists().where(Page_source_entry.page_source_text==item["page_source_text"])).scalar()
                    #
                    # if page_source_exists:
                    #     page_source_query = session_test.query(Page_source_entry).filter(Page_source_entry.page_source_text == item["page_source_text"]).one()
                    #     # source_result = inst_to_dict(source_query)
                    #     page_source_result = inst_to_dict(page_source_query)["page_source_id"]
                    #     page_source_id = page_source_result
                    #
                    # else:
                    adding_page_source = Page_source_entry(**page_source_entry)
                    session_test.add(adding_page_source)
                    session_test.commit()
                    session_test.refresh(adding_page_source)
                    page_source_id = adding_page_source.page_source_id
                        # external_url_entry["external_url_id"] = external_url_id
                else:
                    raise DropItem("No page source no job %s" % item["url"])


                ##### RECORDING EXTERNAL PAGE SOURCE
                ########################################################################

                if item["page_external_source_text"]:

                    page_external_source_entry = {
                                 # "page_external_source_html": item["page_external_source_html"],
                                 "page_external_source_text": item["page_external_source_text"]}

                    # page_external_source_exists = session_test.query(exists().where(Page_external_source_entry.page_external_source_text==item["page_external_source_text"])).scalar()
                    #
                    # if page_external_source_exists:
                    #     page_external_source_query = session_test.query(Page_external_source_entry).filter(Page_external_source_entry.page_external_source_text == item["page_external_source_text"]).one()
                    #     # source_result = inst_to_dict(source_query)
                    #     page_external_source_result = inst_to_dict(page_external_source_query)["page_external_source_id"]
                    #     page_external_source_id = page_external_source_result
                    #
                    # else:
                    adding_page_external_source = Page_external_source_entry(**page_external_source_entry)
                    session_test.add(adding_page_external_source)
                    session_test.commit()
                    session_test.refresh(adding_page_external_source)
                    page_external_source_id = adding_page_external_source.page_external_source_id
                        # external_url_entry["external_url_id"] = external_url_id
                else:
                    page_external_source_id = None


                job_entry = {
                             "url_id": url_id,
                             "external_url_id": external_url_id,
                             "company_id": company_id,
                             "title_id": title_id,
                             "job_description_id": job_description_id,

                             "location_id": location_id,
                             "country_id": country_id,

                             "date_published": item["date_added"],
                             "date_scraped": item["date_scraped"],

                             "source_id": source_id,

                             "page_source_id": page_source_id,
                             "page_external_source_id": page_external_source_id}

                session_test.add(Job_entry(**job_entry))
                session_test.commit()
        #
        #
        #     article_entry = {"url_id" : url_id,
        #                     "article_text" : item["article_text"],
        #                     "article_title" : item["article_title"],
        #                     "author_id" : [],
        #                     "date_published" : item["date_published"],
        #                     "date_scraped" : item["date_scraped"],
        #                     # "source_spider" : item["source_spider"],
        #                     "source_id" : ""}
        #
        # # article_exists = session_test.query(exists().where(Article_entry.url==item["url"])).scalar()
        # # if not article_exists:
        # # list(set(t))
        #     for author in list(set(item["author_name"])):
        #         author_entry = {"author_name" : author}
        #         author_exists = session_test.query(exists().where(Author_entry.author_name==author)).scalar()
        #         if author_exists:
        #             author_query = session_test.query(Author_entry).filter(Author_entry.author_name == author).one()
        #             author_result = inst_to_dict(author_query)["author_id"]
        #             article_entry["author_id"].append(author_result)
        #         else:
        #             adding_author = Author_entry(**author_entry)
        #             session_test.add(adding_author)
        #             session_test.commit()
        #             session_test.refresh(adding_author)
        #             author_id = adding_author.author_id
        #             article_entry["author_id"].append(author_id)
        #
        #     source_entry = {"source_spider" : item["source_spider"],
        #                     "source_domain" : item["source_domain"]}
        #     source_exists = session_test.query(exists().where(Source_entry.source_spider==item["source_spider"])).scalar()
        #     if source_exists:
        #         source_query = session_test.query(Source_entry).filter(Source_entry.source_spider == item["source_spider"]).one()
        #         # source_result = inst_to_dict(source_query)
        #         source_result = inst_to_dict(source_query)["source_id"]
        #         article_entry["source_id"] = source_result
        #
        #     else:
        #         adding_source = Source_entry(**source_entry)
        #         session_test.add(adding_source)
        #         session_test.commit()
        #         session_test.refresh(adding_source)
        #         source_id = adding_source.source_id
        #         article_entry["source_id"] = source_id


            return item
        else:
            raise DropItem("Job already exists %s" % item["url"])
