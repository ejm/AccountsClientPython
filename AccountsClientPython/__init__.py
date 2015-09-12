import profiles

def by_name(name):
  profiles.find_profile_by_name(name)

def by_uuid(uuid):
  profiles.find_profile_by_uuid(uuid)

def name_history(name):
  profiles.find_history_by_name(name)

def uuid_history(uuid):
  profiles.find_history_by_uuid(uuid)
