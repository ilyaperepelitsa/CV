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

import pkg_resources
json_path = pkg_resources.resource_filename('credentials', 'passwords.json')

data = json.load(open(json_path))

dataslap_postgres = data["aws"]["personal"]["dataslap"]["postgres"]["free_20gb"]["dataslap_user"]

engine_test = create_engine('postgres://%(username)s:%(password)s@%(host)s:%(port)s/job_search_metrics' %
                            {"username": dataslap_postgres["username"],
                             "password": dataslap_postgres["password"],
                             "host": dataslap_postgres["host"],
                             "port": dataslap_postgres["port"]})
Base_item = declarative_base()


class Metric_entry(Base_item):
    __tablename__ = "metrics"
    scraper = Column(VARCHAR(50))
    spider = Column(VARCHAR(50))
    activity_type = Column(VARCHAR(50))
    table_name = Column(VARCHAR(50))
    entry_time = Column(TIMESTAMP)

    def __repr__(self):
        return "<Base_item(scraper='%s', spider='%s', activity_type='%s',\
                                    table_name='%s', entry_time='%s')>"\
            % (self.scraper, self.spider, self.activity_type, self.table_name,
                self.entry_time)



Base_item.metadata.create_all(engine_test)
Session_test = sessionmaker(bind=engine_test)
session_test = Session_test
