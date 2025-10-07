from random import randint


def generate_progression() -> str:
    progression_length = randint(5, 10)
    start = randint(1, 100)
    step = randint(1, 10)
    end = start + progression_length * step

    missing_number_index = randint(0, progression_length - 1)

    progression_list = []

    for index, item in enumerate(range(start, end, step)):
        if index == missing_number_index:
            progression_list.append("..")
        else:
            progression_list.append(str(item))

    return " ".join(progression_list)


def get_missing_number(progression: str) -> str:
    progression_list = progression.split()
    missing_number_index = progression_list.index("..")
    if missing_number_index >= 2:
        step = int(progression_list[1]) - int(progression_list[0])
        missing_number = int(progression_list[missing_number_index - 1]) + step
    else:
        step = int(progression_list[-1]) - int(progression_list[-2])
        missing_number = int(progression_list[missing_number_index + 1]) - step

    return str(missing_number)
