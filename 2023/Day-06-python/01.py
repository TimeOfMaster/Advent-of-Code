import os, math

input_path = os.path.dirname(os.path.abspath(__file__)) + r"\\input.txt"

with open(input_path, 'r') as f:
    times = list(map(int, f.readline().split()[1:]))
    distance = list(map(int, f.readline().split()[1:]))

def get_distance(charge, race_time):
    return (race_time - charge) * charge

num_ways = 1
for i, time in enumerate(times):
    num = 0
    for charge in range(time + 1):
        if get_distance(charge, time) > distance[i]:
            num += 1
    num_ways *= num

print(num_ways)
