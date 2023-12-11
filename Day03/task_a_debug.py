#!/usr/bin/env python3
import os
from colorama import Fore, Back, Style

script_dir = os.path.dirname(os.path.realpath(__file__))

test_data_path = f"{script_dir}/data_task_a"
# test_data_path = f"{script_dir}/data_task_a_test"
# test_data_path = f"{script_dir}/data_task_b"
# test_data_path = f"{script_dir}/data_task_b_test"

file = open(test_data_path)

schematic = list()

def print_schematic():
    for s in schematic:
        print(s)

def get_at(x, y):
    try:
        return schematic[y][x]
    except Exception:
        return None

def get_int_at(x, y):
    try:
        return int(schematic[x][y])
    except Exception:
        return None

def check_neighbours(start, end, level):
    for x in range(start-1, end+2):
        for y in range(level-1, level+2):
            value = get_at(x,y)
            if value is None:
                continue
            if value.isdigit():
                continue
            if value == '.':
                continue
            return True
    return False

def get_subpart(start,end, level):
    return schematic[level][start:end+1]


for l in file:
    # print(l)
    schematic.append(l.strip())

width = len(schematic[0])
height = len(schematic)

print_schematic()

print("---------------------")
total_sum = 0
for y in range(height):
    value_string = ""
    start = -1
    end = -1
    found_digit = False
    for x in range(width+1):
        value = get_at(x,y)
        # print(value)
        if value is not None and value.isdigit():
            if not found_digit:
                start = x
                found_digit = True
            end = x
            if end < x:
                start = x
            # else
            # continue
        else:
            if found_digit:
                found_digit = False
                digits = int(get_subpart(start, end, y))
                if check_neighbours(start, end, y):
                    print(Fore.GREEN, end="")
                    print(digits, end="")
                    print(Style.RESET_ALL, end="")
                    total_sum += digits
                else:
                    print(Fore.RED, end="")
                    print(digits, end="")
                    print(Style.RESET_ALL, end="")
            print(value, end="")
    print("")

print("----------------")
print(f"Total sum: {total_sum}")
