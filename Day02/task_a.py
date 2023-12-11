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

sum_of_game_id = 0

def check_cubes_valid(cubes, max_cubes):
    for k in cubes.keys():
        if cubes[k] > max_cubes[k]:
            return False
    return True

for l in file:
    l = l.strip()
    game = int(l.split(":")[0].split(" ")[1])
    sets = l.split(":")[1].split(";")
    print(f"Game: {game}")
    print(sets)
    game_valid = True
    for s in sets:
        print(s)
        cubes_raw = s.split(",")
        # print(cubes_raw)
        cubes = dict()
        for c in cubes_raw:
            d = c.strip().split(" ")
            if d[1] not in cubes.keys():
                cubes[d[1]] = 0
            cubes[d[1]] = cubes[d[1]] + int(d[0])
        print(cubes)
        if not check_cubes_valid(cubes, max_cubes):
            game_valid = False
            break

    if(game_valid):
        print(f"Game: {game}, is valid")
        sum_of_game_id += game
    else:
        print(f"Game: {game}, is not valid")
    print("----------------")
    # break
print(f"Sum of valid game ids: {sum_of_game_id}")
