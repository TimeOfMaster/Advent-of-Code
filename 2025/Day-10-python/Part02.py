import os
import re
from Part01 import read_input
from z3 import Int, Optimize, sat, Sum

def parse_line(line: str) -> tuple[list[int], list[list[int]]]:
    """Parse a line from the input into joltage requirements and button configurations.

    Args:
        line (str): Input line containing indicator lights, buttons, and joltage requirements

    Raises:
        ValueError: If no joltage requirements pattern is found in the line

    Returns:
        tuple[list[int], list[list[int]]]: Target joltage levels and list of button configurations
    """
    
    # Extract joltage requirements {3,5,4,7}
    joltage_match: re.Match[str] | None = re.search(r'\{([0-9,]+)\}', line)
    if not joltage_match:
        raise ValueError(f"No joltage requirements found in line: {line}")
    target: list[int] = [int(x) for x in joltage_match.group(1).split(',')]
    
    # Extract button configurations (0,3,4)
    buttons: list[list[int]] = []
    for match in re.finditer(r'\(([0-9,]+)\)', line):
        button: list[int] = [int(x) for x in match.group(1).split(',')]
        buttons.append(button)
    
    return target, buttons

def solve_machine_joltage(target: list[int], buttons: list[list[int]]) -> int:
    """Solve a single machine's joltage requirements using Z3 solver.

    Args:
        target (list[int]): Desired joltage levels for each counter
        buttons (list[list[int]]): List of button configurations

    Returns:
        int: Minimum number of button presses needed
    """
    
    n_counters: int = len(target)
    n_buttons: int = len(buttons)
    
    # Create Z3 optimizer (for minimization)
    opt = Optimize()
    
    # Create integer variables for button presses (non-negative)
    button_presses = [Int(f'button_{i}') for i in range(n_buttons)]
    
    # Add constraints: all button presses must be non-negative
    for i, bp in enumerate(button_presses):
        opt.add(bp >= 0)
    
    # Add constraints: each counter must reach its target value
    for counter_idx in range(n_counters):
        counter_sum = 0
        for button_idx, button in enumerate(buttons):
            if counter_idx in button:
                counter_sum = counter_sum + button_presses[button_idx]
        opt.add(counter_sum == target[counter_idx])
    
    # Minimize the total number of button presses
    total_presses = Sum(button_presses)
    opt.minimize(total_presses)
    
    # Solve
    if opt.check() == sat:
        model = opt.model()
        result: int = sum(model[bp].as_long() for bp in button_presses)
        return result
    else:
        return 0  # No solution

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
        presses: int = solve_machine_joltage(target, buttons)
        total_presses += presses
    
    return total_presses

if __name__ == "__main__":
    input_file: str = os.path.join(os.path.dirname(os.path.abspath(__file__)), "input.txt")
    lines: list[str] = read_input(input_file)
    result: int = main(lines)
    print(f"Part 2: {result}")
