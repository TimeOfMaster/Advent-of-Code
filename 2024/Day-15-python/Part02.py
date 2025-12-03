from dataclasses import dataclass
import os

@dataclass(frozen=True)
class Pos:
    i: int
    j: int
    def __add__(self, other):
        return Pos(self.i + other.i, self.j + other.j)
    def __sub__(self, other):
        return Pos(self.i - other.i, self.j - other.j)
    def __eq__(self, other):
        return isinstance(other, Pos) and (self.i, self.j) == (other.i, other.j)
    def __hash__(self):
        return hash((self.i, self.j))
    
def read_input_part01(filename: str) -> tuple[list[str], list[str], int, int, Pos]:
    grid: list[str] = []
    moves: list[str] = []
    with open(filename, 'r') as f:
        for i, line in enumerate(f.readlines()):
            if line.startswith('#'):
                row = list(line.strip())
                if '@' in row:
                    j = row.index('@')
                    robot_pos: Pos = Pos(i, j)
                    row[j] = '.'
                grid.append(row)
            else:
                moves.append(line.strip())
    moves = ''.join(moves)
    length: int = len(grid)
    width: int = len(grid[0])

    return grid, moves, length, width, robot_pos

def read_input(filename: str) -> tuple[list[str], int, int, Pos]:
    grid: list[str] = []
    with open(filename, 'r') as f:
        for i, line in enumerate(f.readlines()):
            if line.startswith('#'):
                row = list(line.strip().replace('#', '##').replace('O', '[]').replace('.', '..').replace('@', '@.'))
                if '@' in row:
                    j = row.index('@')
                    robot_pos = Pos(i, j)
                    row[j] = '.'
                grid.append(row)
    length: int = len(grid)
    width: int = len(grid[0])

    return grid, length, width, robot_pos

def main(
        grid: list[str], 
        moves: list[str], 
        length: int, 
        width: int, 
        robot_pos: Pos,
        DIRECTIONS: dict[str, Pos]={'^': Pos(-1, 0), '>': Pos(0, 1), 'v': Pos(1, 0), '<': Pos(0, -1)}
        ) -> int:
    for char in moves:
        dest: Pos = robot_pos + DIRECTIONS[char]
        if grid[dest.i][dest.j] == '.':
            robot_pos = dest
        elif grid[dest.i][dest.j] in '[]':
            # find all box positions getting pushed
            q: list[Pos] = [dest]
            boxes: set[Pos] = {dest}
            while q:
                current: Pos = q.pop()
                nbrs: list[Pos] = []
                if grid[current.i][current.j] == '[':
                    nbrs.append(current + Pos(0, 1))
                else:
                    nbrs.append(current + Pos(0, -1))
                nbrs.append(current + DIRECTIONS[char])
                for nbr in nbrs:
                    if nbr in boxes:
                        continue
                    if grid[nbr.i][nbr.j] in '[]':
                        q.append(nbr)
                        boxes.add(nbr)
            # find all spaces in front of boxes getting pushed
            spaces: set[Pos] = set()
            for box in boxes:
                space_ahead: Pos = box + DIRECTIONS[char]
                if space_ahead not in boxes:
                    spaces.add(space_ahead)
                    if grid[space_ahead.i][space_ahead.j] == '#':
                        break
            # check if empty spaces in front, and apply push if so
            if all(grid[space.i][space.j] == '.' for space in spaces):
                def push_distance(box):
                    if char in '<>':
                        return abs(box.j - dest.j)
                    else:
                        return abs(box.i - dest.i)
                for box in sorted(boxes, key=push_distance, reverse=True):
                    space_ahead = box + DIRECTIONS[char]
                    grid[box.i][box.j], grid[space_ahead.i][space_ahead.j] = grid[space_ahead.i][space_ahead.j], grid[box.i][box.j]
                robot_pos = dest

    gps: int = 0
    for i in range(length):
        for j in range(width):
            if grid[i][j] == '[':
                gps += (100*i + j)
    return gps

if __name__ == "__main__":
    input_file: str = os.path.dirname(os.path.abspath(__file__)) + r"\\input.txt"
    data: tuple[list[str], int, int, Pos] = read_input(input_file)
    data_part01: tuple[list[str], list[str], int, int, Pos] = read_input_part01(input_file)

    grid = data[0]
    moves = data_part01[1]
    length = data[1]
    width = data[2]
    robot_pos = data[3]
    
    print(f"Part 2: {main(grid, moves, length, width, robot_pos)}")