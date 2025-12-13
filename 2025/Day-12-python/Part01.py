"""Advent of Code 2025 - Day 12: Christmas Tree Farm (Part 1)

Determine how many regions beneath Christmas trees can fit all the required
presents. Each input describes odd-shaped presents (# cells) and rectangular
regions with counts of each shape. Presents may rotate or flip, must stay on the
grid, and cannot overlap; empty dots in a shape do not block other presents.
"""

import os


def read_input(file_path: str) -> list[str]:
    """Read the puzzle input file into a list of lines.

    Args:
        file_path (str): Path to the input file located alongside this script.

    Returns:
        list[str]: Lines of the puzzle input.
    """

    data: list[str] = []

    with open(file_path, "r") as f:
        data = f.read().splitlines()

    return data


def calculate_answer(data: list[str]) -> int:
    """Compute how many regions can fit all presents (simplified check).

    Args:
        data (list[str]): Raw input lines containing shape/region information.

    Returns:
        int: Count of regions that satisfy the placement condition.
    """

    answer: int = 0

    for line in data:
        if "x" in line:
            parts: list[str] = line.strip().split()
            size: list[int] = [int(x) for x in parts[0][:-1].split("x")]
            area: int = size[0] * size[1]
            presents: int = sum([int(x) for x in parts[1:]])
            answer += 1 if area >= presents * 9 else 0

    return answer


def main(data: list[str]) -> int:
    """Entry point: run the Part 1 calculation.

    Args:
        data (list[str]): Raw input lines for Part 1.

    Returns:
        int: The Part 1 answer.
    """

    result: int = calculate_answer(data)
    return result


if __name__ == "__main__":
    input_file: str = os.path.dirname(os.path.abspath(__file__)) + r"\\input.txt"
    data: list[str] = read_input(input_file)

    print(f"Part 1: {main(data)}")
