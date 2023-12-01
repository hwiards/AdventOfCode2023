import os
from input_loader import *
from helpers import *

input = load_input_str(os.path.basename(__file__)[:-3])

example = """1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
"""

example2 = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen"""

str_digit_map = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]


def calc_part1(input_string):
    def find_first_digit(s):
        for char in s:
            if char.isdigit():
                return int(char)
        return 0

    calibration_values = 0
    for line in input_string.splitlines():
        first_digit = find_first_digit(line)
        last_digit = find_first_digit(line[::-1])
        calibration_values += 10 * first_digit + last_digit

    return calibration_values


def part1():
    print("Part 1:")
    erg = calc_part1(example.strip())
    print(f"Example {erg}")
    assert erg == 142
    print(calc_part1(input))



def find_substr(line: str, reverse=False):
    digit_map = {str(dig): num for num, dig in enumerate(str_digit_map, 1)}

    # Helper function to find substring digit
    def find_digit_substring(s):
        for digit_str, digit_num in digit_map.items():
            if s.startswith(digit_str):
                return digit_num
        return None

    # Iterating over the string
    range_func = range(len(line) - 1, -1, -1) if reverse else range(len(line))
    for i in range_func:
        if line[i].isdigit():
            return int(line[i])
        digit = find_digit_substring(line[i:])
        if digit is not None:
            return digit

def calc_part2(input):
    calibration_values = 0
    for line in input.splitlines():
        first_digit = find_substr(line)
        last_digit = find_substr(line, reverse=True)
        calibration_values += 10*first_digit + last_digit

    return calibration_values


def part2():
    print("Part 2:")
    erg = calc_part2(example2)
    print(f"Example {erg}")
    assert erg == 281
    print(calc_part2(input))
