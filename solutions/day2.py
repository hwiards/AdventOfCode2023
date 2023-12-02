import os
from input_loader import *
from helpers import *

input = load_input_str(os.path.basename(__file__)[:-3])

example = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""



def calc_part1(input):

    sum_of_possible_games = 0
    sum_of_powers = 0
    for game in input.splitlines():
        max_dict = {}
        game_id = int(game.split(":")[0].split(" ")[1])
        for round in game.split(":")[1].split(";"):
            for num_color in round.split(","):
                num, color = num_color.strip().split(" ")
                num = int(num)
                if color in max_dict:
                    if max_dict[color] < num:
                        max_dict[color] = num
                else:
                    max_dict[color] = num
        #print(max_dict)
        power = 1
        for num_items in max_dict.values():
            power *= num_items
        sum_of_powers += power
        if max_dict["red"] > 12 or max_dict["green"] > 13 or max_dict["blue"] > 14:
            continue
        sum_of_possible_games += game_id

    return sum_of_possible_games, sum_of_powers

def part1():
    erg, _ = calc_part1(example.strip())
    print(f"Example: {erg}")
    #assert erg == 123
    print(calc_part1(input))


def calc_part2(input):
    pass

def part2():
    pass
    _, erg = calc_part1(example)
    print(f"Example2: {erg}")
    #assert erg == 70
    _, erg = calc_part1(input)
    print(erg)
