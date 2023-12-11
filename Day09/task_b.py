#!/usr/bin/env python3
import os

script_dir = os.path.dirname(os.path.realpath(__file__))

# test_data_path = f"{script_dir}/data_task_a"
# test_data_path = f"{script_dir}/data_task_a_test"
test_data_path = f"{script_dir}/data_task_b"
# test_data_path = f"{script_dir}/data_task_b_test"

file = open(test_data_path)


def check_all_zeroes(values):
    for v in values:
        if v != 0:
            return False
    return True


def extrapolate(values):
    print("------------------")
    value_matrix = list()  # definitly not a matrix... but sounds fancy
    value_matrix.append(values)
    # print(values)
    # next_values = [values[i+1] - values[i] for i in range(len(values)-1)]
    # print(next_values)

    while not check_all_zeroes(value_matrix[-1]):
        next_values = [
            value_matrix[-1][i + 1] - value_matrix[-1][i]
            for i in range(len(value_matrix[-1]) - 1)
        ]
        value_matrix.append(next_values)
    for values in value_matrix:
        print(values)
    print("------------------")
    print("Extrapolating:")
    value_matrix[-1] = [0] + value_matrix[-1]
    for i in range(1, len(value_matrix) + 1):
        index = len(value_matrix) - i
        diff_value = value_matrix[index][0]
        value_matrix[index - 1] = [
            value_matrix[index - 1][0] - diff_value
        ] + value_matrix[index - 1]
        print(value_matrix[index])
    print("------------------")
    return value_matrix[0][0]


sum_of_extrapolated = 0
for l in file:
    # print(l.strip())
    values = [int(x) for x in l.split()]
    # print(values)
    sum_of_extrapolated += extrapolate(values)
    # break

print(f"sum_of_extrapolated: {sum_of_extrapolated}")
