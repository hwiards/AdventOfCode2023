import os
from input_loader import *
from helpers import *
from collections import Counter
from functools import cmp_to_key

input = load_input_str(os.path.basename(__file__)[:-3])

example = """32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483"""


CARDS = "23456789TJQKA"
CARD_STRENGTH = {card: strength for strength, card in enumerate(CARDS)}

CARDS2 = "J23456789TQKA"
CARD_STRENGTH2 = {card: strength for strength, card in enumerate(CARDS2)}

def get_type_of_card(card: str):
    count = Counter(card)

    if 5 in count.values():
        return 7
    if 4 in count.values():
        return 6
    if 3 in count.values():
        if 2 in count.values():
            return 5
        return 4
    if 2 in count.values():
        two_count = Counter(count.values())
        if two_count[2] == 2:
            # two pair
            return 3
        return 2
    return 1

def compare_high_card(first, second):

    for a,b in zip(first, second):
        if a == b:
            continue
        a_strength = CARD_STRENGTH[a]
        b_strength = CARD_STRENGTH[b]

        if a_strength > b_strength:
            return 1
        return -1
    return 0


def sort_cards(first_tuple, second_tuple):
    # negative first is smaller
    # zero equal
    # positive first is bigger

    first, _ = first_tuple
    second, _ = second_tuple

    # Compare type


    first_type = get_type_of_card(first)
    second_type = get_type_of_card(second)
    if first_type > second_type:
        return 1
    if first_type < second_type:
        return -1

    # compare high card
    return compare_high_card(first, second)


def calc_part1(input):
    lines = input.splitlines()

    hands_and_bids = []

    for line in lines:
        hand, bid = line.split()
        hands_and_bids.append((hand, int(bid)))

    sorted_hands_and_bids = sorted(hands_and_bids, key=cmp_to_key(sort_cards))

    return sum(pos * elem[1] for pos, elem in enumerate(sorted_hands_and_bids, 1))

def part1():
    erg = calc_part1(example.strip())
    print(f"Example Part 1: {erg}")
    #assert erg == 4361
    print(f"Result Part 1: {calc_part1(input)}")


def compare_high_card2(first, second, JOKER = False):

    for a,b in zip(first, second):
        if a == b:
            continue
        a_strength = CARD_STRENGTH2[a]
        b_strength = CARD_STRENGTH2[b]

        if a_strength > b_strength:
            return 1
        return -1
    return 0

def get_type_of_card2(card: str):
    count = Counter(card)
    j_count = count.pop("J") if "J" in count else 0

    if j_count == 5:
        return 7
    if j_count == 4:
        return 7
    if j_count == 3:
        if 2 in count.values():
            return 7
        else:
            return 6
    if j_count == 2:
        if 3 in count.values():
            return 7
        if 2 in count.values():
            return 6
        else:
            return 4

    if j_count == 1:
        if 4 in count.values():
            return 7
        if 3 in count.values():
            return 6

        two_count = Counter(count.values())
        if two_count[2] == 2:
            # Full House
            return 5
        if 2 in count.values():
            # Tripplets
            return 4
        # two pair
        return 2

    else:
        return get_type_of_card(card)



def sort_cards2(first_tuple, second_tuple):
    # negative first is smaller
    # zero equal
    # positive first is bigger

    first, _ = first_tuple
    second, _ = second_tuple

    # Compare type


    first_type = get_type_of_card2(first)
    second_type = get_type_of_card2(second)
    if first_type > second_type:
        return 1
    if first_type < second_type:
        return -1

    # compare high card
    return compare_high_card2(first, second)





def calc_part2(input):
    lines = input.splitlines()

    hands_and_bids = []

    for line in lines:
        hand, bid = line.split()
        hands_and_bids.append((hand, int(bid)))

    sorted_hands_and_bids = sorted(hands_and_bids, key=cmp_to_key(sort_cards2))

    return sum(pos * elem[1] for pos, elem in enumerate(sorted_hands_and_bids, 1))

def part2():
    erg = calc_part2(example)
    print(f"Example Part 2: {erg}")
    #assert erg == 467835
    print(f"Result Part 2: {calc_part2(input)}")
