from math import sqrt


def is_prime(number: int) -> str:
    if number <= 1:
        return "no"
    else:
        for i in range(2, int(sqrt(number)) + 1):
            if number % i == 0:
                return "no"
                break
        else:
            return "yes"
