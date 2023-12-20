import math
import os
from input_loader import load_input_str
from helpers import *
from collections import defaultdict
input_str = load_input_str(os.path.basename(__file__)[:-3])

example = """broadcaster -> a, b, c
%a -> b
%b -> c
%c -> inv
&inv -> a"""


example2="""broadcaster -> a
%a -> inv, con
&inv -> b
%b -> con
&con -> output"""

def press_button(state, state_conjunct, instructions:dict[str, tuple], start="broadcaster", times=1000):
    highs, lows = 0, 0

    for _ in range(times):
        stack = [("broadcaster", 0, None)]
        lows += 1
        while stack:
            seq_elem, signal, sender = stack.pop(0)

            if seq_elem not in instructions:
                continue
            destinations, typ = instructions[seq_elem]

            if typ is None:
                lows += len(destinations)
                for dest in destinations:
                    #state[dest] = 0
                    stack.append((dest, 0, seq_elem))


            if typ == "%":
                if signal == 1:
                    continue
                new_state = 0 if state[seq_elem] else 1
                if new_state:
                    highs += len(destinations)
                else:
                    lows += len(destinations)
                for dest in destinations:
                    #state[dest] = new_state
                    stack.append((dest, new_state, seq_elem))
                state[seq_elem] = new_state


            if typ == "&":
                state_conjunct[seq_elem][sender] = signal
                new_state = 0 if all(state_conjunct[seq_elem].values()) else 1
                #new_state = and(1 )
                #new_state = any(1 if state[modul] == 0 else 0 for modul in state_conjunct[seq_elem])
                #new_state = 1 if new_state else 0
                if new_state:
                    highs += len(destinations)
                else:
                    lows += len(destinations)
                for dest in destinations:
                    #state[dest] = new_state
                    stack.append((dest, new_state, seq_elem))

    print(lows, highs)
    return highs * lows


def press_button2 (state, state_conjunct, instructions: dict[str, tuple], start="broadcaster"):
    highs, lows = 0, 0

    vals = {}
    n = 0
    while True:
        n+=1
        stack = [("broadcaster", 0, None)]
        lows += 1
        while stack:
            seq_elem, signal, sender = stack.pop(0)

            if seq_elem not in instructions:
                continue
            destinations, typ = instructions[seq_elem]

            if seq_elem == "cs" and sender != "broadcaster" and signal == 1:
                if sender not in vals:
                    vals[sender] = n
                if len(vals) == 4:
                    return math.lcm(*vals.values())



            if typ is None:
                lows += len(destinations)
                for dest in destinations:
                    # state[dest] = 0
                    stack.append((dest, 0, seq_elem))

            if typ == "%":
                if signal == 1:
                    continue
                new_state = 0 if state[seq_elem] else 1
                if new_state:
                    highs += len(destinations)
                else:
                    lows += len(destinations)
                for dest in destinations:
                    # state[dest] = new_state
                    stack.append((dest, new_state, seq_elem))
                state[seq_elem] = new_state

            if typ == "&":
                state_conjunct[seq_elem][sender] = signal
                new_state = 0 if all(state_conjunct[seq_elem].values()) else 1
                # new_state = and(1 )
                # new_state = any(1 if state[modul] == 0 else 0 for modul in state_conjunct[seq_elem])
                # new_state = 1 if new_state else 0
                if new_state:
                    highs += len(destinations)
                else:
                    lows += len(destinations)
                for dest in destinations:
                    # state[dest] = new_state
                    stack.append((dest, new_state, seq_elem))

    return 0


def calc_part1(input_str):
    instr = {}
    state = defaultdict(int)
    states_conjunct = {}

    for line in input_str.splitlines():
        module, destinations = line.split(" -> ")
        if module[0] == "%":
            dests = destinations.split(", ")
            instr[module[1:]] = (dests, module[0])
        elif module[0] == "&":
            dests = destinations.split(", ")
            instr[module[1:]] = (dests, module[0])
            #states_conjunct[module[1:]] = []
            states_conjunct[module[1:]] = {}
        else:
            instr[module] = (destinations.split(", "), None)

    for modul, (dests, typ) in instr.items():
        for dest in dests:
            if dest in states_conjunct:
                states_conjunct[dest][modul] = 0
                #states_conjunct[dest].append(modul)

    return press_button(state, states_conjunct, instr, "broadcaster", 1000)


def part1():
    erg = calc_part1(example2.strip())
    print(f"Example Part 1: {erg}")
    #assert erg == 4361
    print(f"Result Part 1: {calc_part1(input_str)}")


def calc_part2(input_str):
    instr = {}
    state = defaultdict(int)
    states_conjunct = {}

    for line in input_str.splitlines():
        module, destinations = line.split(" -> ")
        if module[0] == "%":
            dests = destinations.split(", ")
            instr[module[1:]] = (dests, module[0])
        elif module[0] == "&":
            dests = destinations.split(", ")
            instr[module[1:]] = (dests, module[0])
            #states_conjunct[module[1:]] = []
            states_conjunct[module[1:]] = {}
        else:
            instr[module] = (destinations.split(", "), None)

    for modul, (dests, typ) in instr.items():
        for dest in dests:
            if dest in states_conjunct:
                states_conjunct[dest][modul] = 0
                #states_conjunct[dest].append(modul)

    return press_button2(state, states_conjunct, instr, "broadcaster")


def part2():
#    erg = calc_part2(example)
#    print(f"Example Part 2: {erg}")
    #assert erg == 467835
    print(f"Result Part 2: {calc_part2(input_str)}")
