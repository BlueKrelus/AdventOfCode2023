#!/usr/bin/env python3
import os

script_dir = os.path.dirname(os.path.realpath(__file__))

test_data_path = f"{script_dir}/data_task_a"
# test_data_path = f"{script_dir}/data_task_a_test"
# test_data_path = f"{script_dir}/data_task_b"
# test_data_path = f"{script_dir}/data_task_b_test"

file = open(test_data_path)

raw_data = ""

matrix_matrix = list()

for l in file:
    # print(l, end="")
    if len(l) == 1:
        matrix_matrix.append(raw_data)
        raw_data = ""
    raw_data += l
matrix_matrix.append(raw_data.lstrip())

# print(matrix_matrix)
# print(matrix_matrix[0])


def get_row(m, y):
    # print(f">{m[y]}")
    return m[y]


def get_column(m, x):
    column = ""
    for y in range(len(m)):
        column += m[y][x]
    return column


def rotate(m):
    r_m = list()
    for i in range(len(m[0])):
        r_m.append(get_column(m, i))
    return r_m


def find_reflection(m):
    m = [x for x in m.split("\n") if len(x) > 0]

    for i in range(1, len(m)):
        first_part = m[:i]
        smudge_cnt = 0
        for a, b in zip(first_part[::-1], m[i:]):
            if a != b:
                for aa, bb in zip(a, b):
                    if aa != bb:
                        smudge_cnt += 1
        print(f"smudge_cnt {smudge_cnt}")
        if smudge_cnt == 1:
            print(f">>> c {i}")
            return i * 100

    r_m = rotate(m)

    for i in range(1, len(r_m)):
        first_part = r_m[:i]
        smudge_cnt = 0
        for a, b in zip(first_part[::-1], r_m[i:]):
            if a != b:
                for aa, bb in zip(a, b):
                    if aa != bb:
                        smudge_cnt += 1
        print(f"smudge_cnt {smudge_cnt}")
        if smudge_cnt == 1:
            print(f">>> c {i}")
            return i
    return 0


sum = 0

for m in matrix_matrix:
    print("-------------")
    print(m)
    print("-------------")
    sum = sum + find_reflection(m)

print(f"sum {sum}")
