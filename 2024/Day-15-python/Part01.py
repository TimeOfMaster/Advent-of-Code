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

def read_input(filename: str) -> tuple[list[str], list[str], int, int, Pos]:
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
        elif grid[dest.i][dest.j] == 'O':
            temp = dest
            while grid[temp.i][temp.j] == 'O':
                temp += DIRECTIONS[char]
            if grid[temp.i][temp.j] == '.':
                grid[dest.i][dest.j] = '.'
                grid[temp.i][temp.j] = 'O'
                robot_pos = dest

    gps: int = 0
    for i in range(length):
        for j in range(width):
            if grid[i][j] == 'O':
                gps += (100*i + j)
    return gps

if __name__ == "__main__":
    input_file: str = os.path.dirname(os.path.abspath(__file__)) + r"\\input.txt"
    data: tuple[list[str], list[str], int, int, Pos] = read_input(input_file)

    grid = data[0]
    moves = data[1]
    length = data[2]
    width = data[3]
    robot_pos = data[4]
    
    print(f"Part 1: {main(grid, moves, length, width, robot_pos)}")