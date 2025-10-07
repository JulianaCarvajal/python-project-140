from brain_games import game, generate_number, is_prime


def main():
    MESSAGE = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    QUESTION_FN = generate_number
    GET_ANSWER_FN = is_prime
    game(MESSAGE, QUESTION_FN, GET_ANSWER_FN)


if __name__ == "__main__":
    main()
