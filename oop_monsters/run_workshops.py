from workshops_class import *
from monster_class import *

# Create 1 workshop

work_shop1 = Workshop("Creating Chaos for Better Fear")

# Create 3 monsters

sully = Monster('Sully', 22, 9999)
mike = Monster('Mike', 24, 321)
omen = Monster('Omen', 666, 666)

# Append our monsters to our workshop

work_shop1.enroll(sully)
work_shop1.enroll(mike)
work_shop1.enroll(omen)

# We can now generate a list which displays the long and complex string the computer has given to each class instance

list_of_attendance = work_shop1.attendance

# To get the names out, you simply call the method as normal

for monster in list_of_attendance:
    print(monster.name)