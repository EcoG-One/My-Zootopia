import requests

HEADER = {'X-Api-Key': 'G9QyJcWfkTyDv5FL9jdR6Q==pRFfUbsYWJ4ldFmm'}
PARAM = {'name': animal_name}
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
  result = []
  response = requests.get(API_URL, headers=HEADER, params=PARAM)
  if response.status_code == requests.codes.ok:
      result = response.json()
  else:
      print("Error:", response.status_code, response.text)
  return result