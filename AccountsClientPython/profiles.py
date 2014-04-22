import requests
import json

PROFILES_URL = "https://api.mojang.com/profiles/minecraft"
SESSIONS_URL = "https://sessionserver.mojang.com/session/minecraft/profile/{uuid}"

def find_profiles_by_names(names):
  result = []
  pages = [ names[i:i+100] for i in range(0, len(names), 100) ]
  for page in pages:
    headers = {'Content-type': 'application/json', 'Accept': 'application/json'}
    body = json.dumps(page)
    result += _post(PROFILES_URL, body, headers)
  return result
  
def find_profile_by_name(name):
  result = find_profiles_by_names([name])
  if result[0] is None:
    return None
  else:
    return result[0]

def find_profiles_by_uuids(uuids):
  profiles = []
  for uuid in uuids:
    profiles.append(_get(SESSIONS_URL.format(uuid=uuid)))
  return profiles
  
def find_profile_by_uuid(uuid):
  result = find_profiles_by_uuids([uuid])
  if result[0] is None:
    return None
  else:
    return result[0]

def _post(url, body, head):
  response = requests.post(url, data=body, headers=head)
  return response.json()

def _get(url):
  response = requests.get(url)
  return response.json()
