from brain_games import game, generate_number, is_even


def main():
    MESSAGE = 'Answer "yes" if the number is even, otherwise anser "no".'
    QUESTION_FN = generate_number
    GET_ANSWER_FN = is_even
    game(MESSAGE, QUESTION_FN, GET_ANSWER_FN)


if __name__ == "__main__":
    main()
