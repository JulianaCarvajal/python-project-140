import prompt
from brain_games import check_answer, is_even, welcome_user
from random import randint


def main():
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise anser "no".')

    for _ in range(3):
        number = randint(1, 100)
        print(f"Question: {number}")
        guess = prompt.string("Your answer: ")
        correct_answer = is_even(number)
        if not check_answer(guess, correct_answer, name):
            break
    else:
        print(f"Congratulations, {name}!")


if __name__ == "__main__":
    main()
