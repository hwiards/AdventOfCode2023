import os
from input_loader import *
from helpers import *
from itertools import pairwise
input = load_input_str(os.path.basename(__file__)[:-3])

example = """0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45"""

def calc_next_value(sequence):
    diffs = [b-a for a, b in pairwise(sequence)]
    if all(i == 0 for i in diffs):
        # end condition reached
        sequence.append(sequence[-1])
        return sequence
    else:
        longer_diff = calc_next_value(diffs)
        sequence.append(sequence[-1] + longer_diff[-1])
        return sequence



def calc_part1(input):
    next_values = []
    for line in input.splitlines():
        line = list(map(int, line.split()))
        longer_sequence = calc_next_value(line)
        next_values.append(longer_sequence[-1])

    return sum(next_values)

def part1():
    erg = calc_part1(example.strip())
    print(f"Example Part 1: {erg}")
    #assert erg == 4361
    print(f"Result Part 1: {calc_part1(input)}")


def calc_part2(input):
    next_values = []
    for line in input.splitlines():
        line = list(map(int, line.split()))
        line.reverse()
        longer_sequence = calc_next_value(line)
        next_values.append(longer_sequence[-1])

    return sum(next_values)

def part2():
    erg = calc_part2(example)
    print(f"Example Part 2: {erg}")
    #assert erg == 467835
    print(f"Result Part 2: {calc_part2(input)}")
