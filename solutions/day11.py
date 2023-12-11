import os
from input_loader import load_input_str

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

def expand(lines: list[str]):
    # expand rows
    row_expand = 0
    for i, line in enumerate(lines[:]):
        if line.count("#") == 0:
            lines.insert(i+1 + row_expand, line)
            row_expand += 1

    column_expand = 0
    for j in range(len(lines[0])):
        for line in lines:
            if line[j+column_expand] == "#":
                # galaxy found
                break
        else:
            for i, line in enumerate(lines[:]):
                new_line = line[:j+1+column_expand] + "." + line[j+1+column_expand:]
                lines[i] = new_line
            column_expand += 1

    return lines

def calc_part1(input_str):
    lines = input_str.splitlines()
    lines = expand(lines)

    galaxies = []
    distances = []
    for i, line in enumerate(lines):
        for j, space in enumerate(line):
            if space == '#':
                galaxies.append((i, j))

    for i in range(len(galaxies)):
        for j in range(i+1, len(galaxies)):
            x_gal1, y_gal1 = galaxies[i]
            x_gal2, y_gal2 = galaxies[j]
            distances.append(abs(x_gal1-x_gal2) + abs(y_gal1-y_gal2))

    return sum(distances)


def part1():
    erg = calc_part1(example.strip())
    print(f"Example Part 1: {erg}")
    #assert erg == 4361
    print(f"Result Part 1: {calc_part1(input_str)}")


def calc_part2(input_str, multi):
    multi = multi -1
    lines = input_str.splitlines()

    galaxies = []
    distances = []
    for i, line in enumerate(lines):
        for j, space in enumerate(line):
            if space == '#':
                galaxies.append((i, j))

    # row expand
    row_expand = 0
    for i in range(len(lines)):
        galaxies_in_row = [gala for gala in galaxies if gala[0] == i+row_expand]
        if len(galaxies_in_row) == 0:
            for x, gala in enumerate(galaxies):
                if gala[0] > i + row_expand:
                    galaxies[x] = (gala[0]+ multi, gala[1])
            row_expand += multi

    column_expand = 0
    for j in range(len(lines[0])):
        galaxies_in_column = [gala for gala in galaxies if gala[1] == j + column_expand]
        if len(galaxies_in_column) == 0:
            for y, gala in enumerate(galaxies):
                g0, g1 = gala
                compare = j + column_expand
                if g1 > compare:
                    galaxies[y] = (gala[0], gala[1]+ multi)
            column_expand += multi

    for i in range(len(galaxies)):
        for j in range(i+1, len(galaxies)):
            x_gal1, y_gal1 = galaxies[i]
            x_gal2, y_gal2 = galaxies[j]
            distances.append(abs(x_gal1-x_gal2) + abs(y_gal1-y_gal2))

    return sum(distances)


def part2():
    erg = calc_part2(example, 10)
    print(f"Example Part 2: {erg}")
    erg = calc_part2(example, 100)
    print(f"Example Part 2: {erg}")
    #assert erg == 467835
    print(f"Result Part 2: {calc_part2(input_str , 1_000_000)}")
