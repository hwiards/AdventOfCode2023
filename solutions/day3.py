import os
from input_loader import *
from helpers import *
import re
from math import prod

input = load_input_str(os.path.basename(__file__)[:-3])

example = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""

SYMBOLS = ["*", "/", "=", "#", "$", "@", "&", "%", "+", "-", "§"]

def calc_part1(input:str):
    sum_of_partnumbers = 0
    input_lines = input.splitlines()
    for line_num, line in enumerate(input_lines):
        i = 0
        line : str = line
        while i < len(line):
            if line[i].isdigit():
                for j in range(4): #assumtion that number is at most 3 long
                    if i+j == len(line) or not line[i+j].isdigit():
                        break

                # walk around number
                for k in range(i-1, i+j+1):
                    if k >= 0 and k < len(line.strip()):
                        if input_lines[line_num][k] in SYMBOLS:
                            sum_of_partnumbers += int(line[i:i+j])
                            break
                        if line_num != 0:
                            if input_lines[line_num-1][k] in SYMBOLS:
                                sum_of_partnumbers += int(line[i:i+j])
                                break
                        if line_num != len(input_lines)-1:
                            if input_lines[line_num+1][k] in SYMBOLS:
                                sum_of_partnumbers += int(line[i:i+j])
                                break

                i = i+j
                continue
            i = i+1

    return sum_of_partnumbers

def part1():
    erg = calc_part1(example.strip())
    print(f"Example: {erg}")
    #assert erg == 123
    print(calc_part1(input))


def find_number(line, search_start):
    number_start = search_start
    number_end = search_start
    for i in range(search_start, search_start-3, -1):
        if line[i].isdigit(): number_start = i
        else: break

    for i in range(search_start, search_start+3):
        if line[i].isdigit():
            number_end = i
        else:
            break

    return int(line[number_start: number_end+1]), number_end





def calc_part2(input):
    gear_ratios = 0
    input_lines = input.splitlines()
    for line_num, line in enumerate(input_lines):
        for i in range(len(line)):
            if line[i] == "*":
                numbers = []

                for l in range(line_num - 1, line_num + 2):
                    k = i-1
                    while k < i + 2:
                        if k >= 0 and k < len(line.strip()) and l >= 0 and l < len(input_lines):
                            if input_lines[l][k].isdigit():
                                found_number, end_pos = find_number(input_lines[l], k)
                                numbers.append(found_number)
                                k = end_pos
                        k += 1

                if len(numbers) == 2:
                    product = prod(numbers)
                    gear_ratios += prod(numbers)
    return gear_ratios


def part2():
    erg = calc_part2(example)
    print(f"Example2: {erg}")
#    assert erg == 70
    print(calc_part2(input))
