"""Advent of Code 2025 - Day 4: Printing Department (Part 1)

The forklifts in the printing department need to access rolls of paper (@) arranged
on a grid. A roll of paper can only be accessed if it has fewer than 4 neighboring
rolls in the 8 adjacent positions (including diagonals).

This solution counts how many rolls of paper can initially be accessed by the forklifts.
"""

import os

def read_input(filename: str) -> list[list[str]]:
    """Read the input file and parse it into a 2D grid.

    Args:
        filename (str): Path to the input file containing the grid layout

    Returns:
        list[list[str]]: 2D grid where each cell is a character from the input
    """
    
    with open(filename, 'r') as f:
        return [list(line.strip()) for line in f if line.strip()]

def get_neighbors(pos: tuple[int, int], grid: list[list[str]]) -> list[tuple[int, int]]:
    """Get all valid neighbors (including diagonals) for a given position.

    Args:
        pos (tuple[int, int]): The (row, col) position to find neighbors for
        grid (list[list[str]]): The 2D grid of paper rolls

    Returns:
        list[tuple[int, int]]: List of (row, col) tuples for all valid neighbor positions
    """
    
    rows: int = len(grid)
    cols: int = len(grid[0])
    neighbors: list[tuple[int, int]] = []
    
    directions: list[tuple[int, int]] = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),          (0, 1),
        (1, -1),  (1, 0), (1, 1),
    ]
    
    for direction_row, direction_col in directions:
        neighbor_row, neighbor_col = pos[0] + direction_row, pos[1] + direction_col
        if 0 <= neighbor_row < rows and 0 <= neighbor_col < cols:
            neighbors.append((neighbor_row, neighbor_col))
    return neighbors

def get_num_paper_neighbors(pos: tuple[int, int], grid: list[list[str]]) -> int:
    """Count how many neighboring positions contain paper rolls (@).

    Args:
        pos (tuple[int, int]): The (row, col) position to check neighbors for
        grid (list[list[str]]): The 2D grid of paper rolls

    Returns:
        int: Number of adjacent positions (including diagonals) that contain '@'
    """
    
    neighbors: list[tuple[int, int]] = get_neighbors(pos, grid)
    
    count: int = 0
    for neighbor in neighbors:
        if grid[neighbor[0]][neighbor[1]] == "@":
            count += 1
    return count

def count_accessible(grid: list[list[str]]) -> int:
    """Count how many paper rolls can be accessed by forklifts.
    
    A paper roll (@) can be accessed if it has fewer than 4 neighboring paper rolls
    in the 8 adjacent positions (including diagonals).

    Args:
        grid (list[list[str]]): The 2D grid of paper rolls

    Returns:
        int: Number of accessible paper rolls
    """
    count_accessible: int = 0
    
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == "@":
                num_paper_neighbors: int = get_num_paper_neighbors((row, col), grid)
                # Forklift can access if fewer than 4 neighboring paper rolls
                if num_paper_neighbors < 4:
                    count_accessible += 1               
    
    return count_accessible

def main(grid: list[list[str]]) -> int:
    return count_accessible(grid)

if __name__ == "__main__":
    input_file: str = os.path.dirname(os.path.abspath(__file__)) + r"\\input.txt"
    data: list[list[str]] = read_input(input_file)
    
    print(f"Part 1: {main(data)}")
