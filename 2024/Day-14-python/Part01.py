from dataclasses import dataclass
import re, os

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

def read_input(filename: str) -> list[tuple[Pos, Pos]]: # type: ignore
    robots: list[tuple[Pos, Pos]] = []
    with open(filename, 'r') as f:
        for line in f.readlines():
            pattern = r'p=(.+),(.+) v=(.+),(.+)'
            px, py, vx, vy = (int(z) for z in re.match(pattern, line).groups())
            robots.append((Pos(px, py), Pos(vx, vy)))
            
    return robots

def get_dest(pos: Pos, vel: Pos, steps: int, n: int, m: int):
    x = (pos.x + vel.x * steps) % m
    y = (pos.y + vel.y * steps) % n
    return Pos(x, y)

def main(robots: list[tuple[Pos, Pos]], steps: int=100,n: int=103, m: int=101) -> int:
    top_left, top_right, bottom_left, bottom_right = 0, 0, 0, 0
    for pos, velocity in robots:
        dest = get_dest(pos, velocity, steps, n, m)
        if dest.x < m//2:
            if dest.y < n//2:
                top_left += 1
            elif dest.y > n//2:
                bottom_left += 1
        elif dest.x > m//2:
            if dest.y < n//2:
                top_right += 1
            elif dest.y > n//2:
                bottom_right += 1
    return top_left*top_right*bottom_left*bottom_right
        
if __name__ == "__main__":
    input_file: str = os.path.dirname(os.path.abspath(__file__)) + r"\\input.txt"
    data: list[str] = read_input(input_file)
    
    print(f"Part 1: {main(data)}")