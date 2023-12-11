import os
from input_loader import load_input_str
from itertools import combinations

input_str = load_input_str(os.path.basename(__file__)[:-3])

example = """...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#....."""


def part1():
    erg = calc(example.strip(), multi=2)
    print(f"Example Part 1: {erg}")
    assert erg == 374
    print(f"Result Part 1: {calc(input_str, multi=2)}")


def calc(input_str, multi):
    multi = multi - 1
    lines = input_str.splitlines()

    galaxies = [
        (i, j)
        for i, line in enumerate(lines)
        for j, space in enumerate(line)
        if space == "#"
    ]

    # row expand
    row_expand = 0
    for i in range(len(lines)):
        galaxies_in_row = [gala for gala in galaxies if gala[0] == i + row_expand]
        if not galaxies_in_row:
            for x, (g0, g1) in enumerate(galaxies):
                if g0 > i + row_expand:
                    galaxies[x] = (g0 + multi, g1)
            row_expand += multi

    column_expand = 0
    for j in range(len(lines[0])):
        galaxies_in_column = [gala for gala in galaxies if gala[1] == j + column_expand]
        if not galaxies_in_column:
            for y, (g0, g1) in enumerate(galaxies):
                if g1 > j + column_expand:
                    galaxies[y] = (g0, g1 + multi)
            column_expand += multi

    distances = [
        abs(x1 - x2) + abs(y1 - y2) for (x1, y1), (x2, y2) in combinations(galaxies, 2)
    ]

    return sum(distances)


def part2():
    erg = calc(example, 10)
    print(f"Example Part 2: {erg}")
    assert erg == 1030
    erg = calc(example, 100)
    print(f"Example Part 2: {erg}")
    assert erg == 8410
    print(f"Result Part 2: {calc(input_str, 1_000_000)}")
