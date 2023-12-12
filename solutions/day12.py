import itertools
import os
from input_loader import load_input_str
from helpers import *
import re
from functools import cache

input_str = load_input_str(os.path.basename(__file__)[:-3])

example = """???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1"""

def calc_arrangements(line):
    num_arrangements = 0

    records, cont_grp_str = line.split()
    cont_grp = [int(i) for i in cont_grp_str.split(",")]
    n = list(records).count("?") # Number of questionmarks
    k = sum(cont_grp) - list(records).count("#")
    combinatons = list(itertools.combinations(range(0, n), k))

    for combinaton in combinatons:
        c = 0
        question_count = 0
        new_str_list = []
        for i in line:
            if i != '?':
                new_str_list.append(i)
            else:
                if c < len(combinaton) and combinaton[c] == question_count:
                    new_str_list.append("#")
                    c += 1
                else:
                    new_str_list.append('.')
                question_count += 1

        new_str = "".join(new_str_list)
        matches = [len(x) for x in re.findall(r'#+', new_str)]
        if matches == cont_grp:
            num_arrangements += 1

    return num_arrangements



def calc_part1(input_str):
    lines = input_str.splitlines()
    return sum(calc_arrangements(line) for line in lines)


def part1():
    erg = calc_part1(example.strip())
    #print(f"Example Part 1: {erg}")
    #assert erg == 4361
    #print(f"Result Part 1: {calc_part1(input_str)}")

@cache
def calc_arrangements_rec(records, cont_grps, num_quest_run = 0):
    if len(records) == 0:
        # reached end of records, return 1 if runlen equals last grp element of if no run expected (no group element left and run 0)
        if ((len(cont_grps) == 1 and cont_grps[0] == num_quest_run)) or (len(cont_grps) == 0 and num_quest_run == 0):
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
        return calc_arrangements_rec("."+records, cont_grps, num_quest_run) + calc_arrangements_rec("#"+records, cont_grps, num_quest_run)



def calc_arrangements2(line):
    records, cont_grp_str = line.split()
    cont_grp = tuple(int(i) for i in cont_grp_str.split(","))

    records = "?".join([records]*5)
    cont_grp = cont_grp*5

    return calc_arrangements_rec(records, cont_grp)



def calc_part2(input_str):
    lines = input_str.splitlines()
    return sum(calc_arrangements2(line) for line in lines)

def part2():
    erg = calc_part2(example)
    print(f"Example Part 2: {erg}")
    #assert erg == 467835
    print(f"Result Part 2: {calc_part2(input_str,)}")
