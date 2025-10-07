from brain_games import find_gcd, game, generate_numbers


def main():
    MESSAGE = 'Find the greatest common divisor of given numbers.'
    QUESTION_FN = generate_numbers
    GET_ANSWER_FN = find_gcd
    game(MESSAGE, QUESTION_FN, GET_ANSWER_FN)


if __name__ == "__main__":
    main()
