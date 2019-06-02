from initialisation import *

print("Receptionist can check-in a passenger")
before = len(tom.passenger_instances)
legolas = Passenger("Legolas", "Greenleaf", 7433001)
after = len(tom.passenger_instances)
print(before + 1 == after)
print("///////////////////")



print("Receptionist can assign a passenger to a flight")
prebook = len(mor_gon.passengers)
mor_gon.passengers.append(legolas)
postbook = len(mor_gon.passengers)
print(prebook + 1 == postbook)
print("///////////////////")


print("Receptionist can list all existing flights")

# I have been able to find a test that works, however this only functions when called on specific instances of each class.
# Because of my relative lack of knowledge with oop and class functions, this was the best test I could think of this
# weekend. I look forward to workingo on this test during the week.

#print(len(mor_gon.flight_instances))
#print(roh_gon.count)
print(len(mor_gon.flight_instances) == roh_gon.count)

