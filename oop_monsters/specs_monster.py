# Writing tests for my monster class

# ### Story
#
# - AS A user I should be able to create a monster from `class Monster`

from monster_class import *

name = "Sulley"
age = 3000

monster_example = Monster(name, age)
#
# ### Attributes of a monster
#
# - name (str)
# - skills (list)
#
# ### Methods of a monster
#
# Each behaviour should have a name and a defined response
#
print("sleep -> respond back with 'zzzzz'")

print(monster_example.sleep() == "zzzzz")

print("/////////////")

print("eat -> 'nomnomnom''")

print(monster_example.eat() == "nomnomnom")

print("/////////////")

print("scare -> 'RAAAAGGGH!!!'")

print(monster_example.scare() == "RAAAAGGGH!!!")

print("/////////////")

print("Is skills a list type?")

print(type(monster_example.skills) == list)

print("/////////////")

print("train -> Adds a skill to list of skills")

before = len(monster_example.skills)
monster_example.train("stealth")
after = len(monster_example.skills)

print(before + 1 == after)

print("___________")

# Attributes

print("Is 'name' a string?")
print(type(monster_example.name) == str)

print("/////////////")

print("Is the specified name the same as the name I choose for the monster?")
print(monster_example.name == name)

print("/////////////")

print("Is age an integer?")
print(type(monster_example.age) == int)

print("/////////////")

print("Is the age the same as the one I give?")
print(monster_example.age == age)

