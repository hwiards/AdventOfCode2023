import os
from input_loader import load_input_str
import re
from math import prod

input_str = load_input_str(os.path.basename(__file__)[:-3])

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


def get_cat_idx(cat: str) -> int:
    return "xmas".find(cat)


def check_accept(rating, workflows):
    workflow_rules = workflows["in"]

    while True:
        for rule in workflow_rules:
            if isinstance(rule, tuple):
                cat, comp, val, rulename_if_true = rule
                cat_rating = rating[get_cat_idx(cat)]
                if comp == ">":
                    if cat_rating > val:
                        rule = rulename_if_true
                    else:
                        continue
                else:
                    if cat_rating < val:
                        rule = rulename_if_true
                    else:
                        continue

            match rule:
                case "A":
                    return sum(rating)
                case "R":
                    return 0
                case _:
                    workflow_rules = workflows[rule]
                    break


def get_workflows(workflows_str: str) -> dict:
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

    return workflows


def calc_part1(input_str):
    workflows_str, ratings = input_str.split("\n\n")

    workflows = get_workflows(workflows_str)
    parts = [
        list(map(int, re.findall(r"\d+", rating)))
        for rating in ratings.splitlines()]

    return sum(check_accept(rating, workflows) for rating in parts)


def part1():
    erg = calc_part1(example.strip())
    print(f"Example Part 1: {erg}")
    assert erg == 19114
    print(f"Result Part 1: {calc_part1(input_str)}")


# Part 2
def perform_rule(workflows, workflow_name, possible_vals: list[set]):
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
            cat, comp, val, target_rulename_if_true = rule
            cat = get_cat_idx(cat)
            if comp == ">":
                in_range = possible_vals[cat].intersection(range(val + 1, 4000 + 1))
                out_range = possible_vals[cat].intersection(range(1, val + 1))
            else:
                in_range = possible_vals[cat].intersection(range(1, val))
                out_range = possible_vals[cat].intersection(range(val, 4000 + 1))

            in_ranges = list(possible_vals)
            out_ranges = list(possible_vals)
            in_ranges[cat], out_ranges[cat] = in_range, out_range

            combs += perform_rule(workflows, target_rulename_if_true, in_ranges)
            possible_vals = out_ranges
    return combs


def calc_part2(input_str):
    workflows_str, ratings = input_str.split("\n\n")

    workflows = get_workflows(workflows_str)
    possible_vals: list(set) = [set(range(1, 4000 + 1)) for _ in range(4)]

    return perform_rule(workflows, "in", possible_vals)


def part2():
    erg = calc_part2(example)
    print(f"Example Part 2: {erg}")
    assert erg == 167409079868000
    print(f"Result Part 2: {calc_part2(input_str)}")
