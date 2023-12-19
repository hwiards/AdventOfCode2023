import os
from input_loader import load_input_str
from helpers import *
import numpy as np

input_str = load_input_str(os.path.basename(__file__)[:-3])

example = """R 6 (#70c710)
D 5 (#0dc571)
L 2 (#5713f0)
D 2 (#d2c081)
R 2 (#59c680)
D 2 (#411b91)
L 5 (#8ceee2)
U 2 (#caa173)
L 1 (#1b58a2)
U 2 (#caa171)
R 2 (#7807d2)
U 3 (#a77fa3)
L 2 (#015232)
U 2 (#7a21e3)"""


def flood_fill(digged, start):
    filled = digged.copy()

    DIRS = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    todo = [start]
    visited = []
    while todo:
        elem = todo.pop()
        x, y = elem
        if elem in digged:
            continue
        filled.add(elem)
        visited.append(elem)
        for dx, dy in DIRS:
            if (x + dx, y + dy) not in visited:
                todo.append((x + dx, y + dy))
    return filled


def calc_part1(input_str):
    instructions = [
        (d, int(i)) for d, i, _ in (line.split() for line in input_str.splitlines())
    ]
    px, py = (0, 0)
    digged = set()
    digged.add((px, py))

    for d, i in instructions:
        for _ in range(i):
            match d:
                case "D":
                    py += 1
                case "U":
                    py -= 1
                case "L":
                    px -= 1
                case "R":
                    px += 1
            digged.add((px, py))

    minx = min(digged, key=lambda x: x[0])[0]
    maxx = max(digged, key=lambda x: x[0])[0]
    miny = min(digged, key=lambda x: x[1])[1]
    maxy = max(digged, key=lambda x: x[1])[1]

    for x in range(minx, maxx + 1):
        for y in range(miny, maxy + 1):
            if (x, y) in digged:
                continue
            inter = [(i, y) for i in range(minx, x) if (i, y) in digged]
            if len(inter) == 1:
                filled = flood_fill(digged, (x, y))
                return len(filled)


def part1():
    erg = calc_part1(example.strip())
    print(f"Example Part 1: {erg}")
    # assert erg == 4361


#    print(f"Result Part 1: {calc_part1(input_str)}")


def calc_part2(input_str):
    hex_vals = [line.split()[2][2:-1] for line in input_str.splitlines()]
    instr = [(int(val[-1], 16), int(val[:-1], 16)) for val in hex_vals]

    pos = (0, 0)
    verticies = [pos]
    complete_length = 0
    for dir, length in instr:
        complete_length += length
        match dir:
            case 0:
                pos = (pos[0], pos[1] + length)
            case 1:
                pos = (pos[0] + length, pos[1])
            case 2:
                pos = (pos[0], pos[1] - length)
            case 3:
                pos = (pos[0] - length, pos[1])

        verticies.append(pos)

    x = [a[0] for a in verticies]
    y = [a[1] for a in verticies]

    # using the shoelace formula
    return (
        0.5 * np.abs(np.dot(x, np.roll(y, 1)) - np.dot(y, np.roll(x, 1)))
        + complete_length / 2
        + 1
    )


def part2():
    erg = calc_part2(example)
    print(f"Example Part 2: {erg}")
    # assert erg == 467835
    print(f"Result Part 2: {calc_part2(input_str)}")
