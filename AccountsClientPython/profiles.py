import requests
import json

PROFILES_PER_REQUEST = 100
AGENT = "minecraft"
API_URL = "https://api.mojang.com/profiles/minecraft"

def find_profiles_by_names(*names):
  headers = {'Content-type': 'application/json', 'Accept': 'application/json'}
  body = json.dumps(names)
  result = post(API_URL, body, headers)
  return result

def post(url, body, head):
  response = requests.post(url, data=body, headers=head)
  return response.json()

