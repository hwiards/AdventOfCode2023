import math
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
        x1 = math.floor(time / 2 + math.sqrt((time / 2) ** 2 - (dist + 1)))
        x2 = math.ceil(time / 2 - math.sqrt((time / 2) ** 2 - (dist + 1)))
        possibilities.append(x1 - x2 + 1)

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

    x1 = math.floor(time / 2 + math.sqrt((time / 2) ** 2 - (dist + 1)))
    x2 = math.ceil(time / 2 - math.sqrt((time / 2) ** 2 - (dist + 1)))

    return x1 - x2 + 1


def part2():
    erg = calc_part2(example)
    print(f"Example Part 2: {erg}")
    # assert erg == 467835
    print(f"Result Part 2: {calc_part2(input)}")
