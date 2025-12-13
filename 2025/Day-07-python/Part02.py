"""Advent of Code 2025 - Day 7: Laboratories (Part 2)

Simulates a quantum tachyon manifold using the many-worlds interpretation.

In a quantum manifold, a single tachyon particle takes BOTH paths at each splitter,
creating separate timelines. We need to count the total number of distinct timelines
that result from all possible paths through the manifold.

Key differences from Part 1:
- Part 1: Count how many times we split (classical physics)
- Part 2: Count how many different complete paths exist (quantum physics)

Each timeline represents a unique sequence of left/right choices at splitters.
For example:
- Timeline 1: Always go left at every splitter
- Timeline 2: Always go right at every splitter  
- Timeline 3: Go left, then right, then left...
- etc.

The answer grows exponentially with the number of splitters, but memoization helps
by caching results when paths converge at the same position.
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


def count_timelines(
    grid: tuple[str, ...], row: int, col: int, memo: dict[tuple[int, int], int]
) -> int:
    """Count the number of distinct timelines from a given position.

    Uses memoization to cache results and avoid recalculating paths that converge
    at the same position.

    Args:
        grid: The manifold diagram as a tuple of strings (immutable for efficiency)
        row: Current row position
        col: Current column position
        memo: Dictionary cache mapping (row, col) -> number of timelines from that position

    Returns:
        The number of distinct timelines (complete paths) from this position to any exit
    """
    # Base case: out of bounds - this is one complete timeline
    if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]):
        return 1

    # Check memo
    if (row, col) in memo:
        return memo[(row, col)]

    cell: str = grid[row][col]
    timeline_count: int = 0

    # If we hit a splitter, the timeline splits into two
    if cell == "^":
        # Left timeline: particle goes left one step then continues down
        if col - 1 >= 0:
            timeline_count += count_timelines(grid, row + 1, col - 1, memo)
        else:
            # Left path goes out of bounds immediately
            timeline_count += 1

        # Right timeline: particle goes right one step then continues down
        if col + 1 < len(grid[0]):
            timeline_count += count_timelines(grid, row + 1, col + 1, memo)
        else:
            # Right path goes out of bounds immediately
            timeline_count += 1
    else:
        # Continue downward in the same timeline
        timeline_count += count_timelines(grid, row + 1, col, memo)

    memo[(row, col)] = timeline_count
    return timeline_count


def main(starting_pos: tuple[int, int], grid: list[str]) -> int:
    """Calculate the total number of distinct timelines in the quantum manifold.

    Args:
        starting_pos: (row, col) position of the starting marker 'S'
        grid: The manifold diagram as a list of strings

    Returns:
        Total number of distinct timelines (unique paths through the manifold)
    """
    # Count all possible timelines starting from S
    memo: dict[tuple[int, int], int] = {}
    start_row: int
    start_col: int
    start_row, start_col = starting_pos
    grid_tuple: tuple[str, ...] = tuple(grid)
    result: int = count_timelines(grid_tuple, start_row + 1, start_col, memo)

    return result


if __name__ == "__main__":
    input_file: str = os.path.dirname(os.path.abspath(__file__)) + r"\\input.txt"
    starting_pos: tuple[int, int]
    grid: list[str]
    starting_pos, grid = read_input(input_file)

    print(f"Part 2: {main(starting_pos, grid)}")
