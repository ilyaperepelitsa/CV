import json
import os

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Enum, ForeignKey
from sqlalchemy.dialects.postgresql import TEXT, VARCHAR, INTEGER
from sqlalchemy.dialects.postgresql import TIMESTAMP, ARRAY
from sqlalchemy import Boolean
from sqlalchemy import desc

from sqlalchemy.sql import select
from sqlalchemy.sql import exists

# import keys
import pkg_resources
json_path = pkg_resources.resource_filename('credentials', 'passwords.json')

# root_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# json_path = os.path.join(root_path, "credentials/passwords.json")

data = json.load(open(json_path))


def inst_to_dict(inst, delete_id=True):
    dat = {}
    for column in inst.__table__.columns:
        dat[column.name] = getattr(inst, column.name)
    # if delete_id:
    #     dat.pop("num")
    return dat

def get_entry_id(entry, session, item, item_column,
                    query_string, target_column_string):
    entry_exists = session.query(exists().where(
        item_column == query_string)).scalar()

    if not entry_exists:
        adding_item = item(**entry)
        session.add(adding_item)
        session.commit()

    item_query = session.query(item).filter(
        item_column == query_string).one()
    query_result = inst_to_dict(item_query)[target_column_string]
    entry_id = query_result

    return entry_id

def post_entry(entry, session, item, item_column, query_string):
    entry_exists = session.query(exists().where(
        item_column == query_string)).scalar()

    if not entry_exists:
        adding_item = item(**entry)
        session.add(adding_item)
        session.commit()
    else:
        pass


def get_id(session, item, item_column,
                query_string, target_column_string):
    entry_exists = session.query(exists().where(
        item_column == query_string)).scalar()

    if entry_exists:
        item_query = session.query(item).filter(
            item_column == query_string).one()
        query_result = inst_to_dict(item_query)[target_column_string]
        return query_result
    else:
        ask_again = input("The '%s' didn't work, try again. Type 'stop' to stop." % query_string)
        return get_id(session, item, item_column,
                        ask_again, target_column_string, error_string)

def delete_label(session, item, item_column,
                query_string, target_column_string,
                item2, item2_column, target2_column_string):
    label_exists = session.query(exists().where(
        item_column == query_string)).scalar()

    if label_exists:
        item_query = session.query(item).filter(
            item_column == query_string).one()
        query_result = inst_to_dict(item_query)[target_column_string]

    session.query(item2).\
        filter(item2_column == query_result).\
        update({target2_column_string: None})
    session.commit()

    session.query(item).filter(item_column == query_string).delete()
    session.commit()


# json.loads(s)


dataslap_postgres = data["aws"]["personal"]["dataslap"]["postgres"]["free_20gb"]["dataslap_user"]
# dataslap_postgres = keys.get_dataslap_postgres()


engine_test = create_engine('postgres://%(username)s:%(password)s@%(host)s:%(port)s/job_search' %
                            {"username": dataslap_postgres["username"],
                             "password": dataslap_postgres["password"],
                             "host": dataslap_postgres["host"],
                             "port": dataslap_postgres["port"]})
Base_item = declarative_base()


class Url_entry(Base_item):
    __tablename__ = "urls"
    url_id = Column(INTEGER, primary_key=True)
    url = Column(TEXT, unique=True)

    def __repr__(self):
        return "<Base_item(url_id='%s', url='%s')>"\
            % (self.url_id, self.url)
        # return {"url_id" : self.url_id, "url" : self.url}


class External_url_entry(Base_item):
    __tablename__ = "external_urls"
    external_url_id = Column(INTEGER, primary_key=True)
    external_url = Column(TEXT, unique=True)

    def __repr__(self):
        return "<Base_item(external_url_id='%s', external_url='%s')>"\
            % (self.external_url_id, self.external_url)
        # return {"external_url_id" : self.external_url_id, "external_url" : self.external_url}


class Company_entry(Base_item):
    __tablename__ = "companies"
    company_id = Column(INTEGER, primary_key=True)
    company_name = Column(TEXT, unique=True)

    def __repr__(self):
        return "<Base_item(company_id='%s', company_name='%s')>"\
            % (self.company_id, self.company_name)
        # return {"company_id" : self.company_id, "company_name" : self.company_name}

class Display_company_entry(Base_item):
    __tablename__ = "display_companies"
    display_company_id = Column(INTEGER, primary_key=True)
    display_company_name = Column(TEXT, unique=True)

    def __repr__(self):
        return "<Base_item(display_company_id='%s', display_company_name='%s')>"\
            % (self.display_company_id, self.display_company_name)
        # return {"display_company_id" : self.display_company_id, "display_company_name" : self.display_company_name}


