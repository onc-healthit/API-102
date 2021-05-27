import requests
import json
import re

def strip_html(data):
    # https://stackoverflow.com/a/3398894
    p = re.compile(r'<.*?>')
    return p.sub('', data).strip()

base_url = "https://healthit.gov/test-method"
criterion = "standardized-api-patient-and-population-services"

# entity_ids_json = requests.get("{}/{}?_format=json".format(base_url, criterion)).json()["field_clarification_table"]
# Reading cached file (temporary)
entity_ids_json = None
with open('cached_entities.json') as f:
  entity_ids_json = json.load(f)["field_clarification_table"]

data_url = "https://healthit.gov/entity/paragraph"

ccg_json = {criterion : []}

paragraph_identifier = 1

for entity_id in entity_ids_json:
    #data_json = requests.get("{}/{}?_format=json".format(data_url, entity_id["target_id"])).json()
    # Reading cached file (temporary)
    data_json = None
    with open('cached_response.json') as f:
        data_json = json.load(f)

    print(strip_html(data_json["field_standard_s_referenced"][0]["processed"]))
    #print((data_json["field_standard_s_referenced"][0]["processed"]))

    break

#print(entity_ids_json)