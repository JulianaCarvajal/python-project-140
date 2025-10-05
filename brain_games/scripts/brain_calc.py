from brain_games import evaluate_expression, game, generate_expression


def main():
    message = 'What is the result of the expression?'
    question = generate_expression
    get_answer = evaluate_expression
    game(message, question, get_answer)


if __name__ == "__main__":
    main()
