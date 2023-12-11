#!/usr/bin/env python3
import os

script_dir = os.path.dirname(os.path.realpath(__file__))

# test_data_path = f"{script_dir}/data_task_a"
test_data_path = f"{script_dir}/data_task_a_test"
# test_data_path = f"{script_dir}/data_task_b"
# test_data_path = f"{script_dir}/data_task_b_test"

file = open(test_data_path)

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
        seed_list = l.split(":")[1].split()
    if "map" in l:
        map_to_store = l.split()[0]
        continue
    if len(l.strip()) == 0:
        continue
    # store in maps
    if map_to_store == "seed-to-soil":
        seed_to_soil_map.append(l)


print("---------")
print(seed_list)
