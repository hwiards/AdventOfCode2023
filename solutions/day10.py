import os
from input_loader import load_input_str
from helpers import tadd, pad

input_str = load_input_str(os.path.basename(__file__)[:-3])

example = """.....
.S-7.
.|.|.
.L-J.
....."""

EXAMPLE2 = """..F7.
.FJ|.
SJ.L7
|F--J
LJ..."""

EXAMPLE3 = """...........
.S-------7.
.|F-----7|.
.||.....||.
.||.....||.
.|L-7.F-J|.
.|..|.|..|.
.L--J.L--J.
..........."""

EXAMPLE4 = """FF7FSF7F7F7F7F7F---7
L|LJ||||||||||||F--J
FL-7LJLJ||||||LJL-77
F--JF--7||LJLJ7F7FJ-
L---JF-JLJ.||-FJLJJ7
|F|F-JF---7F7-L7L|7|
|FFJF7L7F-JF7|JL---7
7-L-JL7||F7|L7F-7F7|
L.L7LFJ|||||FJL7||LJ
L7JLJL-JLJLJL--JLJ.L"""

EXAMPLE5 = """.F----7F7F7F7F-7....
.|F--7||||||||FJ....
.||.FJ||||||||L7....
FJL7L7LJLJ||LJ.L-7..
L--J.L7...LJS7F-7L7.
....F-J..F7FJ|L7L7L7
....L7.F7||L7|.L7L7|
.....|FJLJ|FJ|F7|.LJ
....FJL-7.||.||||...
....L---J.LJ.LJLJ..."""

DIRs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
pipes = {
    "|": ((-1, 0), (1, 0)),
    "-": ((0, -1), (0, 1)),
    "L": ((-1, 0), (0, 1)),
    "J": ((-1, 0), (0, -1)),
    "7": ((1, 0), (0, -1)),
    "F": ((1, 0), (0, 1)),
}


def calc(input_str, part2=False):
    padded = pad(input_str, ".")
    lines = padded.splitlines()

    S = None
    for i, line in enumerate(lines):
        for j, symbol in enumerate(line):
            if symbol == "S":
                S = (i, j)
                break
        else:
            continue
        break

    for direction in DIRs:
        y_shift, x_shift = direction
        pipe_symbol = lines[S[0] + y_shift][S[1] + x_shift]
        if pipe_symbol in pipes:
            connect1, connect2 = pipes[pipe_symbol]
            if all(i == 0 for i in tadd(direction, connect1)) or all(
                i == 0 for i in tadd(direction, connect2)
            ):
                act_dir = direction
                break

    memory = []
    act_pos = S
    while True:
        memory.append(act_pos)
        next_y, next_x = tadd(act_pos, act_dir)
        next_pipe = lines[next_y][next_x]
        if next_pipe == "S":
            break
        next_dir = (
            pipes[next_pipe][0]
            if not all(i == 0 for i in tadd(act_dir, pipes[next_pipe][0]))
            else pipes[next_pipe][1]
        )
        act_pos = (next_y, next_x)
        act_dir = next_dir

    if not part2:
        return len(memory) // 2

    lines = replace_s(lines, memory)
    return check_inside_loop(lines, memory)


def check_inside_loop(lines, loop):
    loop = set(loop)
    enclosed = set()

    for i, line in enumerate(lines):
        for j, symbol in enumerate(line):
            if (i, j) in loop or symbol == "#":
                continue
            # Count the intersections toward the left side.
            # If it is odd, then it is within the loop
            inter_x = [
                (i, x)
                for x in range(j)
                if (i, x) in loop and lines[i][x] in ["|", "L", "J"]
            ]

            if len(inter_x) % 2 == 1:
                enclosed.add((i, j))

    return len(enclosed)


def replace_s(lines, loop):
    starty, startx = loop[0]
    for pipe, (dir1, dir2) in pipes.items():
        dir_in_loop1 = (starty + dir1[0], startx + dir1[1]) in loop
        dir_in_loop2 = (starty + dir2[0], startx + dir2[1]) in loop
        if dir_in_loop1 and dir_in_loop2:
            newline = lines[starty][:startx] + pipe + lines[starty][startx + 1 :]
            lines[starty] = newline

    return lines


def part1():
    erg = calc(example.strip())
    print(f"Example Part 1: {erg}")
    erg = calc(EXAMPLE2.strip())
    print(f"Example Part 1_2: {erg}")
    assert erg == 8
    print(f"Result Part 1: {calc(input_str)}")


def part2():
    erg = calc(EXAMPLE4, part2=True)
    print(f"Example Part 2: {erg}")
    assert erg == 10
    print(f"Result Part 2: {calc(input_str, part2=True)}")
