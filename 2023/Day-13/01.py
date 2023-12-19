import os

input_path = os.path.dirname(os.path.abspath(__file__)) + r"\\input.txt"

def transpose(grid):
    return [[grid[i][j] for i in range(len(grid))] for j in range(len(grid[0]))]

def print_grid(grid):
    print('\n')
    for row in grid:
        print(''.join(row))
    print('\n')

def get_vert_reflect_line(grid):
    n, m = len(grid), len(grid[0])
    lines = []
    for j in range(1, m):
        width = min(j, m-j)
        if all(tuple(grid[i][j-width:j]) == tuple(grid[i][j:j+width][::-1]) for i in range(n)):
            lines.append(j)
    return lines

def get_scores(grid):
    scores = []
    for l in get_vert_reflect_line(grid):
        scores.append(l)
    for k in get_vert_reflect_line(transpose(grid)):
        scores.append(100 * k)
    return scores

total = 0
with open(input_path, 'r') as f:
    grid = []
    for line in list(f.readlines()) + ['\n']:  # ensure count of final grid
        if line.strip():
            grid.append(list(line.strip()))
            continue

        score = get_scores(grid)[0]
        total += score
        
        grid = []

print(total)
