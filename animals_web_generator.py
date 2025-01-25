import json

def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)


animals_data = load_data('animals_data.json')
for i in range(len(animals_data)):
    try:
        print("Name:", animals_data[i]["name"])
        print("Diet:", animals_data[i]["characteristics"]["diet"])
        print("Location:", animals_data[i]["locations"][0])
        print("Type:", animals_data[i]["characteristics"]["type"])
    except (KeyError, IndexError):
        pass