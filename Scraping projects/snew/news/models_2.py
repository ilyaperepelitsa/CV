# import news.models
from models import *
from sqlalchemy.sql import exists


session_test

# ret = session_test.query(exists().where(news.models.Article_entry.url=="google.com")).scalar()
ret = session_test.query(exists().where(Article_entry.url=="google.com")).scalar()

import dateutil.parser
from dateutil import tz
from_zone = tz.gettz('PST')
to_zone = tz.gettz('America/New_York')

yourdate = dateutil.parser.parse("2018-02-03 12:00:17")
yourdate

yourdate = yourdate.replace(tzinfo=from_zone)

yourdate.astimezone(to_zone)


yourdate.replace(tzinfo=from_zone)
dir(yourdate)
yourdate.tzinfo()
