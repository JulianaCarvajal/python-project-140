def is_even(number: float) -> str:
    if number % 2 == 0:
        return "yes"
    else:
        return "no"


def check_answer(user_answer: str, actual_answer: str, name: str) -> bool:
    if user_answer == actual_answer:
        print("Correct!")
        return True
    else:
        incorrect_answer_message = f"'{user_answer}' is wrong answer ;(.\
                                     Correct answer was '{actual_answer}'."
        print(incorrect_answer_message)
        print(f"Let's try again, {name}!")
        return False
