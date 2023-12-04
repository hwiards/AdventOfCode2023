import os
from input_loader import *
from helpers import *
from collections import defaultdict

input = load_input_str(os.path.basename(__file__)[:-3])

example = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"""

def calc_part1(input):

    points = 0
    for line in input.splitlines():
        winning_numbers = list(map(int, line.split("|")[0].split(":")[1].strip().split()))
        my_numbers = list(map(int, line.split("|")[1].split()))
        num_winners = len(set(winning_numbers).intersection(set(my_numbers)))
        points += 2**(num_winners-1) if num_winners > 0 else 0

    return points

def part1():
    erg = calc_part1(example.strip())
    print(f"Example Part 1: {erg}")
    #assert erg == 4361
    print(f"Result Part 1: {calc_part1(input)}")



def calc_part2(input):
    number_of_processed_cards = 0

    lines = input.splitlines()
    new_backlog_for_card = {}

    card_counter = { i:1 for i in range(1, len(lines)+1)}
    card_number = 1
    while sum(card_counter.values()):
        if card_number not in new_backlog_for_card:
            line = lines[card_number-1]
            winning_numbers = list(map(int, line.split("|")[0].split(":")[1].strip().split()))
            my_numbers = list(map(int, line.split("|")[1].split()))
            num_winners = len(set(winning_numbers).intersection(set(my_numbers)))
            new_backlog = [card_number + i for i in range(1, num_winners+1)]
            new_backlog_for_card[card_number] = new_backlog


        card_count = card_counter[card_number]
        card_counter[card_number] = 0
        backlog = new_backlog_for_card[card_number]
        for backlog_card in backlog:
            card_counter[backlog_card] = card_counter[backlog_card] + card_count


        number_of_processed_cards += card_count
        if card_number == len(lines):
            card_number = 1
        else:
            card_number += 1

    return number_of_processed_cards

def part2():
    erg = calc_part2(example)
    print(f"Example Part 2: {erg}")
    #assert erg == 467835
    print(f"Result Part 2: {calc_part2(input)}")
