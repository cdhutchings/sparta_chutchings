# While loops
# Continuously iterates until a given condition is broken (becomes False)
# Can also be stopped by the Break cause (which can be placed in a control flow of an If clause

# Syntax ~ " while <condition>:
                # block of code

# while loop with count

age = 0

while age <= 18:
    print('Happy birthday!')
    print('here\'s some money')
    print('you are', age)
    age += 1

# while loop with break condition

age = 0

while True:
    print('Happy birthday!')
    print('here\'s some money')
    print('you are', age)
    age += 1
    if age > 18:
        break

# ^ Both of these loops doe exactly the same thing


