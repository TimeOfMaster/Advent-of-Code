from dataclasses import dataclass
from queue import PriorityQueue
from typing import Any
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
    def __lt__(self, other):
        return (self.i, self.j) < (other.i, other.j)
    def get_nbrs(self):
        for delta in (Pos(0, 1), Pos(0, -1), Pos(1, 0), Pos(-1, 0)):
            yield self + delta
    def rot_right(self):
        return Pos(self.j, -self.i)
    def rot_left(self):
        return Pos(-self.j, self.i)

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
    def dijkstra(self, start_pos: Pos, start_dir: Pos, end: Pos, grid) -> tuple[int, int]:
        # find shortest path to goal
        start: tuple[Pos, Pos] = (start_pos, start_dir)
        dist: dict[tuple, int] = {start: 0}
        expanded = set()
        q: PriorityQueue[tuple[dict[tuple[Pos, Pos], int], tuple[Pos, Pos]]] = PriorityQueue()
        q.put((dist[start], start))
        while not q.empty():
            d, current = q.get()
            # goal check
            if current[0] == end:
                end_state = current
                break
            if current in expanded:
                continue
            expanded.add(current)
            current_pos, current_dir = current
            nbrs: list[tuple[int, tuple[tuple[Pos, Pos], Pos]]] = []
            # walk forward
            forward_nbr: Pos = current_pos + current_dir
            if grid.get(forward_nbr) == '.':
                nbrs.append((1, (forward_nbr, current_dir)))
            # turn 90
            nbrs.append((1000, (current_pos, current_dir.rot_left())))
            nbrs.append((1000, (current_pos, current_dir.rot_right())))
            for cost, nbr in nbrs:
                total_dist = dist[current] + cost
                if nbr not in dist or total_dist < dist[nbr]:
                    dist[nbr] = total_dist
                    q.put((total_dist, nbr))

        # backtracking to find paths
        q = [end_state]
        visited: set[Any] = {end_state}
        while q:
            current = q.pop()
            if current == start:
                continue
            current_pos, current_dir = current
            nbrs = []
            # walk backward
            backward_nbr = current_pos - current_dir
            if grid.get(backward_nbr) == '.':
                nbrs.append((1, (backward_nbr, current_dir)))
            # turn 90
            nbrs.append((1000, (current_pos, current_dir.rot_left())))
            nbrs.append((1000, (current_pos, current_dir.rot_right())))
            for cost, nbr in nbrs:
                if nbr in dist and dist[nbr] == dist[current] - cost:
                    if nbr not in visited:
                        q.append(nbr)
                        visited.add(nbr)
        best_path_pos = set(state[0] for state in visited)
        return dist[end_state], len(best_path_pos)

def read_input(filename: str) -> tuple[Grid, Pos, Pos]:
    grid: list[str] = []
    with open(filename, 'r') as f:
        for i, line in enumerate(f.readlines()):
            row = line.strip()
            if 'S' in row:
                j: int= row.find('S')
                start: Pos = Pos(i, j)
                row: str = row.replace('S', '.')
            if 'E' in row:
                j: int = row.find('E')
                end: Pos = Pos(i, j)
                row: str = row.replace('E', '.')
            grid.append(row)
    grid: Grid = Grid(tuple(grid))
    return grid, start, end

def main(grid: Grid, start: Pos, end: Pos) -> int:
    data: tuple[int, int] = grid.dijkstra(start, Pos(0, 1), end, grid)
    distance: int = data[0]
    
    return distance
    
if __name__ == "__main__":
    input_file: str = os.path.dirname(os.path.abspath(__file__)) + r"\\input.txt"
    data: tuple[Grid, Pos, Pos] = read_input(input_file)
    
    grid: Grid = data[0]
    start: Pos = data[1]
    end: Pos = data[2]
    
    print(f"Part 1: {main(grid, start, end)}")