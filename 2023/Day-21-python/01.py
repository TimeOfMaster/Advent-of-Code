from collections import deque
import os

input_path = os.path.dirname(os.path.abspath(__file__)) + r"\\input.txt"

grid = open(input_path, 'r').read().splitlines()

start_row, start_column = next((r, c) for r, row in enumerate(grid) for c, column in enumerate(row) if column == "S")

# Breadth-First-Fill (Flood fill)
answer = set()
seen = {(start_row, start_column)}
queue = deque([(start_row, start_column, 64)])

while queue:
    r, c, s = queue.popleft()

    if s % 2 == 0:
        answer.add((r, c))
    if s == 0:
        continue

    for next_row, next_column in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
        if next_row < 0 or next_row >= len(grid) or next_column < 0 or next_column >= len(grid[0]) or grid[next_row][next_column] == "#" or (next_row, next_column) in seen:
            continue
        seen.add((next_row, next_column))
        queue.append((next_row, next_column, s - 1))

print(len(answer))