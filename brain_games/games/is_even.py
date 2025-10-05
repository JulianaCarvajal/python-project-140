from random import randint


def is_even(number: float) -> str:
    if number % 2 == 0:
        return "yes"
    else:
        return "no"


def generate_number() -> int:
    number = randint(1, 100)
    return number
