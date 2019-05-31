# We want to create workshops of specific scary skills
# The workshop should have a list to keep Monster objects that are attending

class Workshop:

    def __init__(self, topic, location = 'Hell'):
        self.attendance = []
        self.teacher = ''
        self.location = location
        self.topic = topic

    def set_teacher(self, name):
        self.teacher = name

    # ^ This method is a "setter" as it sets a current variable
    # A method with a return clause is called a "getter"

    def enroll(self, name):
         self.attendance.append(name)
        #     print("[ROBOTIC VOICE] YOUR STUDENT HAS BEEN ENROLLED")
        # else:
        #     print("[ROBOTIC VOICE] ERROR! STUDENT HAS NOT BEEN ENROLLED!")