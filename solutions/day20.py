import math
import os
from input_loader import load_input_str
from collections import defaultdict

input_str = load_input_str(os.path.basename(__file__)[:-3])

example = """broadcaster -> a, b, c
%a -> b
%b -> c
%c -> inv
&inv -> a"""

example2 = """broadcaster -> a
%a -> inv, con
&inv -> b
%b -> con
&con -> output"""


def press_button(state, state_conjunct, instructions: dict[str, tuple], part2=False):
    highs, lows = 0, 0

    vals = {}
    n = 0
    while True:
        # Part 1
        if n == 1000 and not part2:
            return highs * lows

        n += 1
        stack = [("broadcaster", 0, None)]
        lows += 1
        while stack:
            seq_elem, signal, sender = stack.pop(0)

            if seq_elem not in instructions:
                continue
            destinations, typ = instructions[seq_elem]

            # Part 2
            if seq_elem == "cs" and signal == 1:
                if sender not in vals:
                    vals[sender] = n
                if len(vals) == 4:
                    return math.lcm(*vals.values())

            if typ is None:
                new_signal = 0

            if typ == "%":
                if signal == 1:
                    continue
                state[seq_elem] = new_signal = not state[seq_elem]

            if typ == "&":
                state_conjunct[seq_elem][sender] = signal
                new_signal = not all(state_conjunct[seq_elem].values())

            stack.extend((dest, new_signal, seq_elem) for dest in destinations)
            highs += len(destinations) if new_signal else 0
            lows += len(destinations) if not new_signal else 0


def parse(input_str):
    instr = {}
    state = defaultdict(int)
    states_conjunct = {}

    for line in input_str.splitlines():
        module, destinations = line.split(" -> ")
        if module[0] == "%" or module[0] == "&":
            dests = destinations.split(", ")
            instr[module[1:]] = (dests, module[0])
            if module[0] == "&":
                states_conjunct[module[1:]] = {}
        else:
            instr[module] = (destinations.split(", "), None)

    for modul, (dests, typ) in instr.items():
        for dest in dests:
            if dest in states_conjunct:
                states_conjunct[dest][modul] = 0

    return state, states_conjunct, instr


def calc_part1(input_str):
    state, states_conjunct, instr = parse(input_str)
    return press_button(state, states_conjunct, instr)


def part1():
    erg = calc_part1(example2.strip())
    print(f"Example Part 1: {erg}")
    assert erg == 11687500
    print(f"Result Part 1: {calc_part1(input_str)}")


def calc_part2(input_str):
    state, states_conjunct, instr = parse(input_str)
    return press_button(state, states_conjunct, instr, part2=True)


def part2():
    print(f"Result Part 2: {calc_part2(input_str)}")
