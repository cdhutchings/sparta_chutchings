# Required range is 1 to 100, so begin with a for loop for that range (101 not inclusive)

for x in range(1,101):

    # Start by setting both of my variables fizz and buzz to be False. This shall be reset on each iteration.
    # Fizz being True indicates a number is divisible by 3
    # Buzz being True indicates a number is divisible by 5

    fizz = False
    buzz = False

    # Performing modulo calculation for both 3 and 5 and the relevant bool variables

    if x % 3 == 0:
        fizz = True

    if x % 5 == 0:
        buzz = True

    # Finalize with a simple set of logical conditions to determine the output

    if fizz and buzz:
        output = "fizzbuzz"
    elif fizz and not buzz:
        output = "fizz"
    elif buzz and not fizz:
        output = "buzz"
    else:
        output = str(x)

    # Finish by printing the output

    print(output)

# Already I can see how this program can be made more extendable to include more phrases by use of a list of bools
# I'm sure I could design this with classes, but I feel this is already simple enough

# To be more in-keeping with the principles of Agile, I shall stop now with a working program rather than make things
# unnecessarily complicated so early on and run the risk of issues!
