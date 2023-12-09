import math
import os

from input_loader import load_input_str
from itertools import cycle

input_str = load_input_str(os.path.basename(__file__)[:-3])

example = """RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)"""

EXAMPLE2 = """LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)"""


def calc_part1(input_str: str):
    lr, network_block = input_str.split("\n\n")

    network = {}
    for line in network_block.splitlines():
        node, elements = line.split(" = ")
        l, r = elements.strip()[1:-1].split(", ")
        network[node] = (l, r)

    step_conter = 0
    act_node = "AAA"
    for direction in cycle(lr):
        l, r = network[act_node]
        if direction == "L":
            act_node = l
        else:
            act_node = r

        step_conter += 1

        if act_node == "ZZZ":
            break

    return step_conter


def part1():
    erg = calc_part1(example.strip())
    print(f"Example Part 1: {erg}")
    # assert erg == 4361
    print(f"Result Part 1: {calc_part1(input_str)}")


def calc_part2(input_str):
    lr, network_block = input_str.split("\n\n")

    network = {}
    for line in network_block.splitlines():
        node, elements = line.split(" = ")
        l, r = elements.strip()[1:-1].split(", ")
        network[node] = (l, r)

    step_conter = 0

    act_nodes = [i for i in network.keys() if i[2] == "A"]
    end_steps = [0] * len(act_nodes)

    for direction in cycle(lr):
        for i, act_node in enumerate(act_nodes[:]):
            if end_steps[i] != 0:
                continue
            l, r = network[act_node]
            if direction == "L":
                act_nodes[i] = l
            else:
                act_nodes[i] = r

            if act_nodes[i][2] == "Z":
                end_steps[i] = step_conter + 1

        step_conter += 1
        if end_steps.count(0) == 0:
            break

    return math.lcm(*end_steps)


def part2():
    erg = calc_part2(EXAMPLE2)
    print(f"Example Part 2: {erg}")
    # assert erg == 467835
    print(f"Result Part 2: {calc_part2(input_str)}")
