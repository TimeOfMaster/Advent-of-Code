import os

def read_input(filename: str) -> list[tuple[int, int]]:
    """Read and parse input file containing ID ranges.

    Args:
        filename (str): Path to the input file containing comma-separated ranges
                       in the format "start-end,start-end,..."

    Returns:
        list[tuple[int, int]]: List of tuples where each tuple contains
                              (start_id, end_id) representing an ID range
    """
    
    data: list[tuple[int, int]] = []
    with open(filename, 'r') as f:
        parts: list[str] = f.read().split(",")
        for part in parts:
            a, b = part.split("-")
            data.append((int(a), int(b)))
    return data

def verify_id(id: int) -> bool:
    """Check if an ID is valid based on the pattern repetition rule.
    
    An ID is invalid if it consists of a sequence of digits repeated at least twice.
    For example:
    - 55 ("5" repeated 2 times) is invalid
    - 6464 ("64" repeated 2 times) is invalid
    - 12341234 ("1234" repeated 2 times) is invalid
    - 123123123 ("123" repeated 3 times) is invalid
    - 1212121212 ("12" repeated 5 times) is invalid
    - 1111111 ("1" repeated 7 times) is invalid
    - 101 (no repeating pattern) is valid
    - 1234 (no repeating pattern) is valid

    Args:
        id (int): The ID number to verify

    Returns:
        bool: True if the ID is valid, False if invalid (pattern repeated at least twice)
    """
    
    id_str = str(id)
    length = len(id_str)
    
    # Try all possible pattern lengths (from 1 to half the string length)
    # A pattern must repeat at least twice, so max pattern length is length // 2
    for pattern_len in range(1, length // 2 + 1):
        # Check if the total length is divisible by the pattern length
        if length % pattern_len == 0:
            pattern = id_str[:pattern_len]
            # Check if the entire string is this pattern repeated
            repetitions = length // pattern_len
            if pattern * repetitions == id_str:
                return False  # Invalid ID (pattern repeated at least twice)
    
    return True  # Valid ID (no repeating pattern found)

def verify_id_range(id_range: tuple[int, int]) -> int:
    """Calculate the sum of all invalid IDs within a given range.

    Args:
        id_range (tuple[int, int]): A tuple containing (start, end) inclusive range

    Returns:
        int: Sum of all invalid IDs found in the range
    """
    
    sum_invalid_ids: int = 0
    for id in range(id_range[0], id_range[1] + 1):
        if not verify_id(id):
            sum_invalid_ids += id

    return sum_invalid_ids

def main(data: list[tuple[int, int]]) -> int:
    """Process all ID ranges and calculate the total sum of invalid IDs.
    
    Args:
        data (list[tuple[int, int]]): List of ID ranges to process
    
    Returns:
        int: Total sum of all invalid IDs across all ranges
    """
    sum_invalid_ids: int = 0
    for id_range in data:
        sum_invalid_ids += verify_id_range(id_range)
    
    return sum_invalid_ids

if __name__ == "__main__":
    input_file: str = os.path.dirname(os.path.abspath(__file__)) + r"\\input.txt"
    data: list[tuple[int, int]] = read_input(input_file)
    
    print(f"Part 2: {main(data)}")