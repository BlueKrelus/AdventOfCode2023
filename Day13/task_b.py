#!/usr/bin/env python3
import os

script_dir = os.path.dirname(os.path.realpath(__file__))

# test_data_path = f"{script_dir}/data_task_a"
test_data_path = f"{script_dir}/data_task_a_test"
# test_data_path = f"{script_dir}/data_task_b"
# test_data_path = f"{script_dir}/data_task_b_test"

file = open(test_data_path)

for l in file:
    print(l)