# Imports
import os
import re
import requests
import json

def strip_html(data):
    # https://stackoverflow.com/a/3398894
    p = re.compile(r'<.*?>')
    return p.sub('', data).strip()

def gather_data_from_web():
    web_data = {}

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

        element = strip_html(data_json["field_standard_s_referenced"][0]["processed"])
        data = data_json["field_technical_explanations_and"][0]["processed"]

        web_data[element] = data

    return web_data

def process_template(onc_template_str):
    onc_template_str = re.sub('<!--(.*?)-->', "", onc_template_str) # Strip comments
    return 1

# Main Code
#web_data = gather_data_from_web()
# Temp, read from file
web_data = None
with open('web_data.json') as f:
    web_data = json.load(f)

choice = input("Press \"A\" to convert all .onc files or enter a specific file name: ")

if choice == "A":
    root_dir = os.getcwd() # Get current working directory

    for subdir, dirs, files in os.walk(root_dir):
        for file in files:
            ext = os.path.splitext(file)[-1].lower()
            if ext == ".onc":
                onc_template = open(file, 'r')
                onc_template_str = onc_template.read()
                print("Processing {}...".format(file))    
                process_template(onc_template_str)
else:
    file_read = False

    # Attempt to read in file and re-prompt if not found
    while not file_read:
        try:
            onc_template = open(choice, 'r')
            file_read = True
            onc_template_str = onc_template.read()
            onc_template.close()
        except FileNotFoundError:
            choice = input("File not found, enter a different file name: ")
            continue
    
    print("Processing {}...".format(choice))    
    process_template(onc_template_str)

print("All processing complete!")