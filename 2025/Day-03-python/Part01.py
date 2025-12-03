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
    """Find the maximum joltage by selecting exactly 2 batteries in order.
    
    Checks all possible pairs of batteries while maintaining their left-to-right
    order in the bank. The joltage is formed by concatenating the two digits.

    Args:
        bank (list[int]): List of battery joltage ratings (digits 1-9)

    Returns:
        int: Maximum joltage (2-digit number) possible from the bank
    """
    max_capacity: int = 0
    # Check all pairs where i comes before j (maintaining order)
    for i in range(len(bank)):
        for j in range(i + 1, len(bank)):
            capacity: int = int(str(bank[i]) + str(bank[j]))
            max_capacity = max(max_capacity, capacity)
                    
    return max_capacity
                

def main(data) -> int:
    return sum(activate_batteries(bank) for bank in data)

if __name__ == "__main__":
    input_file: str = os.path.dirname(os.path.abspath(__file__)) + r"\\input.txt"
    data: list[list[int]] = read_input(input_file)
    
    print(f"Part 1: {main(data)}")
