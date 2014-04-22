import urllib
import AccountsClientPython.profiles as profiles

names_raw = urllib.urlopen('http://pastebin.com/raw.php?i=MQeZjhrp').read().split() # Random Fist of Names found on Pastebin
names = [] # Refined List of Names

for i in range(200): # we want 200 names in this example
  names.append(names_raw[i])

print profiles.find_profile_by_name('techkid6') # Get techkid6's profile
print profiles.find_profiles_by_names(names)    # Get the profiles of those in the list "names"
print profiles.find_profile_by_uuid('d560431ed516419580885b294f4f83f0') # Get the profile for this UUID
print profiles.find_profiles_by_uuids(['d560431ed516419580885b294f4f83f0', '2413639c21d64ba7a43ec90933f543e3']) # Get profiles for these UUID's
