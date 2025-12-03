import os, math

input_path = os.path.dirname(os.path.abspath(__file__)) + r"\\input.txt"

with open(input_path, 'r') as f:
    times = list(map(int, f.readline().split()[1:]))
    distance = list(map(int, f.readline().split()[1:]))

def get_distance(charge, race_time):
    return (race_time - charge) * charge

t = int(''.join(map(str, times)))
d = int(''.join(map(str, distance)))

num = 0
for charge in range(t + 1):
    if get_distance(charge, t) > d:
        num += 1
print(num)