#!/usr/bin/env python3
import os

import time

script_dir = os.path.dirname(os.path.realpath(__file__))

# test_data_path = f"{script_dir}/data_task_a"
# test_data_path = f"{script_dir}/data_task_a_test"
# test_data_path = f"{script_dir}/data_task_a_test2"
test_data_path = f"{script_dir}/data_task_b"
test_data_path = f"{script_dir}/data_task_b_test"

file = open(test_data_path)

directions = None

the_map = dict()

for l in file:
    # print(l)
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

# print(directions)
# print(the_map)


def mod(a, b):
    return abs(a)%abs(b)*(1,-1)[a<0]

def get_step(step):
    return mod(step,len(directions))


print("----------------------------------")

start_list = sorted([x for x in the_map.keys() if x[-1] == 'A' ])


print(start_list)

# exit()

def func(start_key, step):
    current_key = start_key
    skip = True

    while skip or current_key[-1] != "Z":
        skip = False
        direction = directions[get_step(step)]
        if direction == 'L':
            current_key = the_map[current_key][0]
        else:
            current_key = the_map[current_key][1]
        # print(current_key)
        step += 1

    print(step)
    return current_key, step

map_steps = dict()

print("----------------------------------")

# for start in start_list:
#     print(start)
#     print(func(start, 0))



class Job:
    step = 0
    start_key = ""
    current_key = ""
    def __init__(self, start_key):
        self.start_key = start_key
        self.current_key = start_key
    def __str__(self) -> str:
        return f"start_key: {self.start_key}, current_key: {self.current_key}, step: {self.step}"
    def __repr__(self) -> str:
        return self.__str__()
        
job_list = list()

for x in start_list:
    job_list.append(Job(x))

steps_equals = False
max_step = -1

while not steps_equals:
    for job in job_list:
        if job.step == max_step:
            continue
        res = func(job.current_key, job.step)
        job.current_key = res[0]
        job.step = res[1]
        if max_step < job.step:
            max_step = job.step

    steps_equals = True
    for job in job_list:
        print(job)
        if max_step != job.step:
            steps_equals = False
    print(steps_equals)
    print(max_step)
    # time.sleep(1)
    print("----------------------------------")        

    

    # break

print("----------------------------------")

for job in job_list:
    print(job)


# start = start_list[1]
# print(start)
# result = func(start, 0)
# print(result)
# print(type(result))
# result = func(result[0], result[1])
# print(result)
