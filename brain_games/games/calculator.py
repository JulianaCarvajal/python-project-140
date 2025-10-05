from random import choice, randint


def generate_expression() -> str:
    number1 = randint(1, 100)
    operators = ["+", "-", "*"]
    operator = choice(operators)
    number2 = randint(1, 100)

    return f"{number1} {operator} {number2}"


def evaluate_expression(expression: str) -> str:
    n1, operator, n2 = expression.split()
    number1, number2 = int(n1), int(n2)

    match operator:
        case "+":
            result = number1 + number2
        case "-":
            result = number1 - number2
        case "*":
            result = number1 * number2

    return str(result)
