from itertools import count

class Flight:
    flight_instances = []
    count = count(1)

    def __init__(self):
        self.flight_instances.append(self)
        self.count = next(self.count)
        self.origin = ''
        self.destination = ''
        self.aircraft = ''
        self.passengers = []
        self.time = ''
        self.flight_number = ''

    def assign_aircraft(self, aircraft):
        self.aircraft = aircraft

    def assign_journey(self, origin, destination, flight_number):
        self.origin = origin
        self.destination = destination
        self.flight_number = flight_number

    def check_in(self, passenger):
        self.passengers.append(passenger)
