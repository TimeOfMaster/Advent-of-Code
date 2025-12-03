import Part01, Part02, unittest, os, re
from dataclasses import dataclass

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
            pattern = r"p=(.+),(.+) v=(.+),(.+)"
            px, py, vx, vy = (int(z) for z in re.match(pattern, line).groups())
            robots.append((Pos(px, py), Pos(vx, vy)))
            
    return robots

class TestClawContraption(unittest.TestCase):
    def test_part01(self):
        input_file: str = os.path.dirname(os.path.abspath(__file__)) + r"\\testinput.txt"
        data: list[str] = read_input(input_file)
        safety_factor: int = Part01.main(data)
        self.assertEqual(safety_factor, 21)

    def test_part02(self):
        input_file: str = os.path.dirname(os.path.abspath(__file__)) + r"\\testinput.txt"
        data: list[str] = read_input(input_file)
        seconds: int = Part02.main(data)
        self.assertEqual(seconds, 52)

if __name__ == "__main__":
    unittest.main()