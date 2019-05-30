# Imports my functions from bot_brain as well as the required package "time"

from bot_brain import  *
import time

# Begins with basic greeting and asks for the user's name. This name then has any whitespace stripped and is capitalized.

print(generic_hello())

name = input(name_ask()).strip().title()

# Introduces a basic boolean variable to determine whether my loop should continue

on = True

while on: # Remember: "on" is a boolean already, so I do not need to make a logical statement here

    # Makes a one second gap so it actually feels like the bot is doing some kind of calculation!

    time.sleep(1)

    # Asks the user for a query

    query = input(what_want(name)).strip().lower()

    # basic if, elif, else function which runs through various trigger phrases the bot should recognise.
    # If the shutdown command is given, the on variable becomes False so the loop is broken

    if "?" in query:
        print(answer())
    elif query == 'sleep, you are broken':
        print(sleep())
        on = False
    else:
        print(response())



