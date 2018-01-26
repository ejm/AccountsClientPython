import profiles

def by_name(name):
  return profiles.find_profile_by_name(name)

def by_uuid(uuid):
  return profiles.find_profile_by_uuid(uuid)

def name_history(name):
  return profiles.find_history_by_name(name)

def uuid_history(uuid):
  return profiles.find_history_by_uuid(uuid)
