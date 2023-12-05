import os
from input_loader import *
from helpers import *

input = load_input_str(os.path.basename(__file__)[:-3])

example = """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4"""

def block_to_ranges(block:str):
    block_lines = block.splitlines()
    ranges = []

    for line in block_lines[1:]:
        line_nums = list(map(int, line.split()))
        #des_range = range(line_nums[0], line_nums[2])
        source_range = range(line_nums[1], line_nums[1]+line_nums[2])
        offset = line_nums[0] - line_nums[1]
        ranges.append([source_range, offset])

    return ranges

def source_to_dest(input, map_lines):
    for map in map_lines:
        source = map[0]
        offset = map[1]
        if input in source:
            return input + offset

    return input

def calc_part1(input):

    locations = []
    blocks = input.split("\n\n")

    initial_seeds = list(map(int, blocks[0][7:].split()))

    seed_to_soil = block_to_ranges(blocks[1])
    soil_to_fertilizer = block_to_ranges(blocks[2])
    fertilizer_to_water = block_to_ranges(blocks[3])
    water_to_light = block_to_ranges(blocks[4])
    light_to_temp = block_to_ranges(blocks[5])
    temo_to_humiditiy = block_to_ranges(blocks[6])
    humidity_to_location = block_to_ranges(blocks[7])


    maps = [
        seed_to_soil,
        soil_to_fertilizer,
        fertilizer_to_water,
        water_to_light,
        light_to_temp,
        temo_to_humiditiy,
        humidity_to_location
    ]

    for initial_seed in initial_seeds:
        value = initial_seed
        for maping in maps:
            value = source_to_dest(value, maping)

        locations.append(value)

    return min(locations)




def part1():
    erg = calc_part1(example.strip())
    print(f"Example Part 1: {erg}")
    assert erg == 35
    print(f"Result Part 1: {calc_part1(input)}")



def source_to_dest2(input_ranges:set, map_lines):

    output_ranges = []
    while input_ranges:
        input_range = input_ranges.pop()
        for maping in map_lines:
            source = maping[0]
            offset = maping[1]
            if input_range.start in source:
                if len(input_range) <= len(source):
                    output_ranges.append(range(input_range.start+offset, input_range.stop + offset))
                else:
                    # len(input_range) > len(source)
                    output_range = range(input_range.start+offset, source.stop + offset)
                    output_ranges.append(output_range)
                    remaining_input = range(source.stop, input_range.stop)
                    input_ranges.add(remaining_input)
                break
            elif source.start in input_range:
                remaining_input = range(input_range.start, source.start)
                input_ranges.add(remaining_input)
                if source.stop >= input_range.stop:
                    output_range = range(source.start + offset, input_range.stop+offset)
                    output_ranges.append(output_range)
                else:
                    output_range = range(source.start + offset, source.stop + offset)
                    output_ranges.append(output_range)
                    remaining_input = range(source.stop, input_range.stop)
                    input_ranges.add(remaining_input)
                break

        else:
            output_ranges.append(input_range)



    return set(output_ranges)
def calc_part2(input):
    location_min = 100_000_000_000
    blocks = input.split("\n\n")

    initial_seeds_ = list(map(int, blocks[0][7:].split()))
    initial_seeds = []
    for start, length in grouped(initial_seeds_, 2):
        initial_seeds.append(range(start, start+length))



    seed_to_soil = block_to_ranges(blocks[1])
    soil_to_fertilizer = block_to_ranges(blocks[2])
    fertilizer_to_water = block_to_ranges(blocks[3])
    water_to_light = block_to_ranges(blocks[4])
    light_to_temp = block_to_ranges(blocks[5])
    temo_to_humiditiy = block_to_ranges(blocks[6])
    humidity_to_location = block_to_ranges(blocks[7])

    maps = [
        seed_to_soil,
        soil_to_fertilizer,
        fertilizer_to_water,
        water_to_light,
        light_to_temp,
        temo_to_humiditiy,
        humidity_to_location
    ]

    set_of_target_ranges = set(initial_seeds)
    for maping in maps:
        set_of_target_ranges = source_to_dest2(set_of_target_ranges, maping)

    location_min = min([loc_range.start for loc_range in set_of_target_ranges])

    return location_min

def part2():
    erg = calc_part2(example)
    print(f"Example Part 2: {erg}")
    assert erg == 46
    print(f"Result Part 2: {calc_part2(input)}")
