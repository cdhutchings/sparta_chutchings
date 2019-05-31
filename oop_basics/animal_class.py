class Animal:

    # Underscores at beginning and end indicate special method. __init__ runs whenever you create an object of this
    # class

    def __init__(self, colour = ''):
        self.lungs = True
        self.eyes = True
        self.alive = True
        self.colour = colour
        self.age_days = 0
        self.hearts = 1

    def __ageing(self): # double underscore makes a method private (encapsulating). This function is only allowed to
        # be called in the class file, but not in any other file
        self.age_days += 1

    def sleep(self):
        print("zzzzzz~~")
        self.__ageing()

    def eat(self, food = ''):
        print("nomnomnomnom~~ That is some good", food)

    def breathe(self):
        print("INHALE... EXHALE...")

    def potty(self):
        print("O.O")

