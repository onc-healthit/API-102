# Imports
import os
import re
import requests
import json
import time
from pathlib import Path

call_api = True

def read_to_line_end(input_str, pos):
    """Builds a string from a position to the end of the line
    and returns the result.

    Parameters
    ----------
    input_str : str, required
        String containing template file contense (default is None)

    pos : int, required
        Integer represetning the position in the input_str we start
        reading at and continue to first new line.
    """
    pointer = pos
    c = input_str[pointer]

    while c != "\n":
        pointer += 1

        # End of file check
        if pointer >= len(input_str):
            break

        c = input_str[pointer]

    return input_str[pos:pointer]

def strip_html(data):
    # https://stackoverflow.com/a/3398894
    p = re.compile(r'<.*?>')
    return p.sub('', data).strip()

def html_list_to_markdown(input, tabbed = False):
    input = re.sub(r'<ul ?[^>]*>', '', input) # Removing opening '<ul>' tag

    input = input.replace("</ul>", "") # Removing closing '</ul>' tag

    input = input.replace("\t", "") # Removing tabs
    
    if tabbed:
        input = input.replace("<li>", "\t- ") # Replcaing <li> with '\t-' (markdwon list syntax + a tab)
    else:
        input = input.replace("<li>", "- ") # Replcaing <li> with '-' (markdwon list syntax)
    
    input = input.replace("</li>", "") # Removing </li> tags

    links = re.findall(r"<a[^>]*>[^<]+<\/a>", input) # Find all of the <a> (link) tags

    # Augment link tags so that they open in new tab
    for link in links:
        tabbed_link = link.replace("<a", "<a target = \"_blank\"")
        input = input.replace(link, tabbed_link)

    return input

def gather_data_from_web(criterion):
    web_data = {}

    base_url = "https://healthit.gov/test-method"

    entity_ids_json = None
    if call_api:
        entity_ids_json = requests.get("{}/{}?_format=json".format(base_url, criterion)).json()["field_clarification_table"]
    else:
        with open('cached_entities.json') as f:
            entity_ids_json = json.load(f)["field_clarification_table"]

    data_url = "https://healthit.gov/entity/paragraph"

    for entity_id in entity_ids_json:
        data_json = None
        if call_api:
            data_json = requests.get("{}/{}?_format=json".format(data_url, entity_id["target_id"])).json()
            time.sleep(2) # Buffer between API calls
        else:
            with open('cached_test_files/cached_response.json') as f:
                data_json = json.load(f)

        element = strip_html(data_json["field_standard_s_referenced"][0]["processed"])
        data = data_json["field_technical_explanations_and"][0]["processed"]

        web_data[element] = data

    return web_data

def process_template(onc_template_str, file_name):
    # Search for the criterion endpoint path
    criterion_endpoint_tag = "$criterion-endpoint{"
    criterion_endpoint_tag_index = onc_template_str.find(criterion_endpoint_tag)
    criterion_endpoint_tag = function_line = read_to_line_end(onc_template_str, criterion_endpoint_tag_index)
    criterion_endpoint = re.findall('"([^"]*)"', criterion_endpoint_tag)[0] # Extracting criterion endpoint value
    onc_template_str = onc_template_str.replace(criterion_endpoint_tag, "")

    web_data = None
    if call_api:
        api_check = input("Warning! Numerous API calls are about to be made, are you sure you want to proceed? ('y' for yes): ")
        if api_check.lower() == 'y':
            web_data = gather_data_from_web(criterion_endpoint)
        else:
            print("Exiting...")
            exit()
    else:
        with open('cached_test_files/web_data.json') as f:
            web_data = json.load(f)

    onc_template_str = re.sub('<!--(.*?)-->', "", onc_template_str) # Strip comments

    # Search for the first ref
    ref_tag = "$ref{"
    ref_tag_index = onc_template_str.find(ref_tag)

    # Will continue looping for each load function present in template
    while ref_tag_index > 0:
        function_line = read_to_line_end(onc_template_str, ref_tag_index)

        referenced_parameters = re.findall(r'\{(.*?)\}', function_line)[0].split(",") # Extracting parameters
        referenced_paragraph_key = re.findall('"([^"]*)"', referenced_parameters[0])[0] # Extracting paragraph key

        # Checking for tabbed parameter
        tabbed = False
        if len(referenced_parameters) > 1:
            parameter = referenced_parameters[1].strip()
            if parameter == "tabbed":
                tabbed = True

        referenced_paragraph_data = web_data[referenced_paragraph_key]

        clarifications_list = re.findall('<ul ?[^}]*>[^}]*<\/ul>', referenced_paragraph_data) # Extracting unordered list
        clarifications_list = clarifications_list[0]

        clarifications_list = html_list_to_markdown(clarifications_list, tabbed)

        onc_template_str = onc_template_str.replace(function_line, clarifications_list)
        ref_tag_index = onc_template_str.find(ref_tag) # Search for another ref function
    
    # Output final result to file
    path = str(Path(os.getcwd()).parent) # Using Path to move up one directory level
    output_file = open("{}\\docs\\{}".format(path, file_name), 'w', encoding='utf-8')
    onc_template_str = onc_template_str.strip() # Strip extra newlines and whitespace
    output_file.write(onc_template_str)
    output_file.close()

    print("Done processing {}. File exported to: {}".format(file_name, "{}\\docs\\{}".format(path, file_name)))

# Main Code
choice = input("Press \"A\" to convert all .md files or enter a specific file name: ")

if choice == "A":
    directory = os.getcwd()

    for subdir, dirs, files in os.walk(directory):
        for file in files:
            ext = os.path.splitext(file)[-1].lower()
            if ext == ".md":
                onc_template = open("{}\\{}".format(directory, file), 'r', encoding="utf8")
                onc_template_str = onc_template.read()  
                print("Processing {}...".format("{}\\{}".format(directory, file)))  
                process_template(onc_template_str, file)
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
     
    process_template(onc_template_str, choice)

print("All processing complete!")