# Dictionaries

# Have a key-value pairs
# DO NOT USE AN INDEX
# Use Keys, which can be looked up to get values
# Keys must be unique
# Can also be called "hashes" or "objects" (in Java)
# Assigned using curly brackets {}

# Defining a dictionary
# Structure {'key': 'value'}
# Key can be anything as long as it's unique. Value can be anything too

cruella_vil = {
    'name': 'Cruella de Vil',
    'occupation': 'Evil puppy killer',
    'address': 'Disney World',
    'door_number': 10,
    'skills': ['Fashion', 'Laughing', 'Being Evil'],
    10: 'hello'
}

print(cruella_vil)
print(type(cruella_vil))

# Entries can be access just like a list, however the key must be used in place of the index

print(cruella_vil['name'])
print(type(cruella_vil['name']))

# Editing values are also very similar to lists

cruella_vil[10] = 'goodbye'
print(cruella_vil)

# Manipulating a list value using append

cruella_vil['skills'].append('Business Skills')
print(cruella_vil['skills'])

# Adding a new key:value
# Act as if you are editing: if the key you use does not exist, then it will create it

cruella_vil['favourite_colours'] = 'black and white'
print(cruella_vil)

# Two useful methods for dictionaries

# 1. Listing all the keys of a dictionary

keys = cruella_vil.keys()
print(keys)

# 2. Listing all values

values = cruella_vil.values()
print(values)