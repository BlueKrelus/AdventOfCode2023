#!/usr/bin/env python3
import os

# from collections import deque

script_dir = os.path.dirname(os.path.realpath(__file__))

test_data_path = f"{script_dir}/data_task_a"
# test_data_path = f"{script_dir}/data_task_a_test"
# test_data_path = f"{script_dir}/data_task_b"
# test_data_path = f"{script_dir}/data_task_b_test"

file = open(test_data_path)

command_list = list()

for l in file:
    # print(l)
    command_list += l.split("\n")[0].split(",")

# print(command_list)

# for c in command_list:
#     print(c)


def calc_hash(word):
    current_value = 0
    for c in word:
        current_value += ord(c)
        current_value *= 17
        current_value = current_value % 256
    return current_value


# test_word = 'HASH'
# hash = calc_hash(test_word)
# print(f"{test_word}: {hash}")

# sum_hash = 0
# for c in command_list:
#     hash = calc_hash(c)
#     print(f"{c} : {hash}")
#     sum_hash += hash


class HASH_MAP:
    def __init__(self) -> None:
        self.hash_map = list()
        for i in range(256):
            self.hash_map.append(list())

    def __getitem__(self, key):
        if type(key) == type(42):
            return self.hash_map[key]
        return self.hash_map[calc_hash(key)]

    def __setitem__(self, key, value):
        self.hash_map[calc_hash(key)] = value

    def __len__(self):
        return len(self.hash_map)

    def keys(self):
        return [x for x in range(256) if len(self.hash_map[x]) > 0]

    def print_out(self):
        for i in range(len(self.hash_map)):
            if len(self.hash_map[i]) > 0:
                print(f"{i} : {self.hash_map[i]}")


my_hash_map = HASH_MAP()
# print(my_hash_map)

for c in command_list:
    # print(c)
    if "=" in c:
        label = c.split("=")[0]
        value = int(c.split("=")[1])
        # print(f"{c}    =")
        # print(label)
        added = False
        for i in range(len(my_hash_map[label])):
            if label in my_hash_map[label][i]:
                my_hash_map[label][i][1] = value
                added = True
                break
        if not added:
            my_hash_map[label].append([label, value])
    if "-" in c:
        pass
        label = c.split("-")[0]
        # print(f"{c}    -")

        for i in range(len(my_hash_map[label])):
            if label in my_hash_map[label][i]:
                print(my_hash_map[label])
                # input()
                my_hash_map[label].pop(i)
                print(my_hash_map[label])
                # input()
                break


# print(f"Sum of hashes: {sum_hash}")

total_focus_power = 0

my_hash_map.print_out()

for k in my_hash_map.keys():
    print(f"{k} : {my_hash_map[k]}")
    for j in range(len(my_hash_map[k])):
        focus_power = (k + 1) * (j + 1) * my_hash_map[k][j][1]
        print(focus_power)
        total_focus_power += focus_power

print(f"total focus power: {total_focus_power}")
