#!/usr/bin/env python3
import os
import re

script_dir = os.path.dirname(os.path.realpath(__file__))

# test_data_path = f"{script_dir}/data_task_a"
# test_data_path = f"{script_dir}/data_task_a_test"
test_data_path = f"{script_dir}/data_task_b"
# test_data_path = f"{script_dir}/data_task_b_test"
# test_data_path = f"{script_dir}/problem_data"

file = open(test_data_path)

keys = [
    ["zero","0"],
    ["one", "1"],
    ["two", "2"],
    ["three", "3"],
    ["four", "4"],
    ["five", "5"],
    ["six", "6"],
    ["seven", "7"],
    ["eight", "8"],
    ["nine", "9"],
]


total = 0


def get_index(line, keys, min=True):
    indexes = [m.start() for m in re.finditer(keys[1], line)] + [m.start() for m in re.finditer(keys[0], line)]
    print(indexes)

    if len(indexes) == 0:
        return None
    return indexes
#[0, 5, 10, 15]
    result = list()
    index = None
    # while(index)
    for i in range(0, len(line)):
        c_line = line[i:]
        for key in keys:
            try:
                result.append(c_line.index(key))
            except Exception:
                pass
    if len(result) == 0:
        return None
    return result


for l in file:
    first_digit = None
    second_digit = None
    l = l.strip()
    print(l)

    index_map_min= dict()
    index_map_max= dict()
    for k in keys:
        digit = k[1]
        index = get_index(l, k)
        if index != None:
            # if index_map[index] is None:
            #     index_map[index] = list()
            print(f"{digit} at {index}")
            index_map_min[min(index)] = digit
            index_map_max[max(index)] = digit

    print(index_map_min)
    print(index_map_max)
    # break
    first_digit = index_map_min[min(index_map_min.keys())]
    second_digit = index_map_max[max(index_map_max.keys())]
    print(f"{first_digit}{second_digit}")
    total = total + int(f"{first_digit}{second_digit}")
    # if len(index_map) == 1:
    #     break
    # break


print(f"calibration value: {total}")
