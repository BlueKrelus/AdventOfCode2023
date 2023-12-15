#!/usr/bin/env python3
import os

script_dir = os.path.dirname(os.path.realpath(__file__))

test_data_path = f"{script_dir}/data_task_a"
# test_data_path = f"{script_dir}/data_task_a_test"
# test_data_path = f"{script_dir}/data_task_b"
# test_data_path = f"{script_dir}/data_task_b_test"

file = open(test_data_path)

command_list = list()

for l in file:
    print(l)
    command_list += l.split('\n')[0].split(',')

print(command_list)

# for c in command_list:
#     print(c)

def calc_hash(word):
    current_value = 0
    for c in word:
        current_value += ord(c)
        current_value *= 17
        current_value = current_value % 256
    return current_value

test_word = 'HASH'
hash = calc_hash(test_word)
print(f"{test_word}: {hash}")

sum_hash = 0
for c in command_list:
    hash = calc_hash(c)
    print(f"{c} : {hash}")
    sum_hash += hash

print(f"Sum of hashes: {sum_hash}")
