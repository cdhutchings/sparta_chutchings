from fizzbuzz_class import *

for x in range(1,101):

    factors = []

    fizz = fizzbuzz(x, 3)
    factors.append(fizz)
    buzz = fizzbuzz(x, 5)
    factors.append(buzz)

