import os
from collections import defaultdict

input_path = os.path.dirname(os.path.abspath(__file__)) + r"\\input.txt"

grid = []

with open(input_path, 'r') as f:
    for line in f.readlines():
        grid.append(line.strip())

n = len(grid)
m = len(grid[0])

def get_numbers(i, j1, j2):
    number_set = set()
    for j in range(j1, j2):
        for di in [-1, 0, 1]:
            for dj in [-1, 0, 1]:
                if (di, dj) == (0, 0):
                    continue
                nbri, nbrj = i + di, j + dj
                if 0 <= nbri < n and 0 <= nbrj < m:
                    number_set.add((nbri, nbrj))
    return number_set

def is_symbol(char):
    return (not char.isdigit()) and char != '.'

table = defaultdict(list)
for i in range(n):
    j = 0
    while j < m:
        if not grid[i][j].isdigit():
            j += 1
            continue
        j2 = j + 1
        while j2 < m and grid[i][j2].isdigit():
            j2 += 1
        if any(is_symbol(grid[nbri][nbrj]) for nbri, nbrj in get_numbers(i, j, j2)):
            num = int(grid[i][j:j2])

            for nbri, nbrj in get_numbers(i, j, j2):
                if grid[nbri][nbrj] == '*':
                    table[(nbri, nbrj)].append(num)
        j = j2

gear_ratio_sum = 0
for v in table.values():
    if len(v) == 2:
        gear_ratio_sum += (v[0]*v[1])
print(gear_ratio_sum)