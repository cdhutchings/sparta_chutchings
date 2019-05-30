# Functions

# Functions are integral to programming
# Functional programming might not include OOP.
# Functions are defined and then called. That is it!

#Defining a function

# Some best practices:
    # 1 function per function!
    # Each function should only have one job so that it is testable
    # Your functions should return and not print (unless it is really meant to print)
        # This is for reusability and testability

# Functions help us keep our code DRY.
    # DRY = Don't Repeat Yourself


# Syntax:

# def name(arg1, arg2, arg3 = 'optional'):
    # Indented block of code for the body of the function

# The function needs to be called to run the block of code
# Call a function using it's name and passing in paramaters

# A quick example:

def hello_person(first, last):
    return "Hello " + first + ' ' + last + "!"

print(hello_person("Charlie", "Hutchings"))