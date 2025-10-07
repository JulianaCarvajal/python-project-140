from brain_games import game, generate_progression, get_missing_number


def main():
    MESSAGE = 'What number is missing in the progression?'
    QUESTION_FN = generate_progression
    GET_ANSWER_FN = get_missing_number
    game(MESSAGE, QUESTION_FN, GET_ANSWER_FN)


if __name__ == "__main__":
    main()
