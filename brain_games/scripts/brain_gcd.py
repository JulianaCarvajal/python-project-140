from brain_games import find_gcd, game, generate_numbers


def main():
    message = 'Find the greatest common divisor of given numbers.'
    question = generate_numbers
    get_answer = find_gcd
    game(message, question, get_answer)


if __name__ == "__main__":
    main()
