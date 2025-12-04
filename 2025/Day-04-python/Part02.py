"""Advent of Code 2025 - Day 4: Printing Department (Part 2)

This solution extends Part 1 by simulating the iterative removal of accessible paper rolls.
Once a roll is removed, new rolls may become accessible (having fewer than 4 neighbors).
The process repeats until no more rolls can be accessed.

The algorithm:
1. Find all accessible paper rolls (< 4 neighbors)
2. Remove them by marking as 'X'
3. Repeat until no more rolls become accessible
4. Return the total number of rolls removed
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

def count_and_mark_accessible(grid: list[list[str]]) -> int:
    """Count and mark accessible paper rolls for removal.
    
    A paper roll (@) can be accessed if it has fewer than 4 neighboring paper rolls.
    Accessible rolls are marked with 'X' to indicate removal, which may make other
    rolls accessible in subsequent iterations.

    Args:
        grid (list[list[str]]): The 2D grid of paper rolls (modified in-place)

    Returns:
        int: Number of accessible paper rolls found and marked in this iteration
    """
    count_accessible: int = 0
    
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == "@":
                num_paper_neighbors: int = get_num_paper_neighbors((row, col), grid)
                if num_paper_neighbors < 4:
                    count_accessible += 1
                    # Mark as removed so it won't be counted as a neighbor in next iteration
                    grid[row][col] = "X"           
    
    return count_accessible
    
def main(grid: list[list[str]]) -> int:
    """Iteratively remove accessible paper rolls until none remain.
    
    Repeatedly finds and removes accessible paper rolls (< 4 neighbors) until
    no more rolls can be accessed. Each removal may expose new accessible rolls.

    Args:
        grid (list[list[str]]): The 2D grid of paper rolls (modified in-place)

    Returns:
        int: Total number of paper rolls removed across all iterations
    """
    count_removed: int = 0
    while True:
        count_accessible: int = count_and_mark_accessible(grid)
        count_removed += count_accessible
        # Stop when no more rolls can be accessed
        if count_accessible == 0:
            break
        
    return count_removed

if __name__ == "__main__":
    input_file: str = os.path.dirname(os.path.abspath(__file__)) + r"\\input.txt"
    data: list[list[str]] = read_input(input_file)
    
    print(f"Part 2: {main(data)}")
