import os, sys


def run_solution_first(input: list[str]):
    highest_calories = 0
    calories_per_elf = 0
    for line in input:
        if line == "\n" or line == None:
            if calories_per_elf > highest_calories:
                highest_calories = calories_per_elf
            calories_per_elf = 0
        else:
            calories_per_elf = calories_per_elf + int(line)
    return highest_calories


def get_list_entry_default_zero(input: list[any], index: int):
    try:
        return input[index]
    except IndexError:
        return 0


def run_solution_second(input: list[str]):
    elves = []
    calories_per_elf = 0
    for line in input:
        if line == "\n" or line == None:
            elves.append(calories_per_elf)
            calories_per_elf = 0
        else:
            calories_per_elf = calories_per_elf + int(line)
    elves.sort(reverse=True)
    return (
        get_list_entry_default_zero(elves, 0)
        + get_list_entry_default_zero(elves, 1)
        + get_list_entry_default_zero(elves, 2)
    )


if __name__ == "__main__":
    file = open(os.path.join(sys.path[0], "input.txt"), "r")
    file_contents = file.readlines()
    file.close()

    solution_one = run_solution_first(file_contents)
    print(f"answer to part one: {solution_one}")

    solution_two = run_solution_second(file_contents)
    print(f"answer to part two: {solution_two}")
