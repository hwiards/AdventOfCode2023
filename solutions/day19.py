import os
from input_loader import load_input_str
from helpers import *
import re
from math import prod
input_str = load_input_str(os.path.basename(__file__)[:-3])

from itertools import combinations


example = """px{a<2006:qkq,m>2090:A,rfg}
pv{a>1716:R,A}
lnx{m>1548:A,A}
rfg{s<537:gd,x>2440:R,A}
qs{s>3448:A,lnx}
qkq{x<1416:A,crn}
crn{x>2662:A,R}
in{s<1351:px,qqz}
qqz{s>2770:qs,m<1801:hdj,R}
gd{a>3333:R,R}
hdj{m>838:A,pv}

{x=787,m=2655,a=1222,s=2876}
{x=1679,m=44,a=2067,s=496}
{x=2036,m=264,a=79,s=2244}
{x=2461,m=1339,a=466,s=291}
{x=2127,m=1623,a=2188,s=1013}"""

def get_cat_idx(cat:str):
    match cat:
        case "x":
            return 0
        case "m":
            return 1
        case "a":
            return 2
        case "s":
            return 3

def check_accept(rating, workflows):
    workflow_rules = workflows["in"]

    while True:
        for rule in workflow_rules:
            if isinstance(rule, tuple):
                cat, comp, val, then = rule
                cat_rating = rating[get_cat_idx(cat)]
                if comp == ">":
                    if cat_rating > val:
                        rule = then
                    else: continue
                else:
                    if cat_rating < val:
                        rule = then
                    else: continue

            match rule:
                case "A":
                    return sum(rating)
                case "R":
                    return 0
                case _:
                    workflow_rules = workflows[rule]
                    break

def check_accept2(rating, workflows):
    workflow_rules = workflows["in"]

    while True:
        for rule in workflow_rules:
            if isinstance(rule, tuple):
                cat, comp, val, then = rule
                cat_rating = rating[get_cat_idx(cat)]
                if comp == ">":
                    if cat_rating > val:
                        rule = then
                    else: continue
                else:
                    if cat_rating < val:
                        rule = then
                    else: continue

            match rule:
                case "A":
                    return 1
                case "R":
                    return 0
                case _:
                    workflow_rules = workflows[rule]
                    break


def calc_part1(input_str):

    workflows_str, ratings = input_str.split("\n\n")

    workflows = {}
    for line in workflows_str.splitlines():
        name, rules_str = line.split("{")
        rules = []
        for rule in rules_str[:-1].split(","):
            if ":" not in rule:
                rules.append(rule)
            else:
                cat = rule[0]
                comp = rule[1]
                val, then = rule[2:].split(":")
                rules.append((cat, comp, int(val), then))
        workflows[name] = rules

    parts = [list(map(int,re.findall("\d+", rating))) for rating in ratings.splitlines()]

    return sum(check_accept(rating, workflows) for rating in parts)



def part1():
    erg = calc_part1(example.strip())
    print(f"Example Part 1: {erg}")
    #assert erg == 4361
    print(f"Result Part 1: {calc_part1(input_str)}")



def perform_rule(workflows, workflow_name, possible_vals:list[set]):

    if workflow_name == "A":
        return prod(len(val) for val in possible_vals)

    if workflow_name == "R":
        return 0

    rules = workflows[workflow_name]

    combs = 0
    for rule in rules:
        if isinstance(rule, str):
            combs += perform_rule(workflows, rule, possible_vals)
        else:
            cat, comp, val, then = rule
            cat = get_cat_idx(cat)
            if comp == ">":
                in_range = possible_vals[cat].intersection(range(val+1, 4000+1))
                out_range = possible_vals[cat].intersection(range(1, val+1))
            else:
                in_range = possible_vals[cat].intersection(range(1, val))
                out_range = possible_vals[cat].intersection(range(val, 4000+1))


            in_ranges = possible_vals.copy()
            in_ranges[cat] = in_range
            out_ranges = possible_vals.copy()
            out_ranges[cat] = out_range

            combs += perform_rule(workflows, then, in_ranges)
            possible_vals = out_ranges
    return combs


def calc_part2(input_str):
    workflows_str, ratings = input_str.split("\n\n")

    workflows = {}
    for line in workflows_str.splitlines():
        name, rules_str = line.split("{")
        rules = []
        for rule in rules_str[:-1].split(","):
            if ":" not in rule:
                rules.append(rule)
            else:
                cat = rule[0]
                comp = rule[1]
                val, then = rule[2:].split(":")
                rules.append((cat, comp, int(val), then))
        workflows[name] = rules

    possible_vals: list(set) = [set(range(1,4000+1)), set(range(1,4000+1)), set(range(1,4000+1)), set(range(1,4000+1))]
    # confirmed_vals: list(set) = [set(), set(), set(), set()]
    # for i in range(4):
    #     for val in possible_vals[i]:
    #         arr = [0,0,0,0]
    #         arr[i] = val
    #         if check_accept(arr, workflows):
    #             confirmed_vals[i].add(val)
    #
    # combinations = 0
    # for i in range(4):
    #     new_combs = len(confirmed_vals[i]) * 4000**(3-1)
    #     for j in range(i):
    #         new_combs *= 4000-len(confirmed_vals[j])
    #     combinations += new_combs
    #
    # # check remaining double configs
    # for i in range(4):
    #     possible_vals[i] = possible_vals[i] - confirmed_vals[i]
    #
    # confirmed_combs = []
    # for a,b in combinations(range(4), 2):
    #     for val1 in possible_vals[a]:
    #         for val2 in possible_vals[b]:
    #             arr = [0,0,0,0]
    #             arr[a] = val1
    #             arr[b] = val2
    #             if check_accept2(arr, workflows):
    #                 confirmed_combs.append(arr)

    return perform_rule(workflows, "in", possible_vals)






def part2():
    erg = calc_part2(example)
    print(f"Example Part 2: {erg}")
    #assert erg == 467835
    print(f"Result Part 2: {calc_part2(input_str)}")
