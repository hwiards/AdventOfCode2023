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

CARDS_JOKER = "J23456789TQKA"
CARD_STRENGTH_JOKER = {card: strength for strength, card in enumerate(CARDS_JOKER)}


def compare_high_card(first, second, JOKER=False):
    for a, b in zip(first, second):
        if a == b:
            continue

        if not JOKER:
            a_strength = CARD_STRENGTH[a]
            b_strength = CARD_STRENGTH[b]
        else:
            a_strength = CARD_STRENGTH_JOKER[a]
            b_strength = CARD_STRENGTH_JOKER[b]

        if a_strength > b_strength:
            return 1
        return -1
    return 0


def get_type_of_card(card: str, JOKER=False):
    count = Counter(card)
    j_count = count.pop("J", 0) if JOKER else 0

    if j_count >= 4:
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
        if list(count.values()).count(2) == 2:
            # Full House
            return 5
        if 2 in count.values():
            # Tripplets
            return 4
        # One pair
        return 2

    if 5 in count.values():
        return 7
    if 4 in count.values():
        return 6
    if 3 in count.values() and 2 in count.values():
        return 5
    if 3 in count.values():
        return 4
    if list(count.values()).count(2) == 2:
        return 3  # Two Pair
    if 2 in count.values():
        return 2  # One Pair
    return 1  # High Card


def sort_cards(first_tuple, second_tuple, JOKER = False):
    # negative first is smaller
    # zero equal
    # positive first is bigger

    first, _ = first_tuple
    second, _ = second_tuple

    # Compare type
    first_type = get_type_of_card(first, JOKER)
    second_type = get_type_of_card(second, JOKER)
    if first_type > second_type:
        return 1
    if first_type < second_type:
        return -1

    # compare high card
    return compare_high_card(first, second, JOKER)


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
    # assert erg == 4361
    print(f"Result Part 1: {calc_part1(input)}")



def calc_part2(input):
    lines = input.splitlines()

    hands_and_bids = []

    for line in lines:
        hand, bid = line.split()
        hands_and_bids.append((hand, int(bid)))

    def sort_cards_joker(c1, c2):
        return sort_cards(c1, c2, JOKER=True)

    sorted_hands_and_bids = sorted(hands_and_bids, key=cmp_to_key(sort_cards_joker))

    return sum(pos * elem[1] for pos, elem in enumerate(sorted_hands_and_bids, 1))


def part2():
    erg = calc_part2(example)
    print(f"Example Part 2: {erg}")
    # assert erg == 467835
    print(f"Result Part 2: {calc_part2(input)}")
