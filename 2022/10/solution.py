import os, sys


def compute_cycles(operations: list[str]):
    cycle_vals = [1]
    value = 1
    for entry in operations:
        operation = entry.split(" ")
        if operation[0] == "addx":
            cycle_vals.append(value)
            value = value + int(operation[1])
            cycle_vals.append(value)
        else:
            cycle_vals.append(value)
    return cycle_vals


def run_solution_first(operations: list[str]):
    cycle_vals = compute_cycles(operations)
    cycles = [20, 60, 100, 140, 180, 220]
    total_strength = 0

    for cycle in cycles:
        total_strength = total_strength + cycle * cycle_vals[cycle - 1]

    return total_strength


def run_solution_second(operations: list[str]):
    width = 40
    height = 6
    cycle_vals = compute_cycles(operations)[: width * height]

    screen = ""
    for x_drawing, sprite_x in enumerate(cycle_vals):
        if sprite_x in range(
            (x_drawing % width) - 1, (x_drawing % width) + 2
        ):  # [-1,0,1]
            screen = screen + "#"
        else:
            screen = screen + "."
        if (x_drawing + 1) % width == 0:  # next pixel will be out of bounds
            screen = screen + "\n"
    return screen


if __name__ == "__main__":
    file = open(os.path.join(sys.path[0], "input.txt"), "r")
    file_contents = file.readlines()
    file.close()
    file_contents_stripped = [line.strip() for line in file_contents]

    solution_one = run_solution_first(file_contents_stripped)
    print(f"answer to part one: {solution_one}")

    solution_two = run_solution_second(file_contents_stripped)
    print(f"answer to part two:\n{solution_two}")
