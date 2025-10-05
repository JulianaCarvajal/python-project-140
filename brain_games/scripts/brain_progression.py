from brain_games import game, generate_progression, get_missing_number


def main():
    message = 'What number is missing in the progression?'
    question = generate_progression
    get_answer = get_missing_number
    game(message, question, get_answer)


if __name__ == "__main__":
    main()
