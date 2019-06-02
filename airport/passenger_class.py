class Passenger:

    # Initialisation function

    passenger_instances = []

    def __init__(self, fname, lname, passport):
        self.passenger_instances.append(self)
        self.fname = fname
        self.lname = lname
        self.passport = passport

    # Allows receptionist to check a passenger in
