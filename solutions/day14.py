import os
from input_loader import load_input_str

input_str = load_input_str(os.path.basename(__file__)[:-3])

example = """O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#...."""


def calc_load(state):
    load = 0
    for i, line in enumerate(state):
        load += (len(state) - i) * list(line).count("O")

    return load


def rotate(state):
    return tuple(row for row in zip(*reversed(state)))


def tilt_north(state):
    state = [list(row) for row in state]

    for i, line in enumerate(state):
        if i == 0:
            continue

        for j, c in enumerate(line):
            if c == "O":
                last_possible_row = i
                for x in range(1, i + 1):
                    if state[i - x][j] == ".":
                        last_possible_row = i - x
                    else:
                        break
                if last_possible_row != i:
                    state[last_possible_row][j] = "O"
                    state[i][j] = "."

    return state


def calc_part1(input_str: str):
    state = input_str.splitlines()
    state = tilt_north(state)
    return calc_load(state)


def part1():
    erg = calc_part1(example.strip())
    print(f"Example Part 1: {erg}")
    assert erg == 136
    print(f"Result Part 1: {calc_part1(input_str)}")


def calc_part2(input_str):
    lines = input_str.splitlines()
    state = [list(line) for line in lines]

    previous_states = {}
    for i in range(4 * 1_000_000_000):
        state = rotate(tilt_north(state))
        if state in previous_states:
            break
        previous_states[state] = i

    shift = i - previous_states[state]
    num_cycles_left = (4_000_000_000 - i) % shift

    for _ in range(num_cycles_left - 1):
        state = rotate(tilt_north(state))

    return calc_load(state)


def part2():
    erg = calc_part2(example)
    print(f"Example Part 2: {erg}")
    assert erg == 64
    print(f"Result Part 2: {calc_part2(input_str)}")
