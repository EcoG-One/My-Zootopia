import json


def load_data(file_path):
  '''
  Loads a JSON file
  :param file_path: the path to the JSON file
  :return: the content of the JSON file as a list of dictionaries
  '''
  try:
      with open(file_path, "r") as handle:
        data = handle.read()
  except IOError as e:
      print(f'WARNING! {e}. Exiting...')
      exit()
  return json.loads(data)


def serialize_animal(animal_obj):
    '''
    Serializes an animal object and outputs it as HTML
    :param animal_obj: Dictionary with all the animal properties
    :return: the animal object as HTML
    '''
    output = '\n'
    output += '            <li class="cards__item">\n'
    try:
        output += (f'              <div class="card__title">'
                   f'{animal_obj["name"]}</div>\n')
    except (KeyError, IndexError):
        pass
    output += ('              <p class="card__text">\n                '
               '<ul style="list-style: square outside none">\n')
    try:
        output += (f'                  <li><strong>Diet:</strong> '
                   f'{animal_obj["characteristics"]["diet"]} </li>\n')
    except (KeyError, IndexError):
        pass
    try:
        output += (f'                  <li><strong>Location:</strong> '
                   f'{animal_obj["locations"][0]} </li>\n')
    except (KeyError, IndexError):
        pass
    try:
        output += (f'                  <li><strong>Type:</strong> '
                   f'{animal_obj["characteristics"]["type"]} </li>\n')
    except (KeyError, IndexError):
        pass
    output += '                </ul>\n              </p>\n            </li>\n'
    return output


def skin_type_list(animals_data):
    '''
    Creates a list of available animal skin types
    :param animals_data: List of Dictionaries with all the animals
        and their properties
    :return: a list of available animal skin types
    '''
    skin_list =[]
    for animal_data in animals_data:
        if animal_data["characteristics"]["skin_type"] not in skin_list:
            skin_list.append(animal_data["characteristics"]["skin_type"])
    return skin_list


def read_data(animals_data, skin_choice):
    '''
    Iterates through the animals
    :param animals_data: List of Dictionaries with all the animals and
        their properties
    :param skin_choice: Users choice of animal skin to generate the website
           only for the animals with the selected skin_choice
    :return: all selected animal data as HTML
    '''
    output = ''
    for animal_data in animals_data:
        if (skin_choice == "All"
                or skin_choice == animal_data["characteristics"]["skin_type"]):
            output += serialize_animal(animal_data)
    return output


def read_html():
    '''
    Reads the HTML template file
    :return: the HTML template as string
    '''
    try:
        with open("animals_template.html", "r") as html_template:
            return html_template.read()
    except IOError as e:
        print(f'WARNING! {e}. Exiting...')
        exit()


def main():
    '''
    Main function: Displays to the user a list of the available
        skin_type values from the JSON file and asks for the user to
        enter a skin_type from the displayed list, and then,
        based on the "animals_template.html", generates the webpage
        "animals.html" for the animals with the selected skin_type,
        or all if user chose all.
    :return: HTML page
    '''
    animals_data = load_data('animals_data.json')
    print("Available skin types are: ")
    for skin in skin_type_list(animals_data):
        print(skin)
    while True:
        choice = input("Please enter a skin type or "
                       "'All' for all skin types: ").capitalize()
        if choice == "'all'": #In case user inputs 'All' with quotation
            choice = "All"
        if choice in skin_type_list(animals_data) or choice == "All":
            break
        else:
            print("Wrong input.")
    new_html = read_html().replace("__REPLACE_ANIMALS_INFO__",
                                   read_data(animals_data, choice))
    try:
        with open("animals.html", "w") as new_html_file:
            new_html_file.write(new_html)
    except IOError as e:
        print(f'WARNING! {e}. Exiting...')
        exit()


if __name__ == "__main__":
    main()