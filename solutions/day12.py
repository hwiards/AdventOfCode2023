import os
from input_loader import load_input_str
from functools import cache

input_str = load_input_str(os.path.basename(__file__)[:-3])

example = """???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1"""


def calc_part1(input_str):
    lines = input_str.splitlines()
    return sum(calc_arrangements(line, part2=False) for line in lines)


def part1():
    erg = calc_part1(example.strip())
    print(f"Example Part 1: {erg}")
    assert erg == 21
    print(f"Result Part 1: {calc_part1(input_str)}")


@cache
def calc_arrangements_rec(records, cont_grps, num_quest_run=0):
    if len(records) == 0:
        # reached end of records, return 1 if runlen equals last grp element
        # or if no run expected (no group element left and run 0)
        if (((len(cont_grps) == 1 and cont_grps[0] == num_quest_run))
                or (len(cont_grps) == 0 and num_quest_run == 0)):
            return 1
        return 0

    rec_0 = records[0]
    records = records[1:]

    if cont_grps:
        cont_grp = cont_grps[0]
        remain_cont_grps = tuple(cont_grps[1:])
    else:
        cont_grp = 0
        remain_cont_grps = ()

    if rec_0 == "#":
        if num_quest_run > cont_grp:
            return 0
        return calc_arrangements_rec(records, cont_grps, num_quest_run + 1)
    if rec_0 == ".":
        if num_quest_run == cont_grp:
            return calc_arrangements_rec(records, remain_cont_grps, 0)
        if num_quest_run == 0:
            return calc_arrangements_rec(records, cont_grps, num_quest_run)
        return 0
    if rec_0 == "?":
        arrangements_dot = calc_arrangements_rec("." + records, cont_grps, num_quest_run)
        arrangements_octothorpe = calc_arrangements_rec("#" + records, cont_grps, num_quest_run)
        return arrangements_dot + arrangements_octothorpe


def calc_arrangements(line, part2=False):
    records, cont_grp_str = line.split()
    cont_grp = tuple(int(i) for i in cont_grp_str.split(","))

    if part2:
        records = "?".join([records] * 5)
        cont_grp = cont_grp * 5

    return calc_arrangements_rec(records, cont_grp)


def calc_part2(input_str):
    lines = input_str.splitlines()
    return sum(calc_arrangements(line, part2=True) for line in lines)


def part2():
    erg = calc_part2(example)
    print(f"Example Part 2: {erg}")
    assert erg == 525152
    print(f"Result Part 2: {calc_part2(input_str, )}")
