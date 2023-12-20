import os

input_path = os.path.dirname(os.path.abspath(__file__)) + r"\\input.txt"

class Grid:
    def __init__(self):
        self.rows = []
        self.expanded_rows = set()
        self.expanded_columns = set()
        
    def __repr__(self):
        return '\n'.join(''.join(row) for row in self.rows)
    
    def add_row(self, row):
        self.rows.append(row)
        
    def width(self):
        return len(self.rows[0])
    
    def height(self):
        return len(self.rows)
    
    def expand(self):
        for i in range(self.height()):
            if all(char == '.' for char in self.rows[i]):
                self.expanded_rows.add(i)
        for j in range(self.width()):
            col = [self.rows[i][j] for i in range(self.height())]
            if all(char == '.' for char in col):
                self.expanded_columns.add(j)
                
    def distance(self, i1, j1, i2, j2, expansion):
        offset = 0
        minimum = min(i1, i2)
        maximum = max(i1, i2)
        for i in range(minimum+1, maximum):
            if i in self.expanded_rows:
                offset += (expansion-1)
        minimumj = min(j1, j2)
        maximumj = max(j1, j2)
        for j in range(minimumj+1, maximumj):
            if j in self.expanded_columns:
                offset += (expansion-1)
        return abs(i1 - i2) + abs(j1-j2) + offset
    def get(self, row, col):
        return self.rows[row][col]

grid = Grid()

with open(input_path, 'r') as f:
    for line in f.readlines():
        grid.add_row(list(line.strip()))
grid.expand()

galaxies = []
for row in range(grid.height()):
    for col in range(grid.width()):
        if grid.get(row, col) == '#':
            galaxies.append((row, col))

total = 0
for i1, j1 in galaxies:
    for i2, j2 in galaxies:
        total += grid.distance(i1, j1, i2, j2, 2)

print(total // 2) # // -> floored division