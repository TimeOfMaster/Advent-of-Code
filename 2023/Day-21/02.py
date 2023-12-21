from collections import deque
import os

input_path = os.path.dirname(os.path.abspath(__file__)) + r"\\input.txt"

grid = open(input_path, 'r').read().splitlines()

start_row, start_column = next((r, c) for r, row in enumerate(grid) for c, column in enumerate(row) if column == "S")

assert len(grid) == len(grid[0])    # assert grid is square

size = len(grid)
steps = 26501365

assert start_row == start_column == size // 2   # assert start in the middle of grid
assert steps % size == size // 2

def fill(start_row, start_column, steps):
    answer = set()
    seen = {(start_row, start_column)}
    queue = deque([(start_row, start_column, steps)])

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
    
    return len(answer)

grid_width = steps // size - 1

odd = (grid_width // 2 * 2 + 1) ** 2
even = ((grid_width + 1) // 2 * 2) ** 2

odd_points = fill(start_row, start_column, size * 2 + 1)
even_points = fill(start_row, start_column, size * 2)

corner_top = fill(size - 1, start_column, size - 1)
corner_right = fill(start_row, 0, size - 1)
corner_bottom = fill(0, start_column, size - 1)
corner_left = fill(start_row, size - 1, size - 1)

small_topright = fill(size - 1, 0, size // 2 - 1)
small_topleft = fill(size - 1, size - 1, size // 2 - 1)
small_bottomright = fill(0, 0, size // 2 - 1)
small_bottomleft = fill(0, size - 1, size // 2 - 1)

large_topright = fill(size - 1, 0, size * 3 // 2 - 1)
large_topleft = fill(size - 1, size - 1, size * 3 // 2 - 1)
large_bottomright = fill(0, 0, size * 3 // 2 - 1)
large_bottomleft = fill(0, size - 1, size * 3 // 2 - 1)

print(
    odd * odd_points +
    even * even_points +
    
    corner_top + corner_right + corner_bottom + corner_left +
    
    (grid_width + 1) * (small_topright + small_topleft + small_bottomright + small_bottomleft) +
    
    grid_width * (large_topright + large_topleft + large_bottomright + large_bottomleft)
)