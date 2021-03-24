# Imports
import re # Regular Expressions
import json
import os

# Functions
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

def process_template(onc_template_str):
    onc_template_str = re.sub('<!--(.*?)-->', "", onc_template_str) # Strip comments

    # Find $load()
    load_regex_str = "\$load\(.*.json\)"
    load_regex = re.compile(load_regex_str)
    load_command = load_regex.findall(onc_template_str)[0]
    file_name = load_command[6:][:-1] # Extract file name

    onc_template_str = onc_template_str.replace(load_command, "") # Remove load command from output

    # Read in json from file
    json_tp_file = json.load(open(file_name, 'r'))[file_name[:-5]]
    
    # Convert test procedure JSON data to HTML
    tp_as_dict = {}
    entry_ids = []

    for entry in json_tp_file:
        tp_as_dict[entry["id"]] =  entry
        entry_ids.append(entry["id"])

    # Search for the first load function
    json_search_function = "$tpJSON(id:"
    index = onc_template_str.find(json_search_function)

    # Will continue looping for each load function present in template
    while index > 0:
        function_line, pos = read_to_line_end(onc_template_str, index)

        id_regex = re.compile('"(.*?)"')
        identifier = id_regex.findall(function_line)[0]

        json_id_data = find_data_by_identifier(json_tp_file, identifier)

        entry_index = entry_ids.index(identifier)

        unreferenced_prev_tps = ""
        if entry_index > 0:
            for i in range(entry_index):
                unreferenced_prev_tps += json_to_markdown(tp_as_dict[entry_ids[i]])

            unreferenced_prev_tps += "\n"
            entry_ids = entry_ids[(entry_index + 1):]

        onc_template_str = onc_template_str.replace(function_line, unreferenced_prev_tps + json_to_markdown(json_id_data))

        index = onc_template_str.find(json_search_function) # Search for another load function

    # Any remaining entries get tacked onto the end
    for entry in entry_ids:
        onc_template_str += "\n" + json_to_markdown(find_data_by_identifier(json_tp_file, entry))

    # Output final result to file
    output_file_name = file_name.replace(".json", ".md") # Use same file name just with markdown extension
    output_file = open(output_file_name, 'w')
    onc_template_str = onc_template_str.strip() # Strip extra newlines and whitespace
    output_file.write(onc_template_str)
    output_file.close()

    print("Done! Take a look at {}".format(output_file_name))

# Main Code
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