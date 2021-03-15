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

    output_str += "<table>\n"
    output_str += "\t<tr>\n"
    output_str += "\t\t<th>System Under Test</th>\n"
    output_str += "\t</tr>\n"

    output_str += "\t<tr>\n"

    output_str += "\t\t<td>\n"
    output_str += "\t\t\t<ol>\n"

    for entry in data["table"]:
        output_str += "\t\t\t\t<u><b>{}</b></u>\n".format(entry["group"])

        for step in entry["steps"]:
            bulleted_list = ""

            if "bullets" in step:
                bulleted_list += "\t\t\t\t\t<ul>\n"

                for bullet in step["bullets"]:
                    bulleted_list += "\t\t\t\t\t\t<li>{}</li>\n".format(bullet)

                bulleted_list += "\t\t\t\t\t</ul>\n"
            
            if bulleted_list != "":
                output_str += "\t\t\t\t<li>{}\n{}\t\t\t\t</li>\n".format(step["SUT"], bulleted_list)
            else:
                output_str += "\t\t\t\t<li>{}</li>\n".format(step["SUT"])
    
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

    
    # Convert test procedure JSON data to HTML
    tp_as_markdown_dict = {}
    entry_ids = []

    for entry in json_tp_file:
        #tp_as_markdown_dict.append((entry["id"], json_to_markdown(entry)))
        tp_as_markdown_dict[entry["id"]] =  entry
        entry_ids.append(entry["id"])

    # Search for the first load function
    json_search_function = "$tpJSON(id:"
    index = tpt_template_str.find(json_search_function)

    # Will continue looping for each load function present in template
    while index > 0:
        function_line, pos = read_to_line_end(tpt_template_str, index)

        id_regex = re.compile('"(.*?)"')
        identifier = id_regex.findall(function_line)[0]

        json_id_data = find_data_by_identifier(json_tp_file, identifier)

        entry_index = entry_ids.index(identifier)

        unreferenced_prev_tps = ""
        if entry_index > 0:
            for i in range(entry_index):
                unreferenced_prev_tps += json_to_markdown(tp_as_markdown_dict[entry_ids[i]])

            unreferenced_prev_tps += "\n"
            entry_ids = entry_ids[(entry_index + 1):]

        tpt_template_str = tpt_template_str.replace(function_line, unreferenced_prev_tps + json_to_markdown(json_id_data))

        # tp_as_markdown_dict = list(filter(lambda x: x[0] != identifier, tp_as_markdown_dict)) # Remove what we just added from the markdown list

        index = tpt_template_str.find(json_search_function) # Search for another load function

    # Any remaining entries get tacked onto the end
    for entry in entry_ids:
        tpt_template_str += "\n" + json_to_markdown(find_data_by_identifier(json_tp_file, entry))

    # Output final result to file
    output_file = open("output.md", 'w')
    output_file.write(tpt_template_str)
    output_file.close()

    print("Done! Take a look at output.md")
