from dataclasses import dataclass
from collections import deque
import os

@dataclass(frozen=True)
class Pos:
    x: int
    y: int
    def __add__(self, other):
        return Pos(self.x + other.x, self.y + other.y)
    def __eq__(self, other):
        return isinstance(other, Pos) and (self.x, self.y) == (other.x, other.y)
    def __hash__(self):
        return hash((self.x, self.y))
    def is_inbounds(self, N: int, M: int) -> bool:
        return 0 <= self.x < M and 0 <= self.y < N
    def get_nbrs(self, N: int=71, M: int=71):
        for delta in (Pos(0, 1), Pos(0, -1), Pos(1, 0), Pos(-1, 0)):
            if (self+delta).is_inbounds(N=N, M=M,):
                yield self + delta

def read_input(filename: str) -> list[Pos]:
    bytes: list[Pos] = []
    with open(filename, 'r') as f:
        for line in f.readlines():
            x, y = (int(z) for z in line.split(','))
            bytes.append(Pos(x, y))
    
    return bytes

def bfs(start: Pos, goal: Pos, obstacles: set[list[Pos]]) -> dict[Pos, int]:
    queue: deque = deque()
    queue.append(start)
    dist: dict[Pos, int] = {start: 0}
    while queue:
        current = queue.popleft()
        for nbr in current.get_nbrs():
            if nbr in obstacles:
                # print(current, nbr)
                continue
            if nbr in dist:
                continue
            dist[nbr] = dist[current] + 1
            if nbr == goal:
                return dist[nbr]
            queue.append(nbr)

def main(bytes: list[Pos], N: int=71, M: int=71) -> list[Pos]:
    obstacles: set[list[Pos]] = set(bytes[:1024])
    for i in range(1024, len(bytes)):
        obstacles.add(bytes[i])
        if bfs(Pos(0, 0), Pos(M-1, N-1), obstacles) is None:
            break
    return '{},{}'.format(bytes[i].x, bytes[i].y)

if __name__ == "__main__":
    input_file: str = os.path.dirname(os.path.abspath(__file__)) + r"\\input.txt"
    data: list[Pos] = read_input(input_file)
    
    print(f"Part 2: {main(data)}")