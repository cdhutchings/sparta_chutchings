class Monster:

    def __init__(self, name = '', age = ''):
        self.name = name
        self.skills = ["scaring", "jumping"]
        self.age = age

    def sleep(self):
        return "zzzzz"

    def eat(self):
        return "nomnomnom"

    def scare(self):
        return "RAAAAGGGH!!!"

    def train(self, skill):
        self.skills.append(skill) # Return not necessary in this case since we are not expecting an output from the
                                    # function, just a change in the variable 'self'

