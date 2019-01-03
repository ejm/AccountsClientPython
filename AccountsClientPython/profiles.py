import requests
import json

PROFILES_URL = "https://api.mojang.com/profiles/minecraft"
SESSIONS_URL = "https://sessionserver.mojang.com/session/minecraft/profile/{uuid}"
HISTORY_URL  = "https://api.mojang.com/user/profiles/{uuid}/names"

def find_profiles_by_names(names):
  result = []
  pages = [ names[i:i+100] for i in range(0, len(names), 100) ]
  for page in pages:
    headers = {'Content-type': 'application/json', 'Accept': 'application/json'}
    print(type(page))
    body = json.dumps(page)
    result += _post(PROFILES_URL, body, headers)
  return result
  
def find_profile_by_name(name):
  result = find_profiles_by_names([name])
  if not result:
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
  if not result:
    return None
  else:
    return result[0]

def find_history_by_name(name):
  return find_history_by_uuid(find_profile_by_name(name)['id'])

def find_history_by_uuid(uuid):
 return _get(HISTORY_URL.format(uuid=uuid))

def _post(url, body, head):
  response = requests.post(url, data=body, headers=head)
  return response.json()

def _get(url):
  response = requests.get(url)
  return response.json()
