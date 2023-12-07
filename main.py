import sys

import solutions

#for day_name, day in solutions.days.items():
#    print(f"Executing {day_name}")
#    day.part1()
#    day.part2()

def execute(day_name = None):
    if day_name:
        day = solutions.days[day_name]
    else:
        day_keys = sorted(solutions.days.keys(), reverse=True)
        day = solutions.days[day_keys[0]]

    day.part1()
    day.part2()

if __name__ == '__main__':

    arguments = sys.argv
    if len(arguments) == 1:
        # no argument
        execute()
    else:
        execute(day_name= sys.argv[1])