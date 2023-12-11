#!/usr/bin/env python3
import os

script_dir = os.path.dirname(os.path.realpath(__file__))

# test_data_path = f"{script_dir}/data_task_a"
test_data_path = f"{script_dir}/data_task_a_test"
# test_data_path = f"{script_dir}/data_task_b"
# test_data_path = f"{script_dir}/data_task_b_test"

file = open(test_data_path)

total = 0

for l in file:
    first_digit = None
    second_digit = None
    l = l.strip()
    # print(l)
    for c in l:
        if str(c).isdigit():
            first_digit = c
            break
    for c in l[::-1]:
        if str(c).isdigit():
            second_digit = c
            break
    print(f"{first_digit}{second_digit}")
    total = total + int(f"{first_digit}{second_digit}")


print(f"calibration value: {total}")
