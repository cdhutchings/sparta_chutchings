from animal_class import Animal

# Define a reptile that inherits from Animal

class Reptile(Animal):

    def __init__(self, colour = ''):
        super().__init__(colour) # inherits the attributes from the parent class - this is not automatic.

        self.hearts = 4 # polymorphism in action. I can change attribute values from what they were set in the parent
                        # class


    def seek_heat(self):
        print("mmmmmm~ lotsa sun!")

    def hunt(self):
        print("wait for it~~   POUNCE!!")

    def eat(self, food = ''):
        print("mmmmmmm!", food)


