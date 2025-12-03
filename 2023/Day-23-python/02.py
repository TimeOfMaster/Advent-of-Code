import os

input_path = os.path.dirname(os.path.abspath(__file__)) + r"\\input.txt"

grid = open(input_path, 'r').read().splitlines()

start = (0, grid[0].index("."))
end = (len(grid) - 1, grid[-1].index("."))

points = [start, end]

for r, row in enumerate(grid):
    for c, column in enumerate(row):
        if column == "#":
            continue
        neighbors = 0
        for new_row, new_column in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
            if 0 <= new_row < len(grid) and 0 <= new_column < len(grid[0]) and grid[new_row][new_column] != "#":
                neighbors += 1
        if neighbors >= 3:
            points.append((r, c))

graph = {pt: {} for pt in points}

for start_row, start_column in points:
    stack = [(0, start_row, start_column)]
    seen = {(start_row, start_column)}

    while stack:
        n, r, c = stack.pop()
        
        if n != 0 and (r, c) in points:
            graph[(start_row, start_column)][(r, c)] = n
            continue

        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            new_row = r + dr
            new_column = c + dc
            if 0 <= new_row < len(grid) and 0 <= new_column < len(grid[0]) and grid[new_row][new_column] != "#" and (new_row, new_column) not in seen:
                stack.append((n + 1, new_row, new_column))
                seen.add((new_row, new_column))

seen = set()

def dfs(pt):
    if pt == end:
        return 0

    m = -float("inf")

    seen.add(pt)
    for next in graph[pt]:
        if next not in seen:
            m = max(m, dfs(next) + graph[pt][next])
    seen.remove(pt)

    return m

print(dfs(start))