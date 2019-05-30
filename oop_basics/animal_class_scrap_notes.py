# A class is a blueprint of an object
import time
class Animal:
    # Define how it looks (__init__ method) and behaves(its methods)

    origin = 'I am an animal from the animal kingdom (on Earth)'

    # Appearance:

    def __init__(self, species, colour = '', loc = ''):
        self.species = species
        self.alive = True
        self.colour = colour
        self.location = loc
        self.eyes = True
        self.lungs = True


    # Behaviour:

    def sleep(self):
        print("sleepy~ zzz...")

    def breathe(self):
        print("INHALE... EXHALE...")

    def eat(self, food = ''):
        print("nomnomnomnom!", food)

    def potty(self):
        print("O.O")

    def what_are_you(self):
        print(self.origin)

    # In each of these methods, "self" refers to the instance of the class Animal, NOT the class itself.

