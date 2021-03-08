# Imports

import re # Regular Expressions
import json

# Functions
def read_to_line_end(input_str, pos):
    pointer = pos
    c = input_str[pointer]

    while c != "\n":
        pointer += 1
        c = input_str[pointer]

    return input_str[pos:pointer], pointer

def find_data_by_identifier(json, identifier):
    for entry in json:
        if entry["id"] == identifier:
            return entry

def json_to_markdown(data):
    output_str = ""

    output_str += "## {}\n".format(data["title"])

    sut = []
    tlv = []
    for step in data["steps"]:
        sut.append(step["SUT"])
        tlv.append(step["TLV"])

    output_str += "<table>\n"
    output_str += "\t<tr>\n"
    output_str += "\t\t<th>System Under Test</th>\n"
    output_str += "\t\t<th>Lab Verification</th>\n"
    output_str += "\t</tr>\n"

    output_str += "\t<tr>\n"

    output_str += "\t\t<td>\n"
    output_str += "\t\t\t<ol>\n"

    for entry in sut:
        output_str += "\t\t\t\t<li>{}</li>\n".format(entry)
    
    output_str += "\t\t\t</ol>\n"
    output_str += "\t\t</td>\n"

    output_str += "\t\t<td>\n"
    output_str += "\t\t\t<ol>\n"

    for entry in tlv:
        output_str += "\t\t\t\t<li>{}</li>\n".format(entry)

    output_str += "\t\t\t</ol>\n"
    output_str += "\t\t</td>\n"

    output_str += "\t</tr>\n"
    output_str += "</table>\n"

    return output_str

# Main Code

choice = input("Press \"A\" to convert all .tpt files or enter a specific file name: ")

if choice == "A":
    # TODO: Loop through all tpt files and process accordingly
    print("Placeholder")
else:
    file_read = False

    tpt_template = None

    while not file_read:
        try:
            tpt_template = open(choice, 'r')
            file_read = True
            tpt_template_str = tpt_template.read()
        except FileNotFoundError:
            choice = input("File not found, enter a different file name: ")
            continue
        
    tpt_template_str = re.sub('<!--(.*?)-->', "", tpt_template_str) # Strip comments

    # Find $load()
    load_regex_str = "\$load\(.*.json\)"
    load_regex = re.compile(load_regex_str)
    load_command = load_regex.findall(tpt_template_str)[0]
    file_name = load_command[6:][:-1]

    tpt_template_str = tpt_template_str.replace(load_command, "")

    # Read in json from file
    json_tp_file = json.load(open(file_name, 'r'))[file_name[:-5]]

    json_search_function = "$tpJSON(id:"
    index = tpt_template_str.find(json_search_function)

    function_line, pos = read_to_line_end(tpt_template_str, index)

    id_regex = re.compile('"(.*?)"')
    identifier = id_regex.findall(function_line)[0]

    json_id_data = find_data_by_identifier(json_tp_file, identifier)

    tpt_template_str = tpt_template_str.replace(function_line, json_to_markdown(json_id_data))

    output_file = open("output.md", 'w')

    output_file.write(tpt_template_str)

    output_file.close()

    print("here")
