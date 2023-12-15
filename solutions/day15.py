import os
from input_loader import load_input_str
from helpers import *
from collections import defaultdict

input_str = load_input_str(os.path.basename(__file__)[:-3])


example = """rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"""

def calc_hash(seq: str):
    cur = 0
    for c in seq:
        o = ord(c)
        cur += o
        cur *= 17
        cur %= 256

    return cur


def calc_part1(input_str):
    return sum (calc_hash(x) for x in input_str.split(","))

def part1():
    erg = calc_part1(example.strip())
    print(f"Example Part 1: {erg}")
    #assert erg == 4361
    print(f"Result Part 1: {calc_part1(input_str)}")


def calc_part2(input_str):
    seqs = input_str.split(",")

    boxes = defaultdict(list)
    for seq in seqs:
        if "-" in seq:
            label = seq[:-1]
            box = calc_hash(label)
            boxes[box] = [(labelo, lenso) for (labelo, lenso) in boxes[box] if labelo != label]

        elif "=" in seq:
            label, lens = seq.split("=")
            lens = int(lens)
            box = calc_hash(label)
            if label in [labelo for (labelo, _) in boxes[box]]:
                boxes[box] = [(label, lens) if labelo == label else (labelo, lenso) for (labelo, lenso) in boxes[box]]
            else:
                boxes[box].append((label, lens))

    power = 0
    for box, box_elems in boxes.items():
        for slot, (label, lens) in enumerate(box_elems,1):
            focal_power = (box+1)* slot * lens
            power += focal_power


    return power

def part2():
    erg = calc_part2(example)
    print(f"Example Part 2: {erg}")
    assert erg == 145
    print(f"Result Part 2: {calc_part2(input_str)}")
