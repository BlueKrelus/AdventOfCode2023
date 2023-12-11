#!/usr/bin/env python3
import os

script_dir = os.path.dirname(os.path.realpath(__file__))

test_data_path = f"{script_dir}/data_task_a"
# test_data_path = f"{script_dir}/data_task_a_test"
# test_data_path = f"{script_dir}/data_task_b"
# test_data_path = f"{script_dir}/data_task_b_test"

file = open(test_data_path)

max_cubes = {
    "red": 12,
    "green": 13,
    "blue": 14,
}

sum_of_power_value = 0


for l in file:
    l = l.strip()
    game = int(l.split(":")[0].split(" ")[1])
    sets = l.split(":")[1].split(";")
    print(f"Game: {game}")
    print(sets)
    game_valid = True
    cubes = dict()
    for s in sets:
        print(s)
        cubes_raw = s.split(",")
        # print(cubes_raw)
        for c in cubes_raw:
            d = c.strip().split(" ")
            if d[1] not in cubes.keys():
                cubes[d[1]] = 0
            if cubes[d[1]] < int(d[0]):
                cubes[d[1]] = int(d[0])

    print(cubes)
    power_value = 1
    for v in [int(cubes[k]) for k in cubes.keys()]:
        power_value = power_value * v
    print(power_value)
    print("----------------")
    sum_of_power_value += power_value
    # break
print(f"Sum of power values: {sum_of_power_value}")
