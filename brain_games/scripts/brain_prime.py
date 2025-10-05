from brain_games import game, generate_number, is_prime


def main():
    message = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    question = generate_number
    get_answer = is_prime
    game(message, question, get_answer)


if __name__ == "__main__":
    main()
