from math import gcd
from random import randint


def generate_numbers() -> str:
    number1 = randint(1, 100)
    number2 = randint(1, 100)

    return f"{number1} {number2}"


def find_gcd(numbers: str) -> str:
    number1, number2 = numbers.split()
    result = gcd(int(number1), int(number2))

    return str(result)
