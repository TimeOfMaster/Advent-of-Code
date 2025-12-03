import os

def read_input(filename: str) -> list[list[int]]:
    """Read and parse input file containing battery banks.

    Args:
        filename (str): Path to the input file where each line contains
                       a sequence of digits representing battery joltage ratings

    Returns:
        list[list[int]]: List of battery banks, where each bank is a list of
                        joltage ratings (digits 1-9)
    """
    
    data: list[list[int]] = []
    with open(filename, 'r') as f:
        for line in f:
            chars = list(line)
            data.append([int(x) for x in chars if x.isdigit()])
            
    return data

def activate_batteries(bank: list[int]) -> int:
    """Find the maximum joltage by selecting exactly 12 batteries in order.
    
    Uses a greedy algorithm: at each step, select the largest digit that still
    allows selecting enough batteries from the remaining sequence.

    Args:
        bank (list[int]): List of battery joltage ratings (digits 1-9)

    Returns:
        int: Maximum joltage (12-digit number) possible from the bank
    """
    # To maximize the number, greedily pick the largest digits
    # We need 12 batteries total
    selected = []
    remaining_needed = 12
    start_index = 0
    
    while remaining_needed > 0:
        # Find the maximum digit in the range where we can still pick enough batteries after it
        max_digit = -1
        max_index = -1
        
        # We need to leave at least (remaining_needed - 1) batteries after our choice
        end_range = len(bank) - (remaining_needed - 1)
        
        for i in range(start_index, end_range):
            if bank[i] > max_digit:
                max_digit = bank[i]
                max_index = i
        
        selected.append(max_digit)
        start_index = max_index + 1
        remaining_needed -= 1
    
    return int("".join(str(d) for d in selected))
                

def main(data) -> int:
    return sum(activate_batteries(bank) for bank in data)

if __name__ == "__main__":
    input_file: str = os.path.dirname(os.path.abspath(__file__)) + r"\\input.txt"
    data: list[list[int]] = read_input(input_file)
    
    print(f"Part 2: {main(data)}")
