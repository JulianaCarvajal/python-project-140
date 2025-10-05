import prompt


def welcome_user() -> str:
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}!")
    return name


def check_answer(actual_answer: str, name: str) -> bool:
    user_answer = prompt.string("Your answer: ")

    if user_answer == actual_answer:
        print("Correct!")
        return True
    else:
        print(f"'{user_answer}' is wrong answer ;(."
              f"Correct answer was '{actual_answer}'.")
        print(f"Let's try again, {name}!")
        return False


def game(message: str, make_question, get_answer):
    name = welcome_user()
    print(message)

    for _ in range(3):
        question = make_question()
        print(f"Question: {question}")
        correct_answer = get_answer(question)
        if not check_answer(correct_answer, name):
            break
    else:
        print(f"Congratulations, {name}!")
