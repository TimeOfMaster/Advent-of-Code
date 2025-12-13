import os
from shapely.geometry import Point, Polygon

def read_input(filename: str) -> tuple[Polygon, list[tuple[int, int]]]:
    """Read red tile coordinates and create polygon of valid tiles.
    
    The polygon represents the loop formed by red tiles, which includes:
    - Red tiles (boundary vertices)
    - Green tiles connecting consecutive red tiles (boundary edges)
    - Green tiles inside the loop (interior)

    Args:
        filename (str): Path to input file containing comma-separated coordinates

    Returns:
        tuple[Polygon, list[tuple[int, int]]]: Polygon representing valid red/green area and list of red tile coordinates
    """
    
    coords: list[tuple[int, int]] = []
    
    with open(filename, "r") as f:
        content: str = f.read().strip()
    
    for line in content.splitlines():
        x, z = line.split(",")
        coords.append((int(x), int(z)))
    
    # Create polygon from coordinates
    polygon = Polygon(coords)
    
    return polygon, coords

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

def create_rectangle(x1: int, y1: int, x2: int, y2: int) -> Polygon:
    """Create a rectangular polygon from two opposite corner coordinates.
    
    Creates a closed polygon with vertices at the four corners of the rectangle.

    Args:
        x1 (int): X coordinate of first corner
        y1 (int): Y coordinate of first corner
        x2 (int): X coordinate of opposite corner
        y2 (int): Y coordinate of opposite corner

    Returns:
        Polygon: Polygon representing the rectangle
    """

    return Polygon([(x1, y1), (x1, y2), (x2, y2), (x2, y1)])

def is_rectangle_valid(corner1: tuple[int, int], corner2: tuple[int, int], polygon: Polygon) -> bool:
    """Check if rectangle with given corners is entirely within valid tile area.
    
    The rectangle is valid if it only contains red or green tiles (i.e., entirely
    within the polygon formed by the loop of red tiles).

    Args:
        corner1 (tuple[int, int]): First corner (x, y) coordinates
        corner2 (tuple[int, int]): Opposite corner (x, y) coordinates
        polygon (Polygon): Polygon representing valid red/green tile area

    Returns:
        bool: True if rectangle is completely within the polygon, False otherwise
    """
    
    x1, y1 = corner1
    x2, y2 = corner2
    
    # Create rectangle
    rect = create_rectangle(x1, y1, x2, y2)
    
    # Check if rectangle is within polygon
    return polygon.contains(rect)

def find_largest_rectangle(polygon: Polygon, red_tiles: list[tuple[int, int]]) -> int:
    """Find the largest rectangle with red tile corners that fits in the polygon.
    
    Tests all pairs of red tiles as potential rectangle corners. Only counts
    rectangles that are entirely within the valid area (red and green tiles).
    The rectangle can only include red or green tiles, not any other tiles.

    Args:
        polygon (Polygon): Polygon representing valid red/green tile area
        red_tiles (list[tuple[int, int]]): List of red tile coordinates (potential rectangle corners)

    Returns:
        int: Maximum rectangle area found using only red/green tiles
    """
    
    max_area = 0
    n = len(red_tiles)
    
    print(f"Checking {n} red tiles...")
    
    checked = 0
    for corner1 in red_tiles:
        for corner2 in red_tiles:
            checked += 1
            
            x1, y1 = corner1
            x2, y2 = corner2
            
            rect = create_rectangle(x1, y1, x2, y2)
            if polygon.contains(rect):
                area = calculate_rect_size(corner1, corner2)
                if area > max_area:
                    max_area = area
                    print(f"New max area: {max_area} between {corner1} and {corner2}")
    
    return max_area

if __name__ == "__main__":
    input_file: str = os.path.dirname(os.path.abspath(__file__)) + r"\\input.txt"
    polygon, red_tiles = read_input(input_file)
    
    print(f"Polygon area: {polygon.area}")
    print(f"Number of red tiles: {len(red_tiles)}")
    
    result = find_largest_rectangle(polygon, red_tiles)
    print(f"\nPart 2: {result}")