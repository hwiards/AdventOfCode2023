import os
from input_loader import *
from helpers import *

input = load_input_str(os.path.basename(__file__)[:-3])

example = """.....
.S-7.
.|.|.
.L-J.
....."""

EXAMPLE2="""..F7.
.FJ|.
SJ.L7
|F--J
LJ..."""

EXAMPLE3="""...........
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

DIRs = [(1,0), (0,1), (-1,0), (0, -1)]
pipes = {
    "|": ((-1, 0), (1, 0)),
    "-": ((0, -1), (0, 1)),
    "L": ((-1, 0), (0, 1)),
    "J": ((-1, 0), (0, -1)),
    "7": ((1, 0), (0, -1)),
    "F": ((1, 0), (0, 1))
}

def calc_part1(input):
    padded = pad(input, ".")
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

    for dir in DIRs:
        y_shift, x_shift = dir
        pipe_symbol = lines[S[0]+y_shift][S[1]+x_shift]
        if pipe_symbol in pipes:
            connect1, connect2 = pipes[pipe_symbol]
            if all(i == 0 for i in tadd(dir, connect1)) or all(i == 0 for i in tadd(dir, connect2)):
                act_dir = dir
                break

    steps = 0
    memory = []
    act_pos = S
    while True:
        memory.append(act_pos)
        next_y, next_x = tadd(act_pos, act_dir)
        next_pipe = lines[next_y][next_x]
        if next_pipe == "S":
            break
        next_dir = pipes[next_pipe][0] if not all(i == 0 for i in tadd(act_dir, pipes[next_pipe][0])) else pipes[next_pipe][1]
        act_pos = (next_y, next_x)
        act_dir = next_dir

    return len(memory)//2


def part1():
    erg = calc_part1(example.strip())
    print(f"Example Part 1: {erg}")
    erg = calc_part1(EXAMPLE2.strip())
    print(f"Example Part 1_2: {erg}")
    #assert erg == 4361
    print(f"Result Part 1: {calc_part1(input)}")


def get_elems_around(i,j):
    elems = []
    for dir in DIRs:
        y,x = dir
        elems.append((i+y, j+x))
    return elems

# def region_check(lines, memory):
#     not_enclosed = set()
#     enclosed = set()
#     memory = set(memory)
#     to_check = set()
#     checked = set()
#     for i, line in enumerate(lines):
#         for j, symbol in enumerate(line):
#             checked.add((i, j))
#             if symbol == "#":
#                 not_enclosed.add((i,j))
#                 continue
#             if (i, j) in memory:
#                 continue
#
#             if any(elem_around in not_enclosed for elem_around in get_elems_around(i, j)):
#                 not_enclosed.add((i, j))
#                 continue
#
#             to_check.add((i,j))
#
#     while True:
#         changed = False
#         for y, x in to_check:
#             if any(elem_around in not_enclosed for elem_around in get_elems_around(y, x)):
#                 not_enclosed.add((y, x))
#                 to_check.remove((y,x))
#                 changed = True
#                 break
#         if not changed:
#             break
#
#
#     enclosed = checked.difference(memory).difference(not_enclosed)
#     return len(enclosed)

def check_inside_loop(lines, loop):
    loop = set(loop)

    enclosed = set()

    for i, line in enumerate(lines):
        for j, symbol in enumerate(line):
            if (i, j) in loop or symbol == "#":
                continue
            inter_y_1 = [(y, j) for y in range(i) if (y, j) in loop and lines[y][j] == "-"]
            inter_y_2 = [(y, j) for y in range(i, len(lines)) if (y, j) in loop and lines[y][j] == "-"]
            inter_x_1 = [(i, x) for x in range(j) if (i, x) in loop and lines[i][x] in ["|", "L", "J", "S"]]
            inter_x_2 = [(i, x) for x in range(j, len(line)) if (i, x) in loop and lines[i][x] in ["|", "L", "J", "S"]]

            #if any(len(inter) % 2 == 1 for inter in [inter_x_1]):
            #    enclosed.add((i, j))

            if len(inter_x_1) % 2 == 1:
                enclosed.add((i,j))

    return len(enclosed)

def is_valid(lines, x, y, visited, loop):
    return lines[y][x] != "#" and (y,x) not in loop and visited[y][x] == 0

#def flood_fill(lines, x, y, visited, loop):
#    visited[y][x] =True
#    for dy, dx in DIRs:
#        next_y, next_x = y+dy, x+dx
#        if is_valid(lines, next_x, next_y, visited):


#def get_enclosed_points(lines, loop):
#    enclosed = set()
#    not_enclosed = set()
#    visited = [[ for _ in range(len(lines[0]))] for _ in range(len(lines))]



def replace_L(lines, loop):
    starty, startx = loop[0]
    for pipe, (dir1, dir2) in pipes.items():
        if (starty + dir1[0], startx+dir1[1]) in loop and (starty + dir2[0], startx+dir2[1]) in loop:
            newline = lines[starty][:startx] + pipe + lines[starty][startx+1:]
            lines[starty] = newline

    return lines

def calc_part2(input):
    padded = pad(input, "#")
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


    for dir in DIRs:
        y_shift, x_shift = dir
        pipe_symbol = lines[S[0]+y_shift][S[1]+x_shift]
        if pipe_symbol in pipes:
            connect1, connect2 = pipes[pipe_symbol]
            if all(i == 0 for i in tadd(dir, connect1)) or all(i == 0 for i in tadd(dir, connect2)):
                act_dir = dir
                break

    steps = 0
    memory = []
    memory_lines= []
    act_pos = S
    while True:
        memory.append(act_pos)
        act_pipe = lines[act_pos[0]][act_pos[1]]
        if act_pipe not in ["L", "J","7","F"]:
            memory_lines.append(act_pos)
        next_y, next_x = tadd(act_pos, act_dir)
        next_pipe = lines[next_y][next_x]
        if next_pipe == "S":
            break
        next_dir = pipes[next_pipe][0] if not all(i == 0 for i in tadd(act_dir, pipes[next_pipe][0])) else pipes[next_pipe][1]
        act_pos = (next_y, next_x)
        act_dir = next_dir

    lines = replace_L(lines, memory)
    return check_inside_loop(lines, memory)


def part2():
    erg = calc_part2(EXAMPLE5)
    print(f"Example Part 2: {erg}")
    #assert erg == 467835
    print(f"Result Part 2: {calc_part2(input)}")