class Title_entry(Base_item):
    __tablename__ = "titles"
    title_id = Column(INTEGER, primary_key=True)
    job_title = Column(TEXT, unique=True)

    def __repr__(self):
        return "<Base_item(title_id='%s', job_title='%s')>"\
            % (self.title_id, self.job_title)
        # return {"title_id" : self.title_id, "job_title" : self.job_title}

class Display_title_entry(Base_item):
    __tablename__ = "display_titles"
    display_title_id = Column(INTEGER, primary_key=True)
    display_job_title = Column(TEXT, unique=True)

    def __repr__(self):
        return "<Base_item(display_title_id='%s', display_job_title='%s')>"\
            % (self.display_title_id, self.display_job_title)
        # return {"display_title_id" : self.display_title_id, "display_job_title" : self.display_job_title}

class Job_description_entry(Base_item):
    __tablename__ = "job_descriptions"
    job_description_id = Column(INTEGER, primary_key=True)
    job_description = Column(TEXT, nullable=False)

    def __repr__(self):
        return "<Base_item(job_description_id='%s', job_description='%s')>"\
            % (self.job_description_id, self.job_description)
        # return {"job_description_id" : self.job_description_id, "job_description" : self.job_description}

class Job_entry(Base_item):
    __tablename__ = "jobs"
    job_id = Column(INTEGER, primary_key=True)
    url_id = Column(INTEGER, ForeignKey("urls.url_id"), nullable=False)
    external_url_id = Column(INTEGER, ForeignKey(
        "external_urls.external_url_id"), nullable=True)
    company_id = Column(INTEGER, ForeignKey(
        "companies.company_id"), nullable=False)
    display_company_id = Column(INTEGER, ForeignKey(
        "display_companies.display_company_id"), nullable=True)
    title_id = Column(INTEGER, ForeignKey(
        "titles.title_id"), nullable=False)
    display_title_id = Column(INTEGER, ForeignKey(
        "display_titles.display_title_id"), nullable=True)
    job_description_id = Column(INTEGER, ForeignKey(
        "job_descriptions.job_description_id"), nullable=False)
    location_id = Column(INTEGER, ForeignKey(
        "locations.location_id"), nullable=False)
    country_id = Column(INTEGER, ForeignKey(
        "countries.country_id"), nullable=False)
    date_published = Column(TIMESTAMP, nullable=False)
    # '2016-06-22 19:10:25-07'
    date_scraped = Column(TIMESTAMP, nullable=False)
    source_id = Column(INTEGER, ForeignKey(
        "sources.source_id"), nullable=False)
    page_source_id = Column(INTEGER, ForeignKey(
        "page_sources.page_source_id"), nullable=False)
    page_external_source_id = Column(INTEGER, ForeignKey(
        "page_external_sources.page_external_source_id"), nullable=True)

    def __repr__(self):
        return "<Base_item(job_id='%s', url_id='%s', external_url_id='%s', company_id='%s',\
title_id='%s', job_description_id='%s', location_id='%s',\
country_id='%s', date_published='%s', date_scraped='%s',\
source_id='%s', page_source_id='%s',\
page_external_source_id='%s')>"\
        % (self.job_id, self.url_id, self.external_url_id, self.company_id, self.title_id, self.job_description_id,
            self.location_id, self.country_id, self.date_published, self.date_scraped,
            self.source_id, self.page_source_id, self.page_external_source_id)
        # return {"job_id" : self.job_id, "url_id" : self.url_id,
        #             "external_url_id" : self.external_url_id, "company_id" : self.company_id,
        #             "title_id" : self.title_id, "job_description_id" : self.job_description_id,
        #             "location_id" : self.location_id, "country_id" : self.country_id,
        #             "date_published" : self.date_published, "date_scraped" : self.date_scraped,
        #             "source_id" : self.source_id, "page_source_id" : self.page_source_id,
        #             "page_external_source_id" : self.page_external_source_id}

class Location_entry(Base_item):
    __tablename__ = "locations"
    location_id = Column(INTEGER, primary_key=True)
    location_name = Column(VARCHAR(50), unique=True)

    def __repr__(self):
        return "<Base_item(location_id='%s', location_name='%s')>"\
            % (self.location_id, self.location_name)
        # return {"location_id" : self.location_id, "location_name" : self.location_name}

class Country_entry(Base_item):
    __tablename__ = "countries"
    country_id = Column(INTEGER, primary_key=True)
    country_name = Column(VARCHAR(50), unique=True)

    def __repr__(self):
        return "<Base_item(country_id='%s', country_name='%s')>"\
            % (self.country_id, self.country_name)
        # return {"country_id" : self.country_id, "country_name" : self.country_name}

class Source_entry(Base_item):
    __tablename__ = "sources"
    source_id = Column(INTEGER, primary_key=True)
    source_name = Column(VARCHAR(20), unique=True)

    def __repr__(self):
        return "<Base_item(source_id='%s', source_name='%s')>"\
            % (self.source_id, self.source_name)
        # return {"source_id" : self.source_id, "source_name" : self.source_name}

