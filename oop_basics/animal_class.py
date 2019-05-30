class Animal:

    def __init__(self, colour = ''):
        self.lungs = True
        self.eyes = True
        self.alive = True
        self.colour = colour

    def sleep(self):
        print("zzzzzz~~")

    def eat(self, food = ''):
        print("nomnomnomnom~~ That is some good", food)

    def breathe(self):
        print("INHALE... EXHALE...")

    def potty(self):
        print("O.O")

