"""
Advent of Code 2025 - Day 6: Trash Compactor (Part 1)

Solves cephalopod math worksheets where problems are arranged in vertical columns.
Each column contains numbers stacked vertically with an operator at the bottom (+ or *).
"""

import os


def read_input(filename: str) -> list[list[int | str]]:
    """
    Parse the cephalopod math worksheet input file.
    
    The input consists of a multi-line grid where:
    - Each column represents a math problem
    - Numbers are written vertically in each column (reading top to bottom)
    - The last row contains operators (+ or *)
    - Columns are separated by spaces
    
    Args:
        filename: Path to the input file containing the math worksheet
        
    Returns:
        A list of lists, where each inner list represents a column (problem).
        Each column contains integers (the numbers) followed by a string (the operator).
        
    Example:
        Input file:
            123 328  51 64
             45  64 387 23
              6  98 215 314
            *   +   *   +
            
        Returns: [[123, 45, 6, '*'], [328, 64, 98, '+'], ...]
    """
    with open(filename, 'r') as f:
        lines: list[str] = [line.strip() for line in f if line.strip()]
    
    # Last line contains operators
    operators: list[str] = lines[-1].split()
    
    # All other lines contain numbers
    number_rows: list[list[int]] = []
    for line in lines[:-1]:
        number_rows.append([int(x) for x in line.split()])
    
    # Transpose to get columns and combine with operators
    data: list[list[int | str]] = []
    num_cols: int = len(operators)
    
    for col_idx in range(num_cols):
        column: list[int | str] = [number_rows[row_idx][col_idx] for row_idx in range(len(number_rows))]
        column.append(operators[col_idx])
        data.append(column)
    
    return data



def process_data(data: list[int | str]) -> int:
    """
    Process a single column (problem) and calculate the result.
    
    Takes all numbers in the column and applies the operator (+ or *) sequentially
    from top to bottom.
    
    Args:
        data: A list containing integers (numbers) with the operator as the last element
        
    Returns:
        The result of applying the operator to all numbers in sequence
        
    Raises:
        ValueError: If an unknown operator is encountered
        
    Example:
        Input: [123, 45, 6, '*']
        Process: 123 * 45 * 6 = 33210
        Output: 33210
    """
    result: int = int(data[0])
    
    for i in range(1, len(data) - 1):
        operator: str = str(data[-1])
        operand: int = int(data[i])
        
        if operator == "+":
            result += operand
        elif operator == "*":
            result *= operand
        else:
            raise ValueError(f"Unknown operator: {operator}")
    
    return result


def main(data: list[list[int | str]]) -> int:
    """
    Solve all cephalopod math problems and calculate the grand total.
    
    For each problem (column):
    1. Read numbers top to bottom
    2. Apply the operator (+ or *) sequentially to all numbers
    3. Sum all problem answers for the grand total
    
    Args:
        data: List of lists representing columns/problems from the worksheet
        
    Returns:
        The grand total: sum of all individual problem answers
        
    Example:
        Input: [[123, 45, 6, '*'], [328, 64, 98, '+']]
        Problem 1: 123 * 45 * 6 = 33210
        Problem 2: 328 + 64 + 98 = 490
        Grand total: 33210 + 490 = 33700
    """
    results: list[int] = []
    
    for column_data in data:
        result: int = process_data(column_data)
        results.append(result)
    
    return sum(results)

if __name__ == "__main__":
    input_file: str = os.path.dirname(os.path.abspath(__file__)) + r"\\input.txt"
    data = read_input(input_file)
    
    print(f"Part 1: {main(data)}")