"""Advent of Code 2025 - Day 7: Laboratories (Part 1)

Simulates a classical tachyon manifold where beams split when encountering splitters.

The manifold is a 2D grid where:
- 'S': Starting position where the tachyon beam enters
- '.': Empty space (beam passes through)
- '^': Splitter (beam stops, two new beams emerge left and right, then continue downward)

Tachyon beams always move downward. When a beam hits a splitter, it stops and creates
two new beams that move one step left/right, then continue moving downward.

Example:
    .......S.......  <- Beam enters at S
    .......|.......  <- Moves down
    ......|^|......  <- Hits splitter, creates left and right beams
    ......|.|......  <- Both beams continue downward

"""

import os


def read_input(file_path: str) -> tuple[tuple[int, int], list[str]]:
    """Read and parse the manifold diagram from input file.

    Args:
        file_path: Path to the input file containing the manifold diagram

    Returns:
        A tuple of (starting_position, grid) where:
        - starting_position is (row, col) of the 'S' marker
        - grid is a list of strings representing the manifold
    """
    data: list[str] = []
    starting_pos: tuple[int, int] = (0, 0)

    with open(file_path, "r") as f:
        data = f.read().splitlines()

    for r, row in enumerate(data):
        for c, cell in enumerate(row):
            if cell == "S":
                starting_pos = (r, c)
                return starting_pos, data

    return (-1, -1), data


def simulate_beam(
    grid: list[str], row: int, col: int, visited: set[tuple[int, int]]
) -> int:
    """Recursively simulate a tachyon beam moving through the manifold.

    Uses DFS to follow the beam path, counting splits when encountering splitters.

    Args:
        grid: The manifold diagram as a list of strings
        row: Current row position of the beam
        col: Current column position of the beam
        visited: Set of already visited positions (prevents infinite loops)

    Returns:
        The total number of beam splits encountered from this position onward
    """
    # Base case: out of bounds
    if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]):
        return 0

    # Base case: already visited this position
    state = (row, col)
    if state in visited:
        return 0

    visited.add(state)

    cell: str = grid[row][col]
    split_count: int = 0

    # If we hit a splitter, split the beam
    if cell == "^":
        split_count = 1
        # Spawn two beams: one goes left one step then down, one goes right one step then down
        if col - 1 >= 0:
            split_count += simulate_beam(grid, row + 1, col - 1, visited)
        if col + 1 < len(grid[0]):
            split_count += simulate_beam(grid, row + 1, col + 1, visited)
    else:
        # Continue downward
        split_count += simulate_beam(grid, row + 1, col, visited)

    return split_count


def main(starting_pos: tuple[int, int], grid: list[str]) -> int:
    """Calculate the total number of beam splits in the manifold.

    Args:
        starting_pos: (row, col) position of the starting marker 'S'
        grid: The manifold diagram as a list of strings

    Returns:
        Total number of times the beam is split
    """
    # Start simulation from S, moving downward
    visited: set[tuple[int, int]] = set()
    start_row: int
    start_col: int
    start_row, start_col = starting_pos
    result: int = simulate_beam(grid, start_row + 1, start_col, visited)

    return result


if __name__ == "__main__":
    input_file: str = os.path.dirname(os.path.abspath(__file__)) + r"\\input.txt"
    starting_pos: tuple[int, int]
    grid: list[str]
    starting_pos, grid = read_input(input_file)

    print(f"Part 1: {main(starting_pos, grid)}")
