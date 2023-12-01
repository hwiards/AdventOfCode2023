import os
from input_loader import *
from helpers import *

input = load_input_str(os.path.basename(__file__)[:-3])

example = """1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
"""

example2="""two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen"""

str_digit_map = {
    "one" : 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven" : 7,
    "eight": 8,
    "nine": 9
}
def calc_part1(input):
    sum = 0
    for line in input.splitlines():
        for s in line:
            if s.isdigit():
                sum += 10*int(s)
                print(10*int(s))
                break
        for e in line[::-1]:
            if e.isdigit():
                sum += int(e)
                print(int(e))
                break

    return sum

def part1():
    erg = calc_part1(example.strip())
    print(f"Example: {erg}")
    assert erg == 142
#    print(calc_part1(input))


def calc_part2(input):
    sum = 0
    for line in input.splitlines():
        for count, s in enumerate(line):
            if s.isdigit():
                sum += 10*int(s)
                break
            for num_str, dig in str_digit_map.items():
                if line[count:count+len(num_str)] == num_str:
                    sum += 10*dig
                    break
            else:
                continue
            break
        for count, e in enumerate(line[::-1]):
            line_rev = line[::-1]
            if e.isdigit():
                sum += int(e)
                break
            for num_str, dig in str_digit_map.items():
                rev_numstr = num_str[::-1]
                sub_str = line_rev[count:count + len(num_str)]
                if sub_str == rev_numstr:
                    sum += dig
                    break
            else:
                continue
            break

    return sum


def part2():
    pass
    erg = calc_part2(example2)
    print(f"Example2: {erg}")
    assert erg == 281
    print(calc_part2(input))
