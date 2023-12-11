#!/usr/bin/env python3
import os

import time

script_dir = os.path.dirname(os.path.realpath(__file__))

from multiprocessing import Pool

# test_data_path = f"{script_dir}/data_task_a"
# test_data_path = f"{script_dir}/data_task_a_test"
# test_data_path = f"{script_dir}/data_task_a_test2"
test_data_path = f"{script_dir}/data_task_b"
# test_data_path = f"{script_dir}/data_task_b_test"

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

class Job:
    step = 0
    start_key = ""
    current_key = ""
    max_step = -1
    def __init__(self, start_key):
        self.start_key = start_key
        self.current_key = start_key
    def __str__(self) -> str:
        return f"start_key: {self.start_key}, current_key: {self.current_key}, step: {self.step}"
    def __repr__(self) -> str:
        return self.__str__()
    

def func(job):
    # print(f"job.max_step: {job.max_step}")
    # print(f"job.step: {job.step}")
    if job.step == job.max_step:
        return job
    #  = job.current_key
    step = job.step

    skip = True
    while skip or job.current_key[-1] != "Z":
        skip = False
        direction = directions[get_step(job.step)]
        if direction == 'L':
            job.current_key = the_map[job.current_key][0]
        else:
            job.current_key = the_map[job.current_key][1]
        # print(current_key)
        job.step += 1

    # print(step)
    return job

map_steps = dict()

print("----------------------------------")

# for start in start_list:
#     print(start)
#     print(func(start, 0))



        
job_list = list()

for x in start_list:
    job_list.append(Job(x))

steps_equals = False
max_step = -1

pool = Pool(processes=len(job_list))

while not steps_equals:
    # for job in job_list:
    #     # if job.step == max_step:
    #     #     continue
    #     job.max_step = max_step
    #     job = func(job)
    #     # job.current_key = res[0]
    #     # job.step = res[1]
    #     if max_step < job.step:
    #         max_step = job.step

    job_list = pool.map(func, job_list)

    for job in job_list:
        if max_step < job.step:
            max_step = job.step

    steps_equals = True
    print("----------------------------------")
    for job in job_list:
        print(job)
        job.max_step = max_step
        if max_step != job.step:
            steps_equals = False
    print(steps_equals)
    print(f"max_step: {max_step}")
    # time.sleep(2)
    print("----------------------------------")        

    

    break

print("---------------DONE---------------")

hmm=1
for job in job_list:
    print(job)
    hmm = hmm * job.step

print(hmm)

# start = start_list[1]
# print(start)
# result = func(start, 0)
# print(result)
# print(type(result))
# result = func(result[0], result[1])
# print(result)
