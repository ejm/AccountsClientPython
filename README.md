AccountsClientPython
====================

A python version of Mojang's AccountsClient repository with some extra features, inspired by [Mojang/AccountsClient](https://github.com/Mojang/AccountsClient) and [Thezomg/mcapi](https://github.com/Thezomg/mcapi) 

Installation
------------

```
pip install git+git://github.com/techkid6/AccountsClientPython
```

Example
-------

```python
# This gets the UUID of a player
from AccountsClientPython.profiles import find_profiles_by_name

profiles = find_profiles_by_name('techkid6')
if profiles is not None and len(profiles) > 0:
    print profiles[0]['id']
```

License
-------
This project is a fork of [this project](https://github.com/Mojang/AccountsClient), which has no written license other than the fact that one may fork and convert to other languages as they please.  I am keeping with this license
