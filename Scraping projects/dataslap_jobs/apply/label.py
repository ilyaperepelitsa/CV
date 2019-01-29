from dataslap_jobs.models import *
from apply.browser_tools import *
from pandas import read_sql_query
from pandas import read_sql
from random import shuffle

from datetime import datetime,tzinfo,timedelta
from pytz import timezone


# display_company_id = get_id(
#                 session = session_test,
#                 item = Location_entry,
#                 item_column = Location_entry.location_name,
#                 query_string = 'New York, NY',
#                 target_column_string = "location_id")
#
# display_company_id
#
#
#
# session_test.query(Location_entry.location_id).filter(Location_entry.location_id== 1
#
# driver = init_driver()
# open_a_job(driver, "https://github.com/hasura/skor")



def ask_apply():
    print("----------------------------------")
    answer_apply = input("Would you like to apply for this job? Type 'yes'/'no':")
    answer = False
    if answer_apply == "yes":
        answer = True
    elif answer_apply == "no":
        answer = False
    return answer

def ask_expired():
    print("----------------------------------")
    answer_expired = input("Is this job expired? Type 'yes'/'no':")
    answer = False
    if answer_expired == "yes":
        answer = True
    elif answer_expired == "no":
        answer = False
    return answer

def ask_skills():
    print("----------------------------------")
    existing_skills = [i.skill_label for i in session_test.query(Skill_focus_entry).all()]
    for skill in existing_skills:
        print(" --- '%s'" % skill)
    answer_skill = input("Please provide a skill name that works for this position:")
    if answer_skill in existing_skills:
        return answer_skill


#
# q = query(Job_entry, Location_entry.location_name).\
#     join(Location_entry)
#
# read_sql_query(q, engine_test)
#
# df = read_sql_query(session_test.query(Job_entry, Location_entry.location_name).\
#     join(Location_entry), engine_test)




# session_test.query(Skill_paragraph_entry.skill_paragraph_added).\
#         order_by(Skill_paragraph_entry.skill_paragraph_added.desc()).\
#         first()
#
# pew = session_test.query(Job_entry.source_id).\
#     filter(~Job_entry.job_id.in_(session_test.query(Job_label_entry.job_id)),
#             ~Job_entry.job_id.in_(session_test.query(Job_expired_entry.job_id))).\
#     all()
# len(pew)




# len(non_labeled_jobs)

interrupt = False
driver = init_driver()
# open_a_job(driver, "https://google.com")

# job = non_labeled_jobs.pop()
# job.display_job_title

while not interrupt:

    non_labeled_jobs = session_test.query(Job_entry.job_id,
                                          Job_entry.company_id,
                                          Job_entry.title_id,
                                          Url_entry.url,
                                          External_url_entry.external_url,
                                          Company_entry.company_name,
                                          Display_company_entry.display_company_name,
                                          Title_entry.job_title,
                                          Display_title_entry.display_job_title,
                                          Location_entry.location_name,
                                          Country_entry.country_name,
                                          Source_entry.source_name).\
        filter(~Job_entry.job_id.in_(session_test.query(Job_label_entry.job_id)),
                ~Job_entry.job_id.in_(session_test.query(Job_expired_entry.job_id))).\
        outerjoin(Url_entry, External_url_entry, Company_entry, Display_company_entry,
                  Title_entry, Display_title_entry, Location_entry, Country_entry,
                  Source_entry).\
        all()
    print(len(non_labeled_jobs))

    if len(non_labeled_jobs) > 0:
        shuffle(non_labeled_jobs)
        job = non_labeled_jobs.pop()
        if job.external_url:
            url = job.external_url
            print("This same job on Indeed.com: '%s'" % job.url)
        else:
            url = job.url
            # print(job.url)
        print(url)
        print(job.company_name)
        try:
            print(job.display_company_name)
        except AttributeError:
            pass
        print(job.job_title)
        try:
            print(job.display_job_title)
        except AttributeError:
            pass
        print(job.location_name)
        print(job.country_name)
        print(job.source_name)
        print("===================================")
        open_a_job(driver, url)
        if job.display_company_name is None:
            ask_company = input("Type a company name if you don't want to use this one '%s'. \
                                Hit enter (empty string) to leave as is" % job.company_name)
            if ask_company == "":
                set_display_company = job.company_name
            else:
                set_display_company = ask_company

            display_company_id = get_entry_id(
                            entry = {"display_company_name" : set_display_company},
                            session = session_test,
                            item = Display_company_entry,
                            item_column = Display_company_entry.display_company_name,
                            query_string = set_display_company,
                            target_column_string = "display_company_id")

            session_test.query(Job_entry).\
                filter(Job_entry.company_id == job.company_id).\
                update({"display_company_id": display_company_id})
            session_test.commit()

        if job.display_job_title is None:
            ask_title = input("Type the position name if you don't want to use this one '%s'. \
                                Hit enter (empty string) to leave as is" % job.job_title)
            if ask_title == "":
                set_display_title = job.job_title
            else:
                set_display_title = ask_title

            display_title_id = get_entry_id(
                            entry = {"display_job_title" : set_display_title},
                            session = session_test,
                            item = Display_title_entry,
                            item_column = Display_title_entry.display_job_title,
                            query_string = set_display_title,
                            target_column_string = "display_title_id")

            session_test.query(Job_entry).\
                filter(Job_entry.title_id == job.title_id).\
                update({"display_title_id": display_title_id})
            session_test.commit()

        is_expired = ask_expired()
        if is_expired:
            post_entry(entry = {"job_id" : job.job_id,
                                "expired_timestamp" : datetime.now(timezone('US/Eastern')),},
                            session = session_test,
                            item = Job_expired_entry,
                            item_column = Job_expired_entry.job_id,
                            query_string = job.job_id)
        else:
            do_apply = ask_apply()
            if do_apply:
                matching_skills = []
                while len(matching_skills) < 2:
                    matching_skill = ask_skills()
                    skill_add_id =  get_id(session = session_test,
                                        item = Skill_focus_entry,
                                        item_column = Skill_focus_entry.skill_label,
                                        query_string = matching_skill,
                                        target_column_string = "skill_id")
                    matching_skills.append(skill_add_id)
                post_entry(entry = {"job_id" : job.job_id,
                                    "apply_label" : True,
                                    "apply_timestamp" : datetime.now(timezone('US/Eastern')),
                                    "skill_focus" : matching_skills},
                                session = session_test,
                                item = Job_label_entry,
                                item_column = Job_label_entry.job_id,
                                query_string = job.job_id)

            else:
                post_entry(entry = {"job_id" : job.job_id,
                                    "apply_label" : False,
                                    "apply_timestamp" : datetime.now(timezone('US/Eastern'))},
                                session = session_test,
                                item = Job_label_entry,
                                item_column = Job_label_entry.job_id,
                                query_string = job.job_id)

        print("===================================")
        ask_interrupt = input(
            "If you'd like to stop labeling for now enter 'stop':")
        if ask_interrupt == "stop":
            interrupt = True



