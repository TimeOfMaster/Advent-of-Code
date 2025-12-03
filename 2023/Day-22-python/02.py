from collections import deque
import os

input_path = os.path.dirname(os.path.abspath(__file__)) + r"\\input.txt"

bricks = []
for line in open(input_path):
    bricks += [list(map(int, line.replace("~", ",").split(",")))]

bricks.sort(key=lambda brick: brick[2]) # sort by z coord

def overlaps(a, b):
    return max(a[0], b[0]) <= min(a[3], b[3]) and max(a[1], b[1]) <= min(a[4], b[4])

# simulated fall
for index, brick in enumerate(bricks):
    max_z = 1   # max z coord after drop
    for check in bricks[:index]:
        if overlaps(brick, check):
            max_z = max(max_z, check[5] + 1)
    brick[5] -= brick[2] - max_z
    brick[2] = max_z
    
bricks.sort(key=lambda brick: brick[2]) # sort by z coord

# k: lower brick 
# v: upper brick
k_supports_v = {i: set() for i in range(len(bricks))}
v_supports_k = {i: set() for i in range(len(bricks))}

for j, upper in enumerate(bricks):
    for i, lower in enumerate(bricks[:j]):
        if overlaps(lower, upper) and upper[2] == lower[5] + 1:
            k_supports_v[i].add(j)
            v_supports_k[j].add(i)

total = 0

for i in range(len(bricks)):
    queue = deque(j for j in k_supports_v[i] if len(v_supports_k[j]) == 1)
    falling = set(queue)
    falling.add(i)
    
    while queue:
        j = queue.popleft()
        for k in k_supports_v[j]:
            if k not in falling:
                if v_supports_k[k] <= falling:
                    queue.append(k)
                    falling.add(k)
    
    total += len(falling) - 1

print(total)