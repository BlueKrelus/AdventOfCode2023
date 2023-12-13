#!/usr/bin/env python3
import os

script_dir = os.path.dirname(os.path.realpath(__file__))

# test_data_path = f"{script_dir}/data_task_a"
test_data_path = f"{script_dir}/data_task_a_test"
# test_data_path = f"{script_dir}/data_task_b"
# test_data_path = f"{script_dir}/data_task_b_test"

file = open(test_data_path)

raw_data = ""

matrix_matrix = list()

for l in file:
    print(l, end="")
    if len(l) == 1:
        matrix_matrix.append(raw_data)
        raw_data = ""
    raw_data += l
matrix_matrix.append(raw_data.lstrip())

# print(matrix_matrix)
# print(matrix_matrix[0])

def get_row(m, y):
    print(f">{m[y]}")
    return m[y]

def get_column(m, x):
    column = ""
    for y in range(len(m)):
        column += m[y][x]
    return column

def find_reflextion(m):
    # h
    # for i in range(len(m[0])):
    #     print(get_column(m, i))

    # v

    print(m)

    for i in range(len(m)):
        get_row(m, i)
        input()



for m in matrix_matrix:
    print("-------------")
    print(m)
    print("-------------")
    find_reflextion(m)
    break