# delete_label(session = session_test,
#             item = Display_company_entry,
#             item_column = Display_company_entry.display_company_name,
#             query_string = "Sr. Data Analyst",
#             target_column_string = "display_company_id",
#             item2 = Job_entry,
#             item2_column = Job_entry.display_company_id,
#             target2_column_string = "display_company_id")
#

# delete_label(session = session_test,
#             item = Display_company_entry,
#             item_column = Display_company_entry.display_company_name,
#             query_string = "Financial Analyst",
#             target_column_string = "display_company_id",
#             item2 = Job_entry,
#             item2_column = Job_entry.display_company_id,
#             target2_column_string = "display_company_id")
#
# delete_label(session = session_test,
#             item = Display_company_entry,
#             item_column = Display_company_entry.display_company_name,
#             query_string = "Associate Scientist",
#             target_column_string = "display_company_id",
#             item2 = Job_entry,
#             item2_column = Job_entry.display_company_id,
#             target2_column_string = "display_company_id")


# delete_label(session = session_test,
#             item = Display_company_entry,
#             item_column = Display_company_entry.display_company_name,
#             query_string = "Scientific Technical Leader ",
#             target_column_string = "display_company_id",
#             item2 = Job_entry,
#             item2_column = Job_entry.display_company_id,
#             target2_column_string = "display_company_id")


# delete_label(session = session_test,
#             item = Display_company_entry,
#             item_column = Display_company_entry.display_company_name,
#             query_string = "Sr. Data Scientist",
#             target_column_string = "display_company_id",
#             item2 = Job_entry,
#             item2_column = Job_entry.display_company_id,
#             target2_column_string = "display_company_id")

# delete_label(session = session_test,
#             item = Display_title_entry,
#             item_column = Display_title_entry.display_job_title,
#             query_string = "Software Engineer,",
#             target_column_string = "display_title_id",
#             item2 = Job_entry,
#             item2_column = Job_entry.display_title_id,
#             target2_column_string = "display_title_id")

# delete_label(session = session_test,
#             item = Display_title_entry,
#             item_column = Display_title_entry.display_job_title,
#             query_string = "Software Engineer,",
#             target_column_string = "display_title_id",
#             item2 = Job_entry,
#             item2_column = Job_entry.display_title_id,
#             target2_column_string = "display_title_id")


# delete_label(session = session_test,
#             item = Display_company_entry,
#             item_column = Display_company_entry.display_company_name,
#             query_string = "Software Engineer",
#             target_column_string = "display_company_id",
#             item2 = Job_entry,
#             item2_column = Job_entry.display_company_id,
#             target2_column_string = "display_company_id")


# Software Engineer

# Sr. Data Scientist

# The Execu|Search Group


# session_test.query(Skill_paragraph_entry.skill_paragraph_added).\
#         order_by(Skill_paragraph_entry.skill_paragraph_added.desc()).\
#         first()
