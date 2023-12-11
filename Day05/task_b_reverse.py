#!/usr/bin/env python3
import os
import time
import math

script_dir = os.path.dirname(os.path.realpath(__file__))

test_data_path = f"{script_dir}/data_task_a"
# test_data_path = f"{script_dir}/data_task_a_test"
# test_data_path = f"{script_dir}/data_task_b"
# test_data_path = f"{script_dir}/data_task_b_test"

file = open(test_data_path)

DEST_RANGE = 0
SRC_RANGE = 1
RANGE_LENGTH = 2

seed_to_soil_map = list()
soil_to_fertilizer_map = list()
fertilizer_to_water_map = list()
water_to_light_map = list()
light_to_temperature_map = list()
temperature_to_humidity_map = list()
humidity_to_location_map = list()

seed_list = list()

current_map = list()
map_to_store = None
for l in file:
    print(l.strip())
    if "seeds" in l:
        seed_list = [int(x) for x in l.split(":")[1].split()]
        continue
    if "map" in l:
        map_to_store = l.split()[0]
        continue
    if len(l.strip()) == 0:
        continue
    if l.split()[0].isdigit():
        if map_to_store == "seed-to-soil":
            seed_to_soil_map.append([int(x) for x in l.split()])
        if map_to_store == "soil-to-fertilizer":
            soil_to_fertilizer_map.append([int(x) for x in l.split()])
        if map_to_store == "fertilizer-to-water":
            fertilizer_to_water_map.append([int(x) for x in l.split()])
        if map_to_store == "water-to-light":
            water_to_light_map.append([int(x) for x in l.split()])
        if map_to_store == "light-to-temperature":
            light_to_temperature_map.append([int(x) for x in l.split()])
        if map_to_store == "temperature-to-humidity":
            temperature_to_humidity_map.append([int(x) for x in l.split()])
        if map_to_store == "humidity-to-location":
            humidity_to_location_map.append([int(x) for x in l.split()])

# print("---------")
# print("seed_list")
# print(seed_list)
# print("seed_to_soil_map")
# print(seed_to_soil_map)
# print("soil_to_fertilizer_map")
# print(soil_to_fertilizer_map)
# print("fertilizer_to_water_map")
# print(fertilizer_to_water_map)
# print("water_to_light_map")
# print(water_to_light_map)
# print("light_to_temperature_map")
# print(light_to_temperature_map)
# print("temperature_to_humidity_map")
# print(temperature_to_humidity_map)
# print("humidity_to_location_map")
# print(humidity_to_location_map)

print("--------------------------------------")


def remap_value(maps, value):
    for m in maps:
        # print(m)
        # print(m[SRC_RANGE])
        # print(m[SRC_RANGE] + m[RANGE_LENGTH])
        if value >= m[SRC_RANGE] and value <= m[SRC_RANGE] + m[RANGE_LENGTH]:
            return value + (m[DEST_RANGE] - m[SRC_RANGE])
    return value


def remap_value_reverse(maps, value):
    for m in maps:
        if value >= m[DEST_RANGE] and value <= m[DEST_RANGE] + m[RANGE_LENGTH]:
            # print(m[SRC_RANGE] - m[DEST_RANGE])
            return value + (m[SRC_RANGE] - m[DEST_RANGE])
    return value


min_location = -1

seed_range_list = list()


index = 0
while index < len(seed_list):
    seed_range_list.append([seed_list[index], seed_list[index + 1]])
    index += 2

loop = 0

for m in seed_range_list:
    print(m)

print(seed_range_list[0][0])

print(seed_range_list[0][0] + seed_range_list[0][1] - 1)

# exit()


def check_if_in_range(maps, value):
    for m in maps:
        if value >= m[0] and value <= m[0] + m[1]:
            return True
    return False


print("-----------------------------")

# for step in [100000, 10000, 1000, 100, 10, 1]:
# for step in [100000, 10000]:
for i in range(1000000):
    min = i
    max = 100000000
    if min_location != -1:
        max = min_location
        # max = min_location + step*10
    step = math.floor((max-min)*0.01)
    if step <= 0:
        step = 1
    # step = 1000
    print(f"min: {min}")
    print(f"max: {max}")
    print(f"step: {step}")

    if min == max:
        break

    for location in range(min, max+1, step):
        # print(f"location: {location}")
        humidity = remap_value_reverse(humidity_to_location_map, location)

        # print(f"humidity: {humidity}")
        temperature = remap_value_reverse(temperature_to_humidity_map, humidity)

        # print(f"temperature: {temperature}")
        light = remap_value_reverse(light_to_temperature_map, temperature)

        # print(f"light: {light}")
        water = remap_value_reverse(water_to_light_map, light)

        # print(f"water: {water}")
        fertilizer = remap_value_reverse(fertilizer_to_water_map, water)

        # print(f"fertilizer: {fertilizer}")
        soil = remap_value_reverse(soil_to_fertilizer_map, fertilizer)

        # print(f"soil: {soil}")
        seed = remap_value_reverse(seed_to_soil_map, soil)

        # print(f"seed: {seed}")

        loop += 1
        if check_if_in_range(seed_range_list, seed):
            min_location = location
            print(f"seed: {seed}")
            print(f"min_location: {min_location}")
            break
    print("##############################")
    # if str(min_location)[-1] is not '0':
    #     break

# print([x for x in range(5, 5 + 2)])
# print(range(5, 10)[1])
print(f"min_location: {min_location}")
print(f"loop: {loop}")
