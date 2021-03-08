# Imports

import re # Regular Expressions
import json
from enum import Enum

# Member Variables 
#TODO: Reorganize so these are not necessary
json_tp_file = None #TODO: Do we need to load in JSON files like this or can we just hard code it here?
output_file = open("output.md", 'w')

# Function Definitions

class Env(Enum):
    open = 1
    markdown = 2
    clarification = 3

def read_to_line_end(input_str, pos):
    pointer = pos
    c = input_str[pointer]

    while c != "\n":
        pointer += 1
        c = input_str[pointer]

    return input_str[pos:pointer], pointer

def process_open_line(line, output_file):
    # Two options in Open Env, either it is a load or markdown
    # TODO: Change from hard coded tpJSON name to variable name
    if re.match("tpJSON = load\(.*.json\)", line):
        file_path_regex = re.compile('\(([^\)]+)\)')
        file_name = file_path_regex.findall(line)[0]
        global json_tp_file
        json_tp_file = json.load(open(file_name, 'r'))
    elif re.match("tpJSON\(id: .*\)", line):
        id_regex = re.compile('"(.*?)"')
        identifier = id_regex.findall(line)[0]
        identifier_json = json_tp_file["g10-test-procedure"][0]
        json_to_markdown(identifier_json)
    else:
        print('here')

def json_to_markdown(json):
    sut = []
    tlv = []

    for step in json["steps"]:
        sut.append(step["SUT"])
        tlv.append(step["TLV"])

    output_file.write("## {}\n".format(json["section"]))
    output_file.write("<table>\n")
    output_file.write("\t<tr>\n")
    output_file.write("\t\t<th>System Under Test</th>\n")
    output_file.write("\t\t<th>Lab Verification</th>\n")
    output_file.write("\t</tr>\n")

    output_file.write("\t<tr>\n")

    output_file.write("\t\t<td>\n")
    output_file.write("\t\t\t<ol>\n")

    for entry in sut:
        output_file.write("\t\t\t\t<li>{}</li>\n".format(entry))
    
    output_file.write("\t\t\t</ol>\n")
    output_file.write("\t\t</td>\n")

    output_file.write("\t\t<td>\n")
    output_file.write("\t\t\t<ol>\n")

    for entry in tlv:
        output_file.write("\t\t\t\t<li>{}</li>\n".format(entry))

    output_file.write("\t\t\t</ol>\n")
    output_file.write("\t\t</td>\n")

    output_file.write("\t</tr>\n")

    output_file.write("</table>\n")

def process_markdown(input_str, pos):
    pointer = pos
    c = input_str[pointer]

    while c != '#':
        pointer += 1
        c = input_str[pointer]

    input_str, pointer = read_to_line_end(input_str, pointer)

    output_file.write(input_str + "\n")

    return input_str, pointer

def process_clarification(input_str, pos):
    pointer = pos
    c = input_str[pointer]

    while c != '#':
        pointer += 1
        c = input_str[pointer]

    input_str, pointer = read_to_line_end(input_str, pointer)

    output_file.write(input_str + "\n")

    return input_str, pointer

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
    
    current_env = Env.open # Start out on an open environment

    pointer = 0

    while pointer < len(tpt_template_str):
        c = tpt_template_str[pointer]

        if c != "\n":
            if current_env == Env.markdown:
                if c == '~':
                    pointer += 2
                    current_env = Env.open
                    continue
            elif current_env == Env.clarification:
                if c == '&':
                    pointer += 2
                    current_env = Env.open
                    continue
            if c == '-':
                current_env = Env.clarification
                _, pointer = process_clarification(tpt_template_str, pointer)

            if c != '/':
                line, pointer = read_to_line_end(tpt_template_str, pointer)
                process_open_line(line, output_file)
            else:
                current_env = Env.markdown
                _, pointer = process_markdown(tpt_template_str, pointer)
            
            continue

        pointer += 1

    output_file.close()