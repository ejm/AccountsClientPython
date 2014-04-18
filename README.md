AccountsClientPython
====================

A python version of Mojang's AccountsClient repository with some extra features, inspired by [Mojang/AccountsClient](https://github.com/Mojang/AccountsClient) and [Thezomg/mcapi](https://github.com/Thezomg/mcapi) 

Installation
------------

```
pip install git+git://github.com/techkid6/AccountsClientPython
```

Example Usage
-------------

```python
# This gets the UUID of a player by name
from AccountsClientPython.profiles import find_profiles_by_names

profiles = find_profiles_by_names('techkid6')
if profiles is not None and len(profiles) > 0:
    print profiles[0]['id']
```

```python
# This gets the name of a player by UUID
from AccountsClientPython.profiles import find_profiles_by_uuids

profiles = find_profiles_by_uuids('d560431ed516419580885b294f4f83f0')
if profiles is not None and len(profiles) > 0:
    print profiles[0]['name']
````

License
-------
This project is a fork of [this project](https://github.com/Mojang/AccountsClient), which has no written license other than the fact that one may fork and convert to other languages as they please.  I am keeping with this license
