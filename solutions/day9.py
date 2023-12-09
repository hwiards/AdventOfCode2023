import os
from input_loader import load_input_str
from itertools import pairwise

input_str = load_input_str(os.path.basename(__file__)[:-3])

example = """0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45"""


def calc_next_value(sequence):
    if all(i == 0 for i in sequence):
        # end condition reached
        return sequence

    diffs = [b - a for a, b in pairwise(sequence)]
    extended_diff = calc_next_value(diffs)
    sequence.append(sequence[-1] + extended_diff[-1])
    return sequence


def calc(input_str, part2=False):
    next_values = []
    for line_str in input_str.splitlines():
        line = [int(i) for i in line_str.split()]
        if part2:
            line.reverse()
        longer_sequence = calc_next_value(line)
        next_values.append(longer_sequence[-1])

    return sum(next_values)


def part1():
    erg = calc(example.strip())
    print(f"Example Part 1: {erg}")
    assert erg == 114
    print(f"Result Part 1: {calc(input_str)}")


def part2():
    erg = calc(example, part2=True)
    print(f"Example Part 2: {erg}")
    assert erg == 2
    print(f"Result Part 2: {calc(input_str, part2=True)}")
