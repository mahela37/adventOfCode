import os, sys


def run_solution_first(calories: list[str]):
    highest_calories = 0
    calories_current_elf = 0
    for line in calories:
        if line == "\n" or line == None:  # last entry for elf
            if calories_current_elf > highest_calories:
                highest_calories = calories_current_elf
            calories_current_elf = 0
        else:
            calories_current_elf = calories_current_elf + int(line)
    return highest_calories


def get_list_entry_default_zero(input: list[any], index: int):
    try:
        return input[index]
    except IndexError:
        return 0


def run_solution_second(calories: list[str]):
    calories_per_elf = []
    calories_current_elf = 0
    for line in calories:
        if line == "\n" or line == None:  # last entry for elf
            calories_per_elf.append(calories_current_elf)
            calories_current_elf = 0
        else:
            calories_current_elf = calories_current_elf + int(line)
    calories_per_elf.sort(reverse=True)
    return (
        get_list_entry_default_zero(calories_per_elf, 0)
        + get_list_entry_default_zero(calories_per_elf, 1)
        + get_list_entry_default_zero(calories_per_elf, 2)
    )


if __name__ == "__main__":
    file = open(os.path.join(sys.path[0], "input.txt"), "r")
    file_contents = file.readlines()
    file.close()

    solution_one = run_solution_first(file_contents)
    print(f"answer to part one: {solution_one}")

    solution_two = run_solution_second(file_contents)
    print(f"answer to part two: {solution_two}")
