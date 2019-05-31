def fizzbuzz(number, factor):

    if number % factor == 0:
        return True
    else:
        return False


def output(number, dict):

    factors = []

    for part in dict:
        outcome = fizzbuzz(number, dict[part])

        if outcome:
            factors.append(part)

    factors = ''.join(factors)

    if factors == '':
        return str(number)
    else:
        return factors


