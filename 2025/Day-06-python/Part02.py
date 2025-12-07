"""
Advent of Code 2025 - Day 6: Trash Compactor (Part 2)

Solves cephalopod math worksheets written right-to-left in columns.
Each column represents a problem with numbers read vertically (most significant digit at top)
and an operator at the bottom (+ or *).
"""

import os
import re
import math


def read_input(filename: str) -> list[tuple[str, ...]]:
    """
    Parse the cephalopod math worksheet input file.
    
    The input consists of a multi-line grid where:
    - Each column represents a math problem
    - Numbers are written vertically in each column
    - The last row contains operators (+ or *)
    - Columns are separated by spaces
    
    Args:
        filename: Path to the input file containing the math worksheet
        
    Returns:
        A list of tuples, where each tuple represents a column (problem) from the worksheet.
        Each tuple contains strings for the numbers and the operator.
        
    Example:
        Input file:
            123 328  51 64 
             45 64  387 23 
              6 98  215 314
            *   +   *   +
            
        Returns columns like: [('123', ' 45', '  6', '*'), ...]
    """
    with open(filename, "r") as f:
        data = f.read()
    
    # Split into lines
    data_list: list[str] = data.splitlines()
    
    # Determine column widths by splitting the last line (operators line) on spaces before operators
    col_len_list: list[int] = [len(col) for col in re.split(r"\s(?=[+\*])", data_list[-1])]
    
    # Parse each row into columns based on the determined widths
    col_list: list[list[str]] = []
    for row in data_list:
        cols: list[str] = []
        idx: int = 0
        for col_len in col_len_list:
            idx_next: int = idx + col_len
            cols.append(row[idx:idx_next])
            idx = idx_next + 1  # +1 to skip the space separator
        col_list.append(cols)
    
    # Transpose to get columns (problems)
    col_list_transposed: list[tuple[str, ...]] = list(zip(*col_list))
    
    return col_list_transposed



def main(data: list[tuple[str, ...]]) -> int:
    """
    Solve all cephalopod math problems and calculate the grand total.
    
    For each problem (column):
    1. Read numbers right-to-left, digit by digit (forming numbers from rightmost digits)
    2. Apply the operator (+ or *) to all numbers in the problem
    3. Sum all problem answers for the grand total
    
    Args:
        data: List of tuples representing columns/problems from the worksheet
        
    Returns:
        The grand total: sum of all individual problem answers
        
    Example:
        For column ('123', ' 45', '  6', '*'):
        - Reading right-to-left: 3 5 6 = 356, 2 4 (space) = 24, 1 (space) (space) = 1
        - Operation: 356 * 24 * 1 = 8544
    """
    total_value: int = 0

    for idx, col in enumerate(data):
        # Reverse each number string to read right-to-left
        # col[:-1] excludes the operator at the end
        reversed_numbers: list[list[str]] = [list(num[::-1]) for num in col[:-1]]
        
        # Transpose to group digits by position (rightmost, second-rightmost, etc.)
        rev_col: list[tuple[str, ...]] = list(zip(*reversed_numbers))
        
        # Join digits at each position to form the actual numbers
        join_numbers: list[int] = [int("".join(num).strip()) for num in rev_col]
        
        answer: int = 0
        operator: str = col[-1].strip()
        
        # Apply the appropriate operation
        match operator:
            case "+":
                answer = sum(join_numbers)
            case "*":
                answer = math.prod(join_numbers)
        
        total_value += answer
    
    return total_value

if __name__ == "__main__":

    input_file: str = os.path.dirname(os.path.abspath(__file__)) + r"\\input.txt"
    data = read_input(input_file)

    print(f"Part 2: {main(data)}")