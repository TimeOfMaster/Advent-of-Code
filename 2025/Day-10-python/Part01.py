import os
import re

def read_input(filename: str) -> list[str]:
    """Read input file and return list of lines.

    Args:
        filename (str): Path to the input file

    Returns:
        list[str]: List of lines from the input file
    """
    
    with open(filename, "r") as f:
        return f.read().strip().splitlines()

def parse_line(line: str) -> tuple[list[int], list[list[int]]]:
    """Parse a line from the input into target state and button configurations.

    Args:
        line (str): Input line containing indicator lights, buttons, and joltage requirements

    Raises:
        ValueError: If no indicator lights pattern is found in the line

    Returns:
        tuple[list[int], list[list[int]]]: Target light states (0/1) and list of button configurations
    """
    
    # Extract indicator lights [.##.]
    lights_match: re.Match[str] | None = re.search(r'\[([.#]+)\]', line)
    if not lights_match:
        raise ValueError(f"No lights found in line: {line}")
    target: list[int] = [1 if c == '#' else 0 for c in lights_match.group(1)]
    
    # Extract button configurations (0,3,4)
    buttons: list[list[int]] = []
    for match in re.finditer(r'\(([0-9,]+)\)', line):
        button: list[int] = [int(x) for x in match.group(1).split(',')]
        buttons.append(button)
    
    return target, buttons

def solve_machine(target: list[int], buttons: list[list[int]]) -> int:
    """Solve a single machine using Gaussian elimination in GF(2) to find minimum button presses.

    Args:
        target (list[int]): Desired state of indicator lights (0 for off, 1 for on)
        buttons (list[list[int]]): List of button configurations, where each button is a list of light indices it toggles

    Returns:
        int: Minimum number of button presses needed to achieve the target configuration
    """
    
    n_lights: int = len(target)
    n_buttons: int = len(buttons)
    
    # Build the augmented matrix [A | b] where A is the coefficient matrix
    # Each column represents a button, each row represents a light
    # A[i][j] = 1 if button j toggles light i, 0 otherwise
    # b[i] = target[i] (desired state of light i)
    
    matrix: list[list[int]] = []
    for i in range(n_lights):
        row: list[int] = [0] * n_buttons
        for j, button in enumerate(buttons):
            if i in button:
                row[j] = 1
        row.append(target[i])  # Augment with target state
        matrix.append(row)
    
    # Gaussian elimination in GF(2)
    # Forward elimination to reduced row echelon form
    pivot_cols: list[int] = []  # Track which columns have pivots
    pivot_row: int = 0
    
    for col in range(n_buttons):
        # Find pivot
        found_pivot: bool = False
        for row_idx in range(pivot_row, n_lights):
            if matrix[row_idx][col] == 1:
                # Swap rows
                matrix[pivot_row], matrix[row_idx] = matrix[row_idx], matrix[pivot_row]
                found_pivot = True
                break
        
        if not found_pivot:
            continue
        
        pivot_cols.append(col)
        
        # Eliminate (both above and below for RREF)
        for row_idx in range(n_lights):
            if row_idx != pivot_row and matrix[row_idx][col] == 1:
                # XOR rows (in GF(2), addition is XOR)
                for c in range(n_buttons + 1):
                    matrix[row_idx][c] ^= matrix[pivot_row][c]
        
        pivot_row += 1
    
    # Check for inconsistency (a row like [0 0 0 ... 0 | 1])
    for row in matrix:
        if all(row[j] == 0 for j in range(n_buttons)) and row[-1] == 1:
            return 10**9  # No solution
    
    # Identify free variables (columns without pivots)
    free_vars: list[int] = [i for i in range(n_buttons) if i not in pivot_cols]
    
    # Try all combinations of free variables (2^k possibilities)
    # to find the solution with minimum button presses
    min_presses: float = float('inf')
    
    for mask in range(1 << len(free_vars)):
        solution: list[int] = [0] * n_buttons
        
        # Set free variables according to the mask
        for i, var in enumerate(free_vars):
            solution[var] = (mask >> i) & 1
        
        # Determine pivot variables based on free variables
        for i, col in enumerate(pivot_cols):
            # The value for this pivot variable
            val: int = matrix[i][-1]  # Target value
            for j in range(n_buttons):
                if j != col and matrix[i][j] == 1:
                    val ^= solution[j]
            solution[col] = val
        
        # Count button presses for this solution
        presses: int = sum(solution)
        min_presses = min(min_presses, presses)
    
    return int(min_presses)

def main(lines: list[str]) -> int:
    """Solve the puzzle for all machines and return the total minimum button presses.

    Args:
        lines (list[str]): List of input lines, each representing one machine configuration

    Returns:
        int: Total minimum button presses required for all machines
    """
    
    total_presses: int = 0
    for line in lines:
        target: list[int]
        buttons: list[list[int]]
        target, buttons = parse_line(line)
        presses: int = solve_machine(target, buttons)
        total_presses += presses
    
    return total_presses

if __name__ == "__main__":
    input_file: str = os.path.join(os.path.dirname(os.path.abspath(__file__)), "input.txt")
    lines: list[str] = read_input(input_file)
    result: int = main(lines)
    print(f"Part 1: {result}")
