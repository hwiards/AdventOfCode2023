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


def block_to_ranges(block: str):
    block_lines = block.splitlines()
    ranges = []

    for line in block_lines[1:]:
        line_nums = list(map(int, line.split()))
        source_range = range(line_nums[1], line_nums[1] + line_nums[2])
        offset = line_nums[0] - line_nums[1]
        ranges.append([source_range, offset])

    return ranges


def source_to_dest(input_location, map_lines):
    for mapping in map_lines:
        source = mapping[0]
        offset = mapping[1]
        if input_location in source:
            return input_location + offset

    return input_location


def calc_part1(input):
    locations = []
    blocks = input.split("\n\n")
    initial_seeds = list(map(int, blocks[0][7:].split()))

    maps = [block_to_ranges(block) for block in blocks[1:]]

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


def source_to_dest2(input_ranges: set, map_lines):
    output_ranges = []
    while input_ranges:
        input_range = input_ranges.pop()
        for maping in map_lines:
            source = maping[0]
            offset = maping[1]

            if input_range.start in source:
                if len(input_range) <= len(source):
                    # Full range maps
                    output_ranges.append(range(input_range.start + offset, input_range.stop + offset))
                else:
                    # len(input_range) > len(source)
                    # start of input maps until end of source range, add remaining range to input
                    output_range = range(input_range.start + offset, source.stop + offset)
                    output_ranges.append(output_range)
                    remaining_input = range(source.stop, input_range.stop)
                    input_ranges.add(remaining_input)
                break
            elif source.start in input_range:
                # inputs starts before the source, add remaining range of the front to the input range
                remaining_input = range(input_range.start, source.start)
                input_ranges.add(remaining_input)
                if source.stop >= input_range.stop:
                    # input end completely fully in the source range
                    output_range = range(source.start + offset, input_range.stop + offset)
                    output_ranges.append(output_range)
                else:
                    # It does not fit completely in the source range, add remaining to input ranges
                    output_range = range(source.start + offset, source.stop + offset)
                    output_ranges.append(output_range)
                    remaining_input = range(source.stop, input_range.stop)
                    input_ranges.add(remaining_input)
                break

        else:
            # No mapping does fit, therefore it maps n->n to the output
            output_ranges.append(input_range)

    # use sets to filter duplicate ranges
    return set(output_ranges)


def calc_part2(input):
    blocks = input.split("\n\n")

    initial_seeds = list(map(int, blocks[0][7:].split()))
    initial_seeds = [range(start, start + length) for start, length in grouped(initial_seeds, 2)]

    maps = [block_to_ranges(block) for block in blocks[1:]]

    set_of_target_ranges = set(initial_seeds)
    for mapping in maps:
        set_of_target_ranges = source_to_dest2(set_of_target_ranges, mapping)

    location_min = min([loc_range.start for loc_range in set_of_target_ranges])

    return location_min


def part2():
    erg = calc_part2(example)
    print(f"Example Part 2: {erg}")
    assert erg == 46
    print(f"Result Part 2: {calc_part2(input)}")
