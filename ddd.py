import requests
from pprint import pprint as print

API_URL = 'https://jsonplaceholder.typicode.com/users/1'
response = requests.get(API_URL)
parsed_data = response.json()

print(parsed_data['name'])