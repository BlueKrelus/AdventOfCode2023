#!/usr/bin/env python3
import os

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

print("---------")
print("seed_list")
print(seed_list)
print("seed_to_soil_map")
print(seed_to_soil_map)
print("soil_to_fertilizer_map")
print(soil_to_fertilizer_map)
print("fertilizer_to_water_map")
print(fertilizer_to_water_map)
print("water_to_light_map")
print(water_to_light_map)
print("light_to_temperature_map")
print(light_to_temperature_map)
print("temperature_to_humidity_map")
print(temperature_to_humidity_map)
print("humidity_to_location_map")
print(humidity_to_location_map)

print("--------------------------------------")


def remap_value(maps, value):
    for m in maps:
        # print(m)
        # print(m[SRC_RANGE])
        # print(m[SRC_RANGE] + m[RANGE_LENGTH])
        if value >= m[SRC_RANGE] and value <= m[SRC_RANGE] + m[RANGE_LENGTH]:
            return value + (m[DEST_RANGE] - m[SRC_RANGE])
    return value

min_location = None

seed_range_list = list()


index = 0
while index < len(seed_list):
    seed_range_list.append([seed_list[index], seed_list[index+1]])
    index += 2

# print(seed_range_list)

# for i in range(seed_range_list[0][0], seed_range_list[0][0]+seed_range_list[0][1]):
#     print(i)

# exit()

loop = 0

for seed_range in seed_range_list:
    print(seed_range)
    for seed in range(seed_range[0], seed_range[0]+seed_range[1]):
        # print(f"seed: {seed}")
        soil = remap_value(seed_to_soil_map, seed)
        # print(f"soil: {soil}")
        fertilizer = remap_value(soil_to_fertilizer_map, soil)
        # print(f"fertilizer: {fertilizer}")
        water = remap_value(fertilizer_to_water_map, fertilizer)
        # print(f"water: {water}")
        light = remap_value(water_to_light_map, water)
        # print(f"light: {light}")
        temperature = remap_value(light_to_temperature_map, light)
        # print(f"temperature: {temperature}")
        humidity = remap_value(temperature_to_humidity_map, temperature)
        # print(f"humidity: {humidity}")
        location = remap_value(humidity_to_location_map, humidity)
        # print(f"location: {location}")
        # print(location)
        # break
        if min_location is None:
            min_location = location
        min_location = min([min_location, location])
        loop += 1
# print([x for x in range(5, 5 + 2)])
# print(range(5, 10)[1])
print(f"min_location: {min_location}")
print(f"loop: {loop}")
