from animal_class import *
from reptile_class import *

# Run examples here - separation of concerns

animal1 = Animal()

print(type(animal1))

# animal1.potty()

ringo = Reptile()

# ringo will inherit all behaviours of the parent class Animal, as well as all the behaviours of his own class Reptile
# Because animal1 is only a member of the parent class, reptile attributes will not be compatible

ringo.sleep()
ringo.hunt()

