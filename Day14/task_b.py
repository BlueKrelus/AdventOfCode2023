#!/usr/bin/env python3
import os
import functools

from cProfile import Profile
from pstats import SortKey, Stats

script_dir = os.path.dirname(os.path.realpath(__file__))

test_data_path = f"{script_dir}/data_task_a"
test_data_path = f"{script_dir}/data_task_a_test"
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

print("--------------------------")

@functools.cache
def tilt_segment(segment, left):
    new_line = ""
    stones = segment.replace(".", "")
    empty = segment.replace("O", "")
    new_line += stones + empty if left else empty + stones
    new_line += "#"
    return new_line


@functools.cache
def tilt_line(line, left):
    new_line = ""
    segments = line.split("#")
    for segment in segments:
        new_line += tilt_segment(segment, left)
    if len(new_line) > len(line):
        new_line = new_line[:-1]
    return new_line

@functools.cache
def tilt(stone_platform, turn, left):
    if turn:
        stone_platform = rotate(stone_platform)
    new_platfrom = list()
    for line in stone_platform:
        new_platfrom.append(tilt_line(line, left))
    if turn:
        return rotate(new_platfrom)
    return new_platfrom


def tilt_north(stone_platform):
    return tilt(tuple(stone_platform), True, True)

def tilt_south(stone_platform):
    return tilt(tuple(stone_platform), True, False)

def tilt_west(stone_platform):
    return tilt(tuple(stone_platform), False, True)

def tilt_east(stone_platform):
    return tilt(tuple(stone_platform), False, False)

def print_platfrom(platform):
    for l in platform:
        print(l)
    print()

def test_directions(platform):
    print("Start:")
    print_platfrom(platform)
    platform = tilt_north(platform)
    print("north:")
    print_platfrom(platform)
    platform = tilt_west(platform)
    print("west:")
    print_platfrom(platform)
    platform = tilt_south(platform)
    print("south:")
    print_platfrom(platform)
    platform = tilt_east(platform)
    print("east:")
    print_platfrom(platform)



test_directions(stone_platform)

stone_platform = tuple(stone_platform)

@functools.cache
def cycle(platform):
    platform = tilt_north(platform)
    platform = tilt_west(platform)
    platform = tilt_south(platform)
    platform = tilt_east(platform)
    return tuple(platform)

@functools.cache
def cycles(platform, cycles):
    for i in range(cycles):
        # print(i)
        # platform = tilt_north(platform)
        # platform = tilt_west(platform)
        # platform = tilt_south(platform)
        # platform = tilt_east(platform)
        platform = cycle(platform)
    return tuple(platform)


def run():
    global stone_platform
    # for i in range(10000000):

    #              1000000000
    for i in range(10000000):
        # print(i)
        # stone_platform = tilt_north(stone_platform)
        # stone_platform = tilt_west(stone_platform)
        # stone_platform = tilt_south(stone_platform)
        # stone_platform = tilt_east(stone_platform)
        stone_platform = cycles(tuple(stone_platform), 100)

    print("-------------------")

    for l in stone_platform:
        print(l)

    # exit()

    total_stress = 0

    print("-------------")
    for x in range(len(stone_platform[0])):
        column = get_column(stone_platform, x)
        stress = 0
        for i in range(len(column)):
            if column[::-1][i] == "O":
                stress += i + 1
        total_stress += stress

    print(f"total_stress {total_stress}")


if __name__ == "__main__":
    run()