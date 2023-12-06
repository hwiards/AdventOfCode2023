import os
from input_loader import *
from helpers import *
from math import prod

input = """Time:        58     81     96     76
Distance:   434   1041   2219   1218"""

example = """Time:      7  15   30
Distance:  9  40  200"""

def calc_part1(input):
    lines = input.splitlines()
    times = [int(i) for i in lines[0].split()[1:]]
    distances = [int(i) for i in lines[1].split()[1:]]

    possibilities = []
    for time, dist in zip(times, distances):
        posi = list(i*(time-i) for i in range(time+1))
        valid_posi = [i for i in posi if i > dist]
        num_pos = len(valid_posi)
        possibilities.append(num_pos)

    return prod(possibilities)

def part1():
    erg = calc_part1(example.strip())
    print(f"Example Part 1: {erg}")
    assert erg == 288
    print(f"Result Part 1: {calc_part1(input)}")


def calc_part2(input):
    lines = input.splitlines()
    time = int("".join(lines[0].split()[1:]))
    dist = int("".join(lines[1].split()[1:]))

    posi = list(i * (time - i) for i in range(time + 1))
    valid_posi = [i for i in posi if i > dist]
    num_pos = len(valid_posi)


    return num_pos

def part2():
    erg = calc_part2(example)
    print(f"Example Part 2: {erg}")
    #assert erg == 467835
    print(f"Result Part 2: {calc_part2(input)}")
