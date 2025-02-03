import requests
import os
from dotenv import load_dotenv



API_URL = 'https://api.api-ninjas.com/v1/animals'


def fetch_data(animal_name):
  """
  Fetches the animals data for the animal 'animal_name'.
  Returns: a list of animals, each animal is a dictionary:
  {
    'name': ...,
    'taxonomy': {
      ...
    },
    'locations': [
      ...
    ],
    'characteristics': {
      ...
    }
  },
  """
  param = {'name': animal_name}
  result = []
  response = requests.get(API_URL, headers=HEADER, params=param)
  if response.status_code == requests.codes.ok:
      result = response.json()
  else:
      print("Error:", response.status_code, response.text)
  return result


load_dotenv()
API_KEY = os.getenv('API_KEY')
HEADER = {'X-Api-Key': API_KEY}