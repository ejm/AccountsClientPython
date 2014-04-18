import requests
import json

PROFILES_URL = "https://api.mojang.com/profiles/minecraft"
SESSIONS_URL = "https://sessionserver.mojang.com/session/minecraft/profile/{uuid}"

def find_profiles_by_names(*names):
  headers = {'Content-type': 'application/json', 'Accept': 'application/json'}
  body = json.dumps(names)
  result = post(PROFILES_URL, body, headers)
  return result

def find_profiles_by_uuids(*uuids):
  profiles = []
  for uuid in uuids:
    profiles.append(get(SESSIONS_URL.format(uuid=uuid)))
  return profiles

def post(url, body, head):
  response = requests.post(url, data=body, headers=head)
  return response.json()

def get(url):
  response = requests.get(url)
  return response.json()
