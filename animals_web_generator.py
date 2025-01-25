import json

def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)


def read_data():
    animals_data = load_data('animals_data.json')
    output = ''
    for i in range(len(animals_data)):
        try:
            output += "Name: " + animals_data[i]["name"] + "\n"
            output += "Diet:" + animals_data[i]["characteristics"]["diet"] + "\n"
            output += "Location:" + animals_data[i]["locations"][0] + "\n"
            output += "Type:" + animals_data[i]["characteristics"]["type"] + "\n"
        except (KeyError, IndexError):
            pass
    return output


def read_html():
    with open("animals_template.html", "r") as html_template:
        return html_template.read()


new_html = read_html().replace("__REPLACE_ANIMALS_INFO__", read_data())
with open("animals.html", "w") as new_html_file:
    new_html_file.write(new_html)