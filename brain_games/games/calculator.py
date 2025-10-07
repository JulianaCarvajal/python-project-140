from random import choice, randint


def generate_expression() -> str:
    first_number = randint(1, 100)
    operators = ["+", "-", "*"]
    operator = choice(operators)
    second_number = randint(1, 100)

    return f"{first_number} {operator} {second_number}"


def evaluate_expression(expression: str) -> str:
    n1, operator, n2 = expression.split()
    first_number, second_number = int(n1), int(n2)

    match operator:
        case "+":
            result = first_number + second_number
        case "-":
            result = first_number - second_number
        case "*":
            result = first_number * second_number

    return str(result)
