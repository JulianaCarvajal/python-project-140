from brain_games import game, generate_number, is_even


def main():
    message = 'Answer "yes" if the number is even, otherwise anser "no".'
    question = generate_number
    get_answer = is_even
    game(message, question, get_answer)


if __name__ == "__main__":
    main()
