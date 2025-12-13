import os


def read_input(filename: str):
    """Read red tile coordinates from input file.

    Args:
        filename (str): Path to input file containing comma-separated coordinates

    Returns:
        set[tuple[int, int]]: Set of red tile (x, y) coordinates
    """

    with open(filename, "r") as f:
        content: str = f.read().strip()

    data: set[tuple[int, int]] = set()
    for line in content.splitlines():
        x: str
        z: str
        x, z = line.split(",")
        data.add((int(x), int(z)))
    return data


def calculate_rect_size(corner1: tuple[int, int], corner2: tuple[int, int]) -> int:
    """Calculate area of rectangle defined by two opposite corners.

    Area is calculated as (width + 1) * (height + 1) to count tiles inclusively.

    Args:
        corner1 (tuple[int, int]): First corner (x, y) coordinates
        corner2 (tuple[int, int]): Opposite corner (x, y) coordinates

    Returns:
        int: Rectangle area in tiles
    """

    length: int = abs(corner1[0] - corner2[0]) + 1
    width: int = abs(corner1[1] - corner2[1]) + 1
    return length * width


def get_largest_rect(data: set[tuple[int, int]]) -> int:
    """Find the largest rectangle using two red tiles as opposite corners.

    Tests all pairs of red tiles and calculates the area of the rectangle
    formed by using them as opposite corners. Returns the maximum area found.

    Args:
        data (set[tuple[int, int]]): Set of red tile coordinates

    Returns:
        int: Maximum rectangle area found
    """
    max_area: int = 0

    for corner1 in data:
        for corner2 in data - {corner1}:
            area: int = calculate_rect_size(corner1, corner2)
            print(f"Area between {corner1} and {corner2}: {area}")
            if area > max_area:
                max_area = area

    return max_area


if __name__ == "__main__":
    input_file: str = os.path.dirname(os.path.abspath(__file__)) + r"\\input.txt"
    data = read_input(input_file)

    print(f"Part 1: {get_largest_rect(data)}")
