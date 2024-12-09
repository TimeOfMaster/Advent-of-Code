from dataclasses import dataclass
from collections import defaultdict
from typing import Any
import math, os, unittest

def read_input(filename: str) -> tuple[int, int, list[str]]:
    grid: list[str] = []
    with open(filename, 'r') as f:
        for i, line in enumerate(f.readlines()):
            grid.append(line.strip())
    length: int = len(grid)
    width: int = len(grid[0])
    
    return length, width, grid

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
    def is_inbounds(self, length: int, width: int):
        return 0 <= self.i < length and 0 <= self.j < width
    def get_gcd_vec(self):
        gcd = math.gcd(self.i, self.j)
        return Pos(self.i // gcd, self.j // gcd)

def antennae(length: int, width: int, grid: list[str]) -> defaultdict[Any, list]:
# populate dict of frequency -> [antenna positions]
    antennae: defaultdict[Any, list] = defaultdict(list)
    for i in range(length):
        for j in range(width):
            if grid[i][j] != '.':
                antennae[grid[i][j]].append(Pos(i, j))
    return antennae

def main(length: int, width: int, grid: list[str]) -> int:

    antennaes: defaultdict[Any, list] = antennae(length, width, grid)

    antinodes: set = set()
    for antenna_group in antennaes.values():
        for i, a1 in enumerate(antenna_group):
            for j in range(i+1, len(antenna_group)):
                a2 = antenna_group[j]
                vec = a2-a1
                
                gcd_vec = vec.get_gcd_vec()
                temp = a1
                while temp.is_inbounds(length=length, width=width):
                    antinodes.add(temp)
                    temp += gcd_vec
                temp = a1
                while temp.is_inbounds(length=length, width=width):
                    antinodes.add(temp)
                    temp -= gcd_vec
    return len(antinodes)

class TestAntinodeCalculation(unittest.TestCase):
    def test_original_example_updated(self):
        grid: list[str] = [
            "............",
            "........0...",
            ".....0......",
            ".......0....",
            "....0.......",
            "......A.....",
            "............",
            "............",
            "........A...",
            ".........A..",
            "............",
            "............"
        ]
        length: int = len(grid)
        width: int = len(grid[0])
        expected_antinode_count: int = 34
        result: int = main(length, width, grid)
        self.assertEqual(result, expected_antinode_count)

if __name__ == "__main__":
    input_file: str = os.path.dirname(os.path.abspath(__file__)) + r"\\input.txt"
    data: tuple[int, int, list[str]] = read_input(input_file)
    
    length: int = data[0]
    width: int = data[1]
    grid: list[str] = data[2]
    
    print(f"Part 2: {main(length, width, grid)}")
    
    unittest.main()