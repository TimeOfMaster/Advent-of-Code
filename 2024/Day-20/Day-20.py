from collections import deque
from dataclasses import dataclass
from typing import Tuple, Dict, Optional
import os

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
    def get_nbrs(self):
        for delta in (Pos(0, 1), Pos(0, -1), Pos(1, 0), Pos(-1, 0)):
            yield self + delta

@dataclass(frozen=True)
class Grid:
    grid: tuple[str]
    def height(self):
        return len(self.grid)
    def width(self):
        return len(self.grid[0])
    def __str__(self):
        return '\n'.join(self.grid)
    def get(self, pos: Pos):
        if self.is_inbounds(pos):
            return self.grid[pos.i][pos.j]
        return None
    def is_inbounds(self, pos):
        return 0 <= pos.i < self.height() and 0 <= pos.j < self.width()
    def bfs(self, start):
        q = deque()
        q.append(start)
        dist = {start: 0}
        while q:
            current = q.popleft()
            for nbr in current.get_nbrs():
                if self.get(nbr) == '#':
                    continue
                if nbr in dist:
                    continue
                dist[nbr] = dist[current] + 1
                q.append(nbr)
        return dist

def read_input(filename: str) -> Tuple[Grid, Pos, Pos]:
    grid = []
    start = end = None
    with open(filename, 'r') as f:
        for i, line in enumerate(f):
            row = line.strip()
            if 'S' in row:
                j = row.find('S')
                start = Pos(i, j)
                row = row.replace('S', '.')
            if 'E' in row:
                j = row.find('E')
                end = Pos(i, j)
                row = row.replace('E', '.')
            grid.append(row)
    return Grid(tuple(grid)), start, end

def get_num_good_cheats(
    grid: Grid,
    from_start: Dict[Pos, int],
    from_end: Dict[Pos, int],
    shortest_path: int,
    max_cheat_length: int,
    threshold: int
    ) -> int:
    good_cheats: int = 0
    for i in range(grid.height()):
        for j in range(grid.width()):
            cheat_start = Pos(i, j)
            if grid.get(cheat_start) == '#':
                continue
            for ik in range(-max_cheat_length, max_cheat_length+1):
                jk_max = max_cheat_length - abs(ik)
                for jk in range(-jk_max, jk_max+1):
                    cheat_end = cheat_start + Pos(ik, jk)
                    if grid.is_inbounds(cheat_end) and grid.get(cheat_end) == '.':
                        path_length = from_start[cheat_start] + abs(ik) + abs(jk) + from_end[cheat_end]
                        if shortest_path - path_length >= threshold:
                            good_cheats += 1
    return good_cheats

def main(
    grid: Grid,
    start: Pos,
    end: Pos,
    max_cheat_length: int,
    threshold: int
    ) -> int:
    from_start = grid.bfs(start)
    from_end = grid.bfs(end)
    shortest_path = from_start[end]
    
    return get_num_good_cheats(grid, from_start, from_end, shortest_path,  max_cheat_length, threshold)

if __name__ == '__main__':
    input_file: str = os.path.dirname(os.path.abspath(__file__)) + r"\\input.txt"
    data: Tuple[Grid, Pos, Pos] = read_input(input_file)

    grid: Grid = data[0]
    start: Pos = data[1]
    end: Pos = data[2]
    TRESHOLD: int  = 100

    print(f"Part 1: {main(grid, start, end, 2, TRESHOLD)}")
    print(f"Part 2: {main(grid, start, end, 20, TRESHOLD)}")
    