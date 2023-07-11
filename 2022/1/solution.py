import os, sys


def run_solution(input: list[str]):
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


if __name__ == "__main__":
    file = open(os.path.join(sys.path[0], "input.txt"), "r")
    file_contents = file.readlines()
    file.close()
    solution = run_solution(file_contents)
    print(solution)
