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

graph = {point: {} for point in points}

dirs = {
    "^": [(-1, 0)], # up
    "v": [(1, 0)],  # down
    "<": [(0, -1)], # left
    ">": [(0, 1)],  # right
    ".": [(-1, 0), (1, 0), (0, -1), (0, 1)],    # any direction
}

for start_row, start_column in points:
    stack = [(0, start_row, start_column)]
    seen = {(start_row, start_column)}

    while stack:
        n, r, c = stack.pop()
        
        if n != 0 and (r, c) in points:
            graph[(start_row, start_column)][(r, c)] = n
            continue

        for direction_row, direction_column in dirs[grid[r][c]]:
            new_row = r + direction_row
            new_column = c + direction_column
            if 0 <= new_row < len(grid) and 0 <= new_column < len(grid[0]) and grid[new_row][new_column] != "#" and (new_row, new_column) not in seen:
                stack.append((n + 1, new_row, new_column))
                seen.add((new_row, new_column))

seen = set()

def dfs(point):
    if point == end:
        return 0

    m = -float("inf")

    seen.add(point)
    for next in graph[point]:
        if next not in seen:
            m = max(m, dfs(next) + graph[point][next])
    seen.remove(point)

    return m

print(dfs(start))