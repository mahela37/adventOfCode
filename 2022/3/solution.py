import os, sys


def get_char_priority(character: str):
    if character.isupper():
        return ord(character) - 38
    return ord(character) - 96


def run_solution_first(rucksacks: list[str]):
    sum_priorities = 0

    for rucksack in rucksacks:
        num_items_per_compartment = int(len(rucksack) / 2)
        first_compartment = set(rucksack[:num_items_per_compartment])
        second_compartment = set(rucksack[num_items_per_compartment:])
        common_items = first_compartment.intersection(second_compartment)

        for item in common_items:
            sum_priorities = sum_priorities + get_char_priority(item)

    return sum_priorities


def run_solution_second(rucksacks: list[str]):
    sum_priorities = 0
    i = 0

    while i < len(rucksacks):
        common_items = set(rucksacks[i])
        for j in range(1, 3):
            common_items = common_items.intersection(set(rucksacks[i + j]))

        for item in common_items:
            sum_priorities = sum_priorities + get_char_priority(item)

        i = i + 3  # go to next group of rucksacks
    return sum_priorities


if __name__ == "__main__":
    file = open(os.path.join(sys.path[0], "input.txt"), "r")
    file_contents = file.readlines()
    file.close()
    file_contents_stripped = [line.strip() for line in file_contents]

    solution_one = run_solution_first(file_contents_stripped)
    print(f"answer to part one: {solution_one}")

    solution_two = run_solution_second(file_contents_stripped)
    print(f"answer to part two: {solution_two}")
