from dataclasses import dataclass
import re, os
from itertools import count

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
    def is_inbounds(self, n: int, m: int):
        return 0 <= self.x < m and 0 <= self.y < n
    def get_nbrs(self, n: int, m: int):
        for delta in (Pos(0, 1), Pos(0, -1), Pos(1, 0), Pos(-1, 0)):
            if (self+delta).is_inbounds(n, m):
                yield self + delta

def read_input(filename: str) -> list[tuple[Pos, Pos]]:
    robots: list[tuple[Pos, Pos]] = []
    with open(filename, 'r') as f:
        for line in f.readlines():
            pattern = r'p=(.+),(.+) v=(.+),(.+)'
            px, py, vx, vy = (int(z) for z in re.match(pattern, line).groups())
            robots.append((Pos(px, py), Pos(vx, vy)))
            
    return robots

def contains_cluster(robot_pos_list: list[Pos], n: int, m: int) -> bool:
    largest_group: int = 0
    candidates: set = set(robot_pos_list)
    num: int = len(candidates)
    while candidates:
        q = [list(candidates)[0]]
        visited = {q[0]}
        while q:
            current = q.pop()
            for nbr in current.get_nbrs(n, m):
                if nbr in candidates and nbr not in visited:
                    visited.add(nbr)
                    q.append(nbr)
        largest_group = max(largest_group, len(visited))
        candidates -= visited
    return largest_group >= num // 4

def main(robots: list[tuple[Pos, Pos]], n: int=103, m: int=101) -> int:
    robot_pos = [robot[0] for robot in robots]
    for seconds in count(1):
        for i in range(len(robot_pos)):
            x: int = (robot_pos[i].x + robots[i][1].x) % m
            y: int = (robot_pos[i].y + robots[i][1].y) % n
            robot_pos[i] = Pos(x, y)
        s = set(robot_pos)
        if contains_cluster(robot_pos, n, m):
            return seconds
        
if __name__ == "__main__":
    input_file: str = os.path.dirname(os.path.abspath(__file__)) + r"\\input.txt"
    data: list[str] = read_input(input_file)
    
    print(f"Part 2: Seconds: {main(data)}")