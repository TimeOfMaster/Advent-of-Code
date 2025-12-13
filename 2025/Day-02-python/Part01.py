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
    with open(filename, "r") as f:
        parts: list[str] = f.read().split(",")
        for part in parts:
            a, b = part.split("-")
            data.append((int(a), int(b)))
    return data


def verify_id(id: int) -> bool:
    """Check if an ID is valid based on the pattern repetition rule.

    An ID is invalid if it consists of a sequence of digits repeated exactly twice.
    For example:
    - 55 ("5" repeated twice) is invalid
    - 6464 ("64" repeated twice) is invalid
    - 123123 ("123" repeated twice) is invalid
    - 101 (odd length, cannot be a pattern repeated twice) is valid
    - 1234 ("12" != "34") is valid

    Args:
        id (int): The ID number to verify

    Returns:
        bool: True if the ID is valid, False if invalid (pattern repeated twice)
    """

    id_str = str(id)
    length = len(id_str)

    # Check if the length is even (required for a pattern repeated twice)
    if length % 2 != 0:
        return True  # Valid ID (can't be a pattern repeated twice with odd length)

    # Split the string in half and check if both halves are identical
    half = length // 2
    first_half = id_str[:half]
    second_half = id_str[half:]

    if first_half == second_half:
        return False  # Invalid ID (pattern repeated twice)

    return True  # Valid ID


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

    print(f"Part 1: {main(data)}")
