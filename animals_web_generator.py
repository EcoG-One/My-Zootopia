import data_fetcher


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
                   f'{animal_obj["characteristics"]["group"]} </li>\n')
    except (KeyError, IndexError):
        pass
    output += '                </ul>\n              </p>\n            </li>\n'
    return output


def read_data(animals_data):
    '''
    Iterates through the objects of animals_data list, adding them
        to the HTML using the serialize_animal() function
    :param animals_data: List of Dictionaries with all the animals and
        their properties
    :return: all selected animal data as HTML
    '''
    output = ''
    for animal_data in animals_data:
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
    Main function: asks the user to enter an animal family,
    and then, pools data from "https://api-ninjas.com/api/animals"
    and based on the "animals_template.html" generates the webpage
    "animals.html" for the animals family entered by the user.
    :return: HTML page
    '''
    choice = input("Enter a name of an animal: ").capitalize()
    animals_data  = data_fetcher.fetch_data(choice)
    if not animals_data:
        new_html = read_html().replace("__REPLACE_ANIMALS_INFO__",
                  f"<li>\n                "
                f"<h2 align='center'>The animal {choice} doesn't exist."
                f"</h2>\n            </li>")
        print(f"The animal {choice} doesn't exist.")
    else:
        new_html = read_html().replace("__REPLACE_ANIMALS_INFO__",
                                   read_data(animals_data))
    try:
        with open("animals.html", "w") as new_html_file:
            new_html_file.write(new_html)
        print("Website was successfully generated to the file animals.html.")
    except IOError as e:
        print(f'WARNING! {e}. Exiting...')
        exit()


if __name__ == "__main__":
    main()