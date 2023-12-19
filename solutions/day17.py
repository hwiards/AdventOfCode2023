import os
from input_loader import load_input_str
from helpers import *

from heapq import heappop, heappush

input_str = load_input_str(os.path.basename(__file__)[:-3])

example = """2413432311323
3215453535623
3255245654254
3446585845452
4546657867536
1438598798454
4457876987766
3637877979653
4654967986887
4564679986453
1224686865563
2546548887735
4322674655533
"""

DIRS = [(0,1), (1,0), (0,-1), (-1,0)]

def getheat(grid, row, col, dr, dc):
    if 0 <= row+dr < len(grid) and 0 <= col+dc < len(grid[0]):
        return int(grid[row+dr][col+dc])
    return None


def calc_part1(input_str):

    grid = input_str.splitlines()

    # heatlevel, position, direction (rows, cols), steps in dir
    start = (0,0)
    start_dir = (0,1)
    steps = 0
    heat = 0
    heap = [(heat, start, start_dir, steps)]
    heappush(heap, (heat, start, (1,0), steps))

    visited = {
        ((start, start_dir, steps)) : heat
    }

    while heap:
        cur_heat, (cur_row, cur_col), (cur_dr, cur_dc), steps = heappop(heap)
        if (cur_row, cur_col) == (len(grid) - 1, len(grid[0]) - 1):
            continue

        for (dr, dc) in DIRS:
            neighbour_heat = getheat(grid, cur_row, cur_col, dr, dc)
            if neighbour_heat is not None:
                if ((dr, dc) == (cur_dr, cur_dc) and steps == 3) or (dr, dc) == (cur_dr*-1, cur_dc*-1):
                    continue
                if (dr, dc) == (cur_dr, cur_dc):
                    new_steps = steps + 1
                else:
                    new_steps = 1

                act_neighbour_heat_loss = visited.get(((cur_row+dr, cur_col+dc), (dr, dc), new_steps), float('inf'))

                if cur_heat + neighbour_heat < act_neighbour_heat_loss:
                    visited[((cur_row+dr, cur_col+dc), (dr, dc), new_steps)] = cur_heat + neighbour_heat
                    heappush(heap, (cur_heat+neighbour_heat, (cur_row+dr, cur_col+dc), (dr, dc), new_steps))

    ends = [hl for ((x, y), _, _), hl in visited.items() if (x, y) == (len(grid) - 1, len(grid[0]) - 1)]
    ans = min(ends)
    return ans


def part1():
    erg = calc_part1(example.strip())
    print(f"Example Part 1: {erg}")
    assert erg == 102
    print(f"Result Part 1: {calc_part1(input_str)}")


def calc_part2(input_str):
    grid = input_str.splitlines()

    # heatlevel, position, direction (rows, cols), steps in dir
    start = (0,0)
    start_dir = (0,1)
    steps = 0
    heat = 0
    heap = [(heat, start, start_dir, steps)]
    heappush(heap, (heat, start, (1,0), steps))
    visited = {
        ((start, start_dir, steps)) : heat
    }

    while heap:
        cur_heat, (cur_row, cur_col), (cur_dr, cur_dc), steps = heappop(heap)
        if (cur_row, cur_col) == (len(grid) - 1, len(grid[0]) - 1):
            continue

        for (dr, dc) in DIRS:
            neighbour_heat = getheat(grid, cur_row, cur_col, dr, dc)
            if neighbour_heat is not None:
                if ((dr, dc) == (cur_dr, cur_dc) and steps == 10) or (dr, dc) == (cur_dr*-1, cur_dc*-1):
                    continue

                if steps < 4 and (dr, dc) != (cur_dr, cur_dc):
                    continue


                if (dr, dc) == (cur_dr, cur_dc):
                    new_steps = steps + 1
                else:
                    new_steps = 1

                act_neighbour_heat_loss = visited.get(((cur_row+dr, cur_col+dc), (dr, dc), new_steps), float('inf'))

                if cur_heat + neighbour_heat < act_neighbour_heat_loss:
                    visited[((cur_row+dr, cur_col+dc), (dr, dc), new_steps)] = cur_heat + neighbour_heat
                    heappush(heap, (cur_heat+neighbour_heat, (cur_row+dr, cur_col+dc), (dr, dc), new_steps))

    ends = [hl for ((x, y), _, _), hl in visited.items() if (x, y) == (len(grid) - 1, len(grid[0]) - 1)]
    ans = min(ends)
    return ans

def part2():
    erg = calc_part2(example)
    print(f"Example Part 2: {erg}")
    #assert erg == 467835
    print(f"Result Part 2: {calc_part2(input_str)}")
