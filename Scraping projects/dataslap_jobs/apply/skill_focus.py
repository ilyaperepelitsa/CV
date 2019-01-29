from dataslap_jobs.models import *
# from sqlalchemy import Column


init_skill_focuses = ["gis", "scraping", "data_science", "database",
                    "machine_learning", "finance", "python",
                    "data_visualization"]

for skill_focus in init_skill_focuses:
    post_entry(entry = {"skill_label" : skill_focus},
                    session = session_test,
                    item = Skill_focus_entry,
                    item_column = Skill_focus_entry.skill_label,
                    query_string = skill_focus)
# session_test.rollback()
