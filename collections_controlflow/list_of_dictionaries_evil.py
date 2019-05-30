# Practicing creating a list of dictionaries

list_evil_people = []

cruella_vil = {
    'name': 'Cruella de Vil',
    'occupation': 'Evil puppy killer',
    'address': 'Disney World',
    'door_number': 10,
    'skills': ['Fashion', 'Laughing', 'Being Evil']
}

list_evil_people.append(cruella_vil)

fairy_godmother = {
    'name': 'The Fairy Godmother',
    'occupation': 'Jealous Mother',
    'address': 'Far Far Away',
    'door_number': 18,
    'skills': ['Spells', 'Singing', 'Being Evil']
}

list_evil_people.append(fairy_godmother)

moriarty = {
    'name': 'Moriarty',
    'occupation': 'Napoleon of Crime',
    'address': 'Butcher Street',
    'door_number': 221,
    'skills': ['Envy', 'BASE Jumping', 'Being Evil']
}

list_evil_people.append(moriarty)

master = {
    'name': 'The Master',
    'occupation': 'Rogue Time Lord',
    'address': 'Gallifrey',
    'door_number': -5,
    'skills': ['Time Travel', 'Face Changing', 'Being Evil']
}

list_evil_people.append(master)

print(list_evil_people)
print(len(list_evil_people))

# Accessing Moriarty

print(list_evil_people[2])

# Accessing Moriarty's address

print(list_evil_people[2]['address'])

# Loops in dictionary

for hash in list_evil_people:
    print('\n')
    for embed in hash:
        print(str(embed) + ':', str(hash[embed]))



