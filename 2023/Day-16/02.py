import os
from dataclasses import dataclass

input_path = os.path.dirname(os.path.abspath(__file__)) + r"\\input.txt"

grid = []
with open(input_path, 'r') as f:
    for line in f.readlines():
        grid.append(line.strip())
        
n, m = len(grid), len(grid[0])

@dataclass(frozen=True)
class Pos:
    row: int
    col: int
    def __add__(self, other):
        return Pos(row=self.row + other.row, col=self.col + other.col)

def get_num_energised(pos, direction):
    beams = [(pos, direction)]
    energised = set()
    already_done = set()
    while beams:
        pos, direction = beams.pop()
        already_done.add((pos, direction))
        next_pos = pos + direction
        if not (0 <= next_pos.row < n and 0 <= next_pos.col < m):
            continue
        energised.add(next_pos)
        char = grid[next_pos.row][next_pos.col]
        next_directions = []
        if char == '.':
            next_directions.append(direction)
        elif char == '/':
            next_directions.append({Pos(0, 1): Pos(-1, 0), Pos(1, 0): Pos(0, -1), Pos(-1, 0): Pos(0, 1), Pos(0, -1): Pos(1, 0)}[direction])
        elif char == '\\':
            next_directions.append({Pos(0, 1): Pos(1, 0), Pos(1, 0): Pos(0, 1), Pos(-1, 0): Pos(0, -1), Pos(0, -1): Pos(-1, 0)}[direction])
        elif char == '-':
            if direction.row == 0:
                next_directions.append(direction)
            else:
                next_directions.append(Pos(0, -1))
                next_directions.append(Pos(0, 1))
        elif char == '|':
            if direction.col == 0:
                next_directions.append(direction)
            else:
                next_directions.append(Pos(1, 0))
                next_directions.append(Pos(-1, 0))
        for next_dir in next_directions:
            if (next_pos, next_dir) not in already_done:
                beams.append((next_pos, next_dir))
    return len(energised)

starts = []
for i in range(n):
    starts.append((Pos(i, -1), Pos(0, 1)))
    starts.append((Pos(i, m), Pos(0, -1)))
for j in range(m):
    starts.append((Pos(-1, j), Pos(1, 0)))
    starts.append((Pos(n, j), Pos(-1, 0)))

print(max(get_num_energised(*p) for p in starts))