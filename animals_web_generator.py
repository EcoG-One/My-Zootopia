import json

def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)


def read_data():
    animals_data = load_data('animals_data.json')
    output = ''
    for i in range(len(animals_data)):
        output += '<li class="cards__item">' + "\n"
        try:
            output += '<div class="card__title">'+ animals_data[i]["name"] + "</div>\n"
        except (KeyError, IndexError):
            pass
        output += '<p class="card__text">'
        try:
            output += '<strong>Diet:</strong> ' + animals_data[i]["characteristics"]["diet"] + "<br/>\n"
        except (KeyError, IndexError):
            pass
        try:
            output += '<strong>Location:</strong> ' + animals_data[i]["locations"][0] + "<br/>\n"
        except (KeyError, IndexError):
            pass
        try:
            output += '<strong>Type:</strong> ' + animals_data[i]["characteristics"]["type"] + "<br/>\n"
        except (KeyError, IndexError):
            pass
        output += '</p>\n</li>' + "\n"
    return output


def read_html():
    with open("animals_template.html", "r") as html_template:
        return html_template.read()


new_html = read_html().replace("__REPLACE_ANIMALS_INFO__", read_data())
with open("animals.html", "w") as new_html_file:
    new_html_file.write(new_html)