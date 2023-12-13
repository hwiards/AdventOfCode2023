import os
from input_loader import load_input_str

input_str = load_input_str(os.path.basename(__file__)[:-3])

example = """#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.

#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#"""


def calc_line_diff(line1, line2):
    num_diff = sum(1 for a, b in zip(line1, line2) if a != b)
    return num_diff


def calc_notes2(pattern):
    pattern = pattern.splitlines()

    # horizontal
    for split_idx in range(1, len(pattern)):
        diffs = 0
        for i in range(split_idx):
            idx_lower = split_idx - i - 1
            idx_upper = split_idx + i
            if idx_lower >= 0 and idx_upper < len(pattern):
                diffs += calc_line_diff(pattern[idx_lower], pattern[idx_upper])

        if diffs == 1:
            return split_idx * 100

    # vertical
    for split_idx in range(1, len(pattern[0])):
        diffs = 0
        for i in range(split_idx):

            idx_lower = split_idx - i - 1
            idx_upper = split_idx + i
            if idx_lower < 0 or idx_upper >= len(pattern[0]):
                continue
            col_lower = "".join(a[idx_lower] for a in pattern)
            col_upper = "".join(a[idx_upper] for a in pattern)
            diffs += calc_line_diff(col_upper, col_lower)

        if diffs == 1:
            return split_idx

    return 0


def calc_notes(pattern):
    pattern = pattern.splitlines()

    # horizontal
    for split_idx in range(1, len(pattern)):
        for i in range(split_idx):
            idx_lower = split_idx - i - 1
            idx_upper = split_idx + i
            if idx_lower >= 0 and idx_upper < len(pattern) and pattern[idx_lower] != pattern[idx_upper]:
                break
        else:
            return split_idx * 100

    for split_idx in range(1, len(pattern[0])):
        for i in range(split_idx):

            idx_lower = split_idx - i - 1
            idx_upper = split_idx + i
            if idx_lower < 0 or idx_upper >= len(pattern[0]):
                continue
            col_lower = "".join(a[idx_lower] for a in pattern)
            col_upper = "".join(a[idx_upper] for a in pattern)
            if col_upper != col_lower:
                break
        else:
            return split_idx

    return 0


def calc_part1(input_str):
    patterns = input_str.split("\n\n")
    return sum(calc_notes(pattern) for pattern in patterns)


def part1():
    erg = calc_part1(example.strip())
    print(f"Example Part 1: {erg}")
    assert erg == 405
    print(f"Result Part 1: {calc_part1(input_str)}")


def calc_part2(input_str):
    patterns = input_str.split("\n\n")
    return sum(calc_notes2(pattern) for pattern in patterns)


def part2():
    erg = calc_part2(example)
    print(f"Example Part 2: {erg}")
    assert erg == 400
    print(f"Result Part 2: {calc_part2(input_str)}")
