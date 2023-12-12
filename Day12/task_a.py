#!/usr/bin/env python3
import os
import re

script_dir = os.path.dirname(os.path.realpath(__file__))

test_data_path = f"{script_dir}/data_task_a"
# test_data_path = f"{script_dir}/data_task_a_test"
# test_data_path = f"{script_dir}/data_task_a_test2"
# test_data_path = f"{script_dir}/data_task_b"
# test_data_path = f"{script_dir}/data_task_b_test"

file = open(test_data_path)


def validate(line, number_list):
    new_numlist = [len(x) for x in line.split(".") if len(x) > 0]
    # print(f"> {new_numlist} {number_list}" )
    if new_numlist == number_list:
        return True
    return False


def iterate(line, number_list):
    question_line = line.replace(".", "").replace("#", "")
    length = len(question_line)
    map_line = line.split()[0]
    print(map_line)
    # print(pow(2, length) - 1)
    num_variations = 0
    for i in range(pow(2, length)):
        # print(i)
        bin_line = str(bin(i)).split('b')[1].rjust(length, '0')
        # print(bin_line)
        index = 0
        new_line = ""
        for c in map_line:
            if c == '?':
                if bin_line[index] == '0':
                    new_line += '.'
                else:
                    new_line += '#'
                index += 1
            else:
                new_line += c
        # print(new_line)
        if validate(new_line, number_list):
            print(new_line)
            num_variations += 1
    return num_variations




# bin_line = str(bin(53)).split('b')[1]
# print(bin_line)


# validate(".###.##.#...", None)

# exit()

total_num_variations = 0
for l in file:
    print("--------------------")
    l = l.strip()
    print(l)
    print("--------------------")

    map_list = [x for x in re.split("(\?+|\.+|#+)", l.split()[0]) if len(x) > 0]
    print(map_list)
    number_list = [int(x) for x in l.split()[1].split(",")]
    print(number_list)
    print()
    print("-+-+-+-+-+-+-+")
    variations = iterate(l.split()[0], number_list)
    total_num_variations += variations

    print(f"variations {variations}")

print("-----------------------------------------------")
print(f"total: {total_num_variations}")
