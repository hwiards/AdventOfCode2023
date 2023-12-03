import os
from input_loader import *
from helpers import *

input = load_input_str(os.path.basename(__file__)[:-3])

example = """
"""

def calc_part1(input):
    pass

def part1():
    def part1():
        erg = calc_part1(example.strip())
        print(f"Example Part 1: {erg}")
        #assert erg == 4361
        print(f"Result Part 1: {calc_part1(input)}")


def calc_part2(input):
    pass

def part2():
    erg = calc_part2(example)
    print(f"Example Part 2: {erg}")
    assert erg == 467835
    print(f"Result Part 2: {calc_part2(input)}")
