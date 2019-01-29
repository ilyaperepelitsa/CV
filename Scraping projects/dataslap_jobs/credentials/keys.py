import json
import os

root_path = os.path.dirname(os.path.abspath(__file__))
json_path = os.path.join(root_path, "passwords.json")
data = json.load(open(json_path))

def get_dataslap_postgres(user = "dataslap_user"):
    dataslap_postgres = data["aws"]["personal"]["dataslap"]["postgres"]["free_20gb"][user]
    return dataslap_postgres

# print(get_dataslap_postgres())
