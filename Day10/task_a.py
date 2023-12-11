#!/usr/bin/env python3
import os

script_dir = os.path.dirname(os.path.realpath(__file__))

# test_data_path = f"{script_dir}/data_task_a"
# test_data_path = f"{script_dir}/data_task_a_test"
test_data_path = f"{script_dir}/data_task_a_test_2"
# test_data_path = f"{script_dir}/data_task_a_test_3"
# test_data_path = f"{script_dir}/data_task_b"
# test_data_path = f"{script_dir}/data_task_b_test"


NS_PIPE = "|"
EW_PIPE = "-"
NE_PIPE = "L"
NW_PIPE = "J"
SW_PIPE = "7"
SE_PIPE = "F"
GROUND = "."
START = "S"

Graphics_table = {
    NS_PIPE: "┃",
    EW_PIPE: "━",
    NE_PIPE: "┗",
    NW_PIPE: "┛",
    SW_PIPE: "┓",
    SE_PIPE: "┏",
    GROUND: " ",
    START: "S",
}

translation_table = {
    NS_PIPE: ["N", "S"],
    EW_PIPE: ["E", "W"],
    NE_PIPE: ["N", "E"],
    NW_PIPE: ["N", "W"],
    SW_PIPE: ["S", "W"],
    SE_PIPE: ["S", "E"],
    GROUND: [],
    START: ["N", "E", "S", "W"],
}

file = open(test_data_path)

pipes_system = list()


def get_at(x, y):
    try:
        # print(pipes_system[y][x])
        return pipes_system[y][x]
    except Exception:
        # print(None)
        return None


start_pos = (-1, -1)
other_pos = (5, 5)
other_pos2 = (88, 128)

for l in file:
    l = l.strip()
    pipes_system.append(l)
    # print(l)

for y in range(len(pipes_system)):
    for x in range(len(pipes_system[0])):
        if get_at(x, y) == START:
            start_pos = (x, y)
        print(Graphics_table[get_at(x, y)], end="")
    print()

# print(start_pos)
# print("--------------------------------------------------------")

skip = True
current_pos = start_pos
old_pos = (-1, -1)
old_dir = " "

while current_pos != start_pos or skip:
    skip = False

    print(f"old_pos: {old_pos}")
    print(f"current_pos: {current_pos}")

    pipe = ""
    if "N" in translation_table[get_at(current_pos[0], current_pos[1] + 1)]:
        pipe = pipe + "S"
    if "E" in translation_table[get_at(current_pos[0] - 1, current_pos[1])]:
        pipe = pipe + "W"
    if "S" in translation_table[get_at(current_pos[0], current_pos[1] - 1)]:
        pipe = pipe + "N"
    if "W" in translation_table[get_at(current_pos[0] + 1, current_pos[1])]:
        pipe = pipe + "E"

    print(current_pos)
    print(pipe)

    next_pos = None
    next_dir = ""
    print("-----------------------")
    print(f"old_pos: {old_pos}")
    print(f"old_dir {old_dir}")
    for c in pipe:
        if "N" in c and "S" not in old_dir:
            next_pos = (current_pos[0], current_pos[1] - 1)
            next_dir = "N"
        if "E" in c and "W" not in old_dir:
            next_pos = (current_pos[0] + 1, current_pos[1])
            next_dir = "E"
        if "S" in c and "N" not in old_dir:
            next_pos = (current_pos[0], current_pos[1] + 1)
            next_dir = "S"
        if "W" in c and "E" not in old_dir:
            next_pos = (current_pos[0] - 1, current_pos[1])
            next_dir = "W"
        print(f"> next_pos: {next_pos}")
        if next_pos == old_pos:
            continue
        if next_pos is not None:
            break
    print("-----------------------")

    old_pos = current_pos
    current_pos = next_pos
    old_dir = next_dir

    print(f"next_pos: {next_pos}")
    print("#################################")
    # break


print("Bye o/")
