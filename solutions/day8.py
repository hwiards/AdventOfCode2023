import os
from collections import defaultdict

from input_loader import *
from helpers import *
from itertools import cycle
from math import prod
from collections import Counter



input = load_input_str(os.path.basename(__file__)[:-3])

example = """RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)"""

EXAMPLE2= """LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)"""

def calc_part1(input:str):
    LR, network_block  =  input.split("\n\n")

    NETWORK = {}
    for line in network_block.splitlines():
        node, elements = line.split(" = ")
        l, r = elements.strip()[1:-1].split(", ")
        NETWORK[node] = (l,r)

    step_conter = 0
    act_node = "AAA"
    for DIR in cycle(LR):
        l, r = NETWORK[act_node]
        if DIR == "L":
            act_node = l
        else:
            act_node = r

        step_conter += 1

        if act_node == "ZZZ":
            return step_conter


def part1():
    erg = calc_part1(example.strip())
    print(f"Example Part 1: {erg}")
    #assert erg == 4361
    print(f"Result Part 1: {calc_part1(input)}")


def primes(n):
    primfac = []
    d = 2
    while d*d <= n:
        while (n % d) == 0:
            primfac.append(d)
            n //= d
        d += 1
    if n > 1:
       primfac.append(n)
    return primfac

def calc_part2(input):
    LR, network_block = input.split("\n\n")

    NETWORK = {}
    for line in network_block.splitlines():
        node, elements = line.split(" = ")
        l, r = elements.strip()[1:-1].split(", ")
        NETWORK[node] = (l, r)

    step_conter = 0

    act_nodes = [i for i in NETWORK.keys() if i[2] == "A"]
    end_steps = [0]*len(act_nodes)

    for DIR in cycle(LR):
        for i, act_node in enumerate(act_nodes[:]):
            if end_steps[i] != 0: continue
            l, r = NETWORK[act_node]
            if DIR == "L":
                act_nodes[i] = l
            else:
                act_nodes[i] = r

            if act_nodes[i][2] == "Z":
                end_steps[i] = step_conter + 1



        step_conter += 1
        if end_steps.count(0) == 0:
            break

    prime_factor_list = [primes(n) for n in end_steps]
    relevant_prime_factors = defaultdict(int)
    for factors in prime_factor_list:
        count = Counter(factors)
        for factor, factor_count in count.items():
            if relevant_prime_factors[factor] < factor_count:
                relevant_prime_factors[factor] = factor_count

    return prod([factor**count for factor, count in relevant_prime_factors.items()])

def part2():
    erg = calc_part2(EXAMPLE2)
    print(f"Example Part 2: {erg}")
    #assert erg == 467835
    print(f"Result Part 2: {calc_part2(input)}")
