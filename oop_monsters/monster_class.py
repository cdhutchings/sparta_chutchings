class Monster:

    def __init__(self, name = '', age = ''):
        self.name = name
        self.skills = []
        self.age = age

    def sleep(self):
        return "zzzzz"

    def eat(self):
        return "nomnomnom"

    def scare(self):
        return "RAAAAGGGH!!!"

    def train(self, skill):
        return self.skills.append(skill)

