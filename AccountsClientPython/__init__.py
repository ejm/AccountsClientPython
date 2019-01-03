from .profiles import *
#relative import is needed as sys.path might not have this directory in it albeit it has site-package

def by_name(name):
  return find_profile_by_name(name)

def by_uuid(uuid):
  return find_profile_by_uuid(uuid)

def name_history(name):
  return find_history_by_name(name)

def uuid_history(uuid):
  return find_history_by_uuid(uuid)
  
def by_names(name):
  return find_profiles_by_names(name)
  
def by_uuids(uuid):
  return find_profiles_by_uuids(uuid)
  