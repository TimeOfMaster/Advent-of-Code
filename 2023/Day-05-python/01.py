import os

input_path = os.path.dirname(os.path.abspath(__file__)) + r"\\input.txt"

seed_to_soil = []
soil_to_fertilizer = []
fertilizer_to_water = []
water_to_light = []
light_to_temperature = []
temperature_to_humidity = []
humidity_to_location = []

map_lists = [seed_to_soil, soil_to_fertilizer, fertilizer_to_water, water_to_light,
             light_to_temperature, temperature_to_humidity, humidity_to_location]

with open(input_path, 'r') as f:
    for line in f.readlines():
        if not line.strip():
            continue
        if line.startswith('seeds:'):
            seeds = [int(x) for x in line.split()[1:]]
            continue
        elif line.startswith('seed-to-soil'):
            map_list = seed_to_soil
            continue
        elif line.startswith('soil-to-fertilizer'):
            map_list = soil_to_fertilizer
            continue
        elif line.startswith('fertilizer-to-water'):
            map_list = fertilizer_to_water
            continue
        elif line.startswith('water-to-light'):
            map_list = water_to_light
            continue
        elif line.startswith('light-to-temperature'):
            map_list = light_to_temperature
            continue
        elif line.startswith('temperature-to-humidity'):
            map_list = temperature_to_humidity
            continue
        elif line.startswith('humidity-to-location'):
            map_list = humidity_to_location
            continue
        temp = [int(x) for x in line.split()]
        map_list.append((temp[1], temp[2], temp[0]))

def get_dest(src, map_list):
    for s, r, d in map_list:
        if s <= src < s+r:
            return src - s + d
    return src


def get_location(seed):
    temp = seed
    for map_list in map_lists:
        temp = get_dest(temp, map_list)
    return temp

print(min(get_location(seed) for seed in seeds))
