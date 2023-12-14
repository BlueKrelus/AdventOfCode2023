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
    # print(m)
    # h
    # print("Columns:\n")
    # min_pos = 0
    # max_pos = len(m[0])
    # for i in range(max_pos):
    #     print("")
    #     print(i)
    #     print(get_column(m, i))
    #     for j in range(min([i+i, max_pos])):
    #         print(get_column(m, j))

    # if (get_column(m, i) == get_column(m, i+1)):
    #     print("True")

    # v

    # print(m)

    # print("Rows:\n")

    for i in range(1, len(m)):
        first_part = m[:i]
        mirror = True
        for a, b in zip(first_part[::-1], m[i:]):
            # print(f"a {a}")
            # print(f"b {b}")
            if a != b:
                mirror = False
                break
        if mirror:
            print(f">>> r {i}")
            return i * 100
            # print(get_row(m, i))
        # print("-------------")
        # input()

    r_m = rotate(m)

    for i in range(1, len(r_m)):
        first_part = r_m[:i]
        mirror = True
        for a, b in zip(first_part[::-1], r_m[i:]):
            # print(f"a {a}")
            # print(f"b {b}")
            if a != b:
                mirror = False
                break
        if mirror:
            print(f">>> c {i}")
            return i
            # print(get_row(m, i))
        # print("-------------")
        # input()


sum = 0

for m in matrix_matrix:
    print("-------------")
    print(m)
    print("-------------")
    sum = sum + find_reflection(m)
    # break


print(f"sum {sum}")