class Page_source_entry(Base_item):
    __tablename__ = "page_sources"
    page_source_id = Column(INTEGER, primary_key=True)
    # page_source_html = Column(TEXT, nullable=False)
    page_source_text = Column(TEXT, nullable=False)

    def __repr__(self):
        return "<Base_item(page_source_id='%s',\
page_source_text='%s')>"\
        % (self.page_source_id,
            # self.page_source_html,
            self.page_source_text)
        # return {"page_source_id" : self.page_source_id, "page_source_text" : self.page_source_text}
        # return "<Base_item(page_source_id='%s',\
        #                     page_source_html='%s',\
        #                     page_source_text='%s')>"\


class Page_external_source_entry(Base_item):
    __tablename__ = "page_external_sources"
    page_external_source_id = Column(INTEGER, primary_key=True)
    # page_external_source_html = Column(TEXT, nullable=False)
    page_external_source_text = Column(TEXT, nullable=False)

    def __repr__(self):
        return "<Base_item(page_external_source_id='%s',\
page_external_source_text='%s')>"\
        % (self.page_external_source_id,
            # self.page_external_source_html,
           self.page_external_source_text)
        # return {"page_external_source_id" : self.page_external_source_id,
        #         "page_external_source_text" : self.page_external_source_text}
        # return "<Base_item(page_external_source_id='%s',\
        #                     page_external_source_html='%s',\
        #                     page_external_source_text='%s')>"\


class Job_label_entry(Base_item):
    __tablename__ = "labeled_jobs"
    label_id = Column(INTEGER, primary_key=True)
    job_id = Column(INTEGER, ForeignKey("jobs.job_id"), nullable=False)
    apply_label = Column(Boolean)
    apply_timestamp = Column(TIMESTAMP)
    skill_focus = Column(ARRAY(INTEGER, dimensions=1), nullable=True)

    def __repr__(self):
        return "<Base_item(label_id='%s', job_id='%s',\
apply_label='%s', apply_timestamp='%s',\
skill_focus='%s')>"\
        % (self.label_id, self.job_id, self.apply_label, self.apply_timestamp, self.skill_focus)
        # return {"label_id" : self.label_id, "job_id" : self.job_id,
        #             "apply_label" : self.apply_label, "apply_timestamp" : self.apply_timestamp,
        #             "skill_focus" : self.skill_focus}

class Job_apply_entry(Base_item):
    __tablename__ = "applied_jobs"
    applied_id = Column(INTEGER, primary_key=True)
    job_id = Column(INTEGER, ForeignKey("jobs.job_id"), nullable=False)
    applied_timestamp = Column(TIMESTAMP)

    def __repr__(self):
        return "<Base_item(applied_id='%s', job_id='%s',\
applied_timestamp='%s')>"\
        % (self.applied_id, self.job_id, self.applied_timestamp)

class Job_expired_entry(Base_item):
    __tablename__ = "expired_jobs"
    expired_id = Column(INTEGER, primary_key=True)
    job_id = Column(INTEGER, ForeignKey("jobs.job_id"), nullable=False)
    expired_timestamp = Column(TIMESTAMP)

    def __repr__(self):
        return "<Base_item(expired_id='%s', job_id='%s',\
expired_timestamp='%s')>"\
        % (self.expired_id, self.job_id, self.expired_timestamp)

        # return {"applied_id" : self.applied_id, "job_id" : self.job_id,
        #         "applied_timestamp" : self.applied_timestamp}

class Skill_focus_entry(Base_item):
    __tablename__ = "skill_focuses"
    skill_id = Column(INTEGER, primary_key=True)
    skill_label = Column(VARCHAR(20), nullable=False, unique=True)

    def __repr__(self):
        return "<Base_item(skill_id='%s', skill_label='%s')>"\
            % (self.skill_id, self.skill_label)
        # return {"skill_id" : self.skill_id, "skill_label" : self.skill_label}

class Skill_paragraph_entry(Base_item):
    __tablename__ = "skill_paragraphs"
    paragraph_id = Column(INTEGER, primary_key=True)
    skill_id = Column(INTEGER, ForeignKey(
        "skill_focuses.skill_id"), nullable=False)
    skill_paragraph_text = Column(TEXT, nullable=False)
    skill_paragraph_added = Column(TIMESTAMP)

    def __repr__(self):
        return "<Base_item(paragraph_id='%s', skill_id='%s', skill_paragraph_text='%s',\
skill_paragraph_added='%s')>"\
        % (self.paragraph_id, self.skill_id, self.skill_paragraph_text, self.skill_paragraph_added)
        # return {"paragraph_id" : self.paragraph_id, "skill_label" : self.skill_label,
        #             "skill_paragraph_text" : self.skill_paragraph_text, "skill_paragraph_added" : self.skill_paragraph_added}
