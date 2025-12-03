from dataclasses import dataclass
import os, unittest

def read_input(filename: str) -> tuple[int, int, list[list[int]]]:
    grid: list[list[int]] = []
    with open(filename, 'r') as f:
        for i, line in enumerate(f.readlines()):
            grid.append([int(x) for x in line.strip()])
    length = len(grid)
    width = len(grid[0])

    return length, width, grid

@dataclass(frozen=True)
class Pos:
    i: int
    j: int
    def __add__(self, other):
        return Pos(self.i + other.i, self.j + other.j)
    def __eq__(self, other):
        return isinstance(other, Pos) and (self.i, self.j) == (other.i, other.j)
    def __hash__(self):
        return hash((self.i, self.j))
    def is_inbounds(self):
        return 0 <= self.i < length and 0 <= self.j < width
    def get_nbrs(self):
        for delta in (Pos(0, 1), Pos(0, -1), Pos(1, 0), Pos(-1, 0)):
            if (self+delta).is_inbounds():
                yield self + delta

def dfs(start: Pos, grid: list[list[int]]) -> tuple[int, int]:
    peaks: set[Pos] = set()
    rating: int = 0
    q: list[Pos] = [start]
    while q:
        current = q.pop()
        if grid[current.i][current.j] == 9:
            rating += 1
            peaks.add(current)
        for nbr in current.get_nbrs():
            if grid[nbr.i][nbr.j] == 1 + grid[current.i][current.j]:
                q.append(nbr)
    return len(peaks), rating

def main(length: int, width: int, grid: list[list[int]]) -> int:
    rating: int = 0
    for current_length_pos in range(length):
        for current_width_pos in range(width):
            if grid[current_length_pos][current_width_pos] == 0:
                s, r = dfs(Pos(current_length_pos, current_width_pos), grid=grid)
                rating += r
    return rating

if __name__ == "__main__":
    input_file: str = os.path.dirname(os.path.abspath(__file__)) + r"\\input.txt"
    data: tuple[int, int, list[list[int]]] = read_input(input_file)

    length: int = data[0]
    width: int = data[1]
    grid: list[list[int]] = data[2]
    
    print(f"Part 2: {main(length, width, grid)}")
    
    unittest.main()
