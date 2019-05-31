def fizzbuzz(number, factor):

    # fizzbuzz returns whether a number is divisible by a factor

    if number % factor == 0:
        return True
    else:
        return False

# output takes a number and dictionary of phrases and divisors and outputs a fizzbuzz game up to the specified number
# and follows the rules of the dictionary

def output(number, dict):

    # Create an empty list which will eventually contain the answer

    final = []

    # Loops across the required range

    for x in range(1,number+1):

        # creates empty list of which will contain the phrases 'fizz', 'buzz' etc.

        factors = []

        # Performes the fizzbuzz function for each element of the dictionary

        for part in dict:
            outcome = fizzbuzz(x, dict[part])

            # If the the number is divisible by the divisor, then outcome will be true and shall append the relevant
            # part of the dictionary to the factors list

            if outcome:
                factors.append(part)

        # After checking all possible entries to the dictionary, join the factors list together to make a long
        # string. This also does the job of keeping the phrases in the correct order.

        factors = ''.join(factors)

        # Finalise by calculating the output - the number if "factors" is empty, and the concatenated phrase if not.

        if factors == '':
            final.append(str(x))
        else:
            final.append(factors)

    return final
