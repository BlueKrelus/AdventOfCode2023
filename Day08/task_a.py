#!/usr/bin/env python3
import os

script_dir = os.path.dirname(os.path.realpath(__file__))

test_data_path = f"{script_dir}/data_task_a"
# test_data_path = f"{script_dir}/data_task_a_test"
# test_data_path = f"{script_dir}/data_task_a_test2"
# test_data_path = f"{script_dir}/data_task_b"
# test_data_path = f"{script_dir}/data_task_b_test"

file = open(test_data_path)

directions = None

the_map = dict()

for l in file:
    print(l)
    l = l.strip()
    if len(l) == 0:
        continue
    if "=" not in l:
        directions = l
        continue
    key = l.split("=")[0].strip()
    cords = [
        x.strip() for x in l.split("=")[1].replace("(", "").replace(")", "").split(",")
    ]
    the_map[key] = cords
    # break

print(directions)
print(the_map)


def mod(a, b):
    return abs(a)%abs(b)*(1,-1)[a<0]

def get_step(step):
    return mod(step,len(directions))


print("----------------------------------")

start = "AAA"

current_key = start

step = 0
while current_key != "ZZZ":
    direction = directions[get_step(step)]
    if direction is 'L':
        current_key = the_map[current_key][0]
    else:
        current_key = the_map[current_key][1]
    print(current_key)
    step += 1

print(step)
