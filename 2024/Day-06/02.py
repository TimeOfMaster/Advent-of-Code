from dataclasses import dataclass
import unittest, os

def read_input(filename: str) -> tuple[int, int, list[str], tuple[int, int]]:
    grid: list[str] = []
    with open(filename, 'r') as f:
        for i, line in enumerate(f.readlines()):
            row = line.strip()
            if '^' in row:
                start: tuple[int, int] = (i, row.find('^'))
                row: str = row.replace('^', '.')
            grid.append(row)
    length: int = len(grid)
    width: int = len(grid[0])
    
    return length, width, grid, start

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
    def rotate_right(self):
        return Pos(self.j, -self.i)

def is_inbounds(pos: Pos, length: int, width: int) -> bool:
    return 0 <= pos.i < length and 0 <= pos.j < width

def get_guard_span(length: int, width: int, grid: list[str], start: tuple[int, int], new_obstacle=None) -> tuple[bool, set[Pos]]:
    # returns a set of visited positions by the guard
    # second value returns bool to indicate success of looping guard
    # option to add additional obstacle position
    pos: Pos = Pos(start[0], start[1])
    direction: Pos = Pos(-1, 0)  # up
    visited: set = set()
    states = {(pos, direction)}
    while is_inbounds(pos, length, width):
        visited.add(pos)
        # try to take a step
        dest: Pos = pos + direction
        if is_inbounds(dest, length, width) and (grid[dest.i][dest.j] == '#' or dest == new_obstacle):
            # turn right
            direction = direction.rotate_right()
        else:
            # step forward
            pos = dest
        new_state: tuple[Pos, Pos] = (pos, direction)
        if new_state in states:
            # infinite loop detected
            return True, visited
        states.add(new_state)
    return False, visited

def main(length: int, width: int, grid: list[str], start: tuple[int, int]) -> int:
    visited: set[Pos] = get_guard_span(length, width, grid, start)[1]
    result: int = 0
    obstacle_candidates: set[Pos] = visited - {start}
    for obstacle in obstacle_candidates:
        if get_guard_span(length, width, grid, start, new_obstacle=obstacle)[0]:
            result += 1
    return result

class TestGuardPath(unittest.TestCase):
    def test_example_part2(self):
        grid = [
            "....#.....",
            ".........#",
            "..........",
            "..#.......",
            ".......#..",
            "..........",
            ".#..^.....",
            "........#.",
            "#.........",
            "......#...",
        ]
        length: int = len(grid)
        width: int = len(grid[0])
        start: tuple[int, int] = (6, 4)
        result: int = main(length, width, grid, start)
        self.assertEqual(result, 6)

if __name__ == '__main__':
    input_file = os.path.dirname(os.path.abspath(__file__)) + r"\\input.txt"
    
    input: tuple[int, int, list[str], tuple[int, int]] = read_input(input_file)
    length: int = input[0]
    width: int = input[1]
    grid: list[str] = input[2]
    start: tuple[int, int] = input[3]
    
    print(f'Part 2: {main(length, width, grid, start)}')
    
    unittest.main()