#!/usr/bin/env python3
import os

script_dir = os.path.dirname(os.path.realpath(__file__))

test_data_path = f"{script_dir}/data_task_a"
# test_data_path = f"{script_dir}/data_task_a_test"
# test_data_path = f"{script_dir}/data_task_b"
# test_data_path = f"{script_dir}/data_task_b_test"

file = open(test_data_path)

stone_platform = list()


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


for l in file:
    l = l.strip()
    stone_platform.append(l)
    # print(l)

# print("-----------------------")

# for l in stone_platform:
#     print(l)

stone_platform = rotate(stone_platform)

# print("-----------------------")

# for l in stone_platform:
#     print(l)

tilted_to_north_platform = list()

print("--------------------------")
# print()

for line in stone_platform:
    # print(f"<{line}")
    length = len(line)
    segments = line.split("#")
    new_line = ""
    # if line[0] == "#":
    #     new_line += "#"
    for segment in segments:
        stones = segment.replace(".", "")
        empty = segment.replace("O", "")
        new_line += stones
        new_line += empty
        new_line += "#"
    if len(new_line) > length:
        new_line = new_line[:-1]
    # print(f">{new_line}")
    tilted_to_north_platform.append(new_line)
    # break

tilted_to_north_platform = rotate(tilted_to_north_platform)
print("Tilted to north:")

for l in tilted_to_north_platform:
    print(l)

# exit()

total_stress = 0

print("-------------")
for x in range(len(tilted_to_north_platform[0])):
    column = get_column(tilted_to_north_platform, x)
    # print(column)
    stress = 0
    for i in range(len(column)):
        if column[::-1][i] == "O":
            print(i + 1)
            stress += i + 1
    print(f"{column} {stress}")
    total_stress += stress
    # break

print(f"total_stress {total_stress}")
