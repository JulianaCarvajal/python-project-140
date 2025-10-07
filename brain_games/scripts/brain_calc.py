from brain_games import evaluate_expression, game, generate_expression


def main():
    MESSAGE = 'What is the result of the expression?'
    QUESTION_FN = generate_expression
    GET_ANSWER_FN = evaluate_expression
    game(MESSAGE, QUESTION_FN, GET_ANSWER_FN)


if __name__ == "__main__":
    main()
