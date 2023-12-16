import os
from input_loader import load_input_str
from helpers import *

input_str = load_input_str(os.path.basename(__file__)[:-3])

example = """.|...\\....
|.-.\\.....
.....|-...
........|.
..........
.........\\
..../.\\\\..
.-.-/..|..
.|....-|.\\
..//.|...."""

def run_beam(grid, pos, direction, energized):
    act_x, act_y = pos
    dirx, diry = direction

    while 0 <= act_x < len(grid) and 0 <= act_y < len(grid[0]):
        act_tile = grid[act_x][act_y]
        act_state = (act_x, act_y, dirx, diry)
        if act_state in energized:
            return energized
        energized.add(act_state)

        if act_tile == "/":
            if dirx == 0:
                dirx, diry = -1 * diry, 0
            else:
                dirx, diry = 0, -1*dirx
        if act_tile == '\\':
            if dirx == 0:
                dirx, diry = diry, 0
            else:
                dirx, diry = 0, dirx
        if act_tile == "|":
            if dirx == 0:
                dirx = 1
                diry = 0
                energized = run_beam(grid, (act_x-1, act_y), (-1,0), energized)
        if act_tile == "-":
            if diry == 0:
                dirx = 0
                diry = 1
                energized = run_beam(grid, (act_x, act_y-1), (0, -1), energized)

        act_x += dirx
        act_y += diry


    # for x in range(len(grid)):
    #     for y in range(len(grid[0])):
    #         if (x,y) in energized:
    #             print("#", end="")
    #         else:
    #             print(" ", end="")
    #     print()

    return energized


def calc_part1(input_str):
    grid = input_str.splitlines()
    start = (0,0)
    direction = (0,1)

    states = run_beam(grid, start, direction, set())
    energized_positions = {(x,y) for (x,y,dx, dy) in states}
    return len(energized_positions)


def part1():
    erg = calc_part1(example.strip())
    print(f"Example Part 1: {erg}")
    assert erg == 46
    print(f"Result Part 1: {calc_part1(input_str)}")


def calc_part2(input_str):
    grid = input_str.splitlines()

    states_list = []
    for y in range(len(grid[0])):
        states_list.append(run_beam(grid, (0, y), (1,0), set()))
        states_list.append(run_beam(grid, (len(grid)-1, y), (-1,0), set()))

    for x in range(len(grid)):
        states_list.append(run_beam(grid, (x, 0), (0, 1), set()))
        states_list.append(run_beam(grid, (x, len(grid[0])-1), (0, -11), set()))

    energized_pos_list = [
        len({(x, y) for (x, y, dx, dy) in states}) for states in states_list
    ]

    return max(energized_pos_list)

def part2():
    erg = calc_part2(example)
    print(f"Example Part 2: {erg}")
    assert erg == 51
    print(f"Result Part 2: {calc_part2(input_str)}")
