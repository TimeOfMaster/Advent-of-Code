import os

def read_input(filename: str) -> tuple[int, int, list[str], list[str]]:
    grid: list[str] = []
    with open(filename, 'r') as f:
        lines: list[str] = f.read().split('\n')
        grid = [list(line) for line in lines]
    length: int = len(grid)
    width: int = len(grid[0])
    visited_grid: list[str] = [[0 for _ in range(length)] for _ in range(width)]

    return length, width, grid, visited_grid

def next_unvisited(length: int, width: int, visited_grid: list[str]) -> tuple[int, int] | tuple[bool, bool]:
    for x in range(length):
        for y in range(width):
            if visited_grid[x][y] == 0:
                return x, y
    return False, False

def get_area(x: int, y: int, grid: list[str], visited_grid: list[str], length: int, width: int) -> list[tuple[int, int]]:
    key: str = grid[x][y]
    area: list[tuple[int, int]] = [(x, y)]
    visited_grid[x][y] = 1
    unvisited_points: list[tuple[int, int]] = [(x, y)]
    directions: list[tuple[int, int]] = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    while(len(unvisited_points) > 0):
        x, y = unvisited_points.pop()
        for dx, dy in directions:
            if 0 <= x + dx < length and 0 <= y + dy < width and grid[x + dx][y + dy] == key:
                if (x + dx, y + dy) not in unvisited_points and (x + dx, y + dy) not in area:
                    unvisited_points.append((x + dx, y + dy))
                if (x + dx, y + dy) not in area:
                    area.append((x + dx, y + dy))
                    visited_grid[x + dx][y + dy] = 1
    return area

def area_price(area: list[tuple[int, int]], length: int, width: int) -> int:
    result: int = 0
    for x, y in area:
        corners: list[tuple[int, int]] = [[(-1, -1), (0, -1), (-1, 0)], 
                   [(0, -1), (1, -1), (1, 0)], 
                   [(1, 0), (1, 1), (0, 1)], 
                   [(0, 1), (-1, 1), (-1, 0)]]
        for directions in corners:
            point_neighbours: int = 0
            special_neighbour: int = 0
            for dx, dy in directions:
                if 0 <= x + dx < length and 0 <= y + dy < width and (x + dx, y + dy) in area:
                    point_neighbours += 1
                    if abs(dx) + abs(dy) == 2:
                        special_neighbour += 1
            if point_neighbours == 0 or (point_neighbours == 1 and special_neighbour == 1):
                result += 1
            if point_neighbours == 2:
                result += 1/3
    return int(len(area) * round(result))

def main(length: int, width: int, grid: list[str], visited_grid: list[str]) -> int:
    result: int = 0
    while True:
        x, y = next_unvisited(length, width, visited_grid)
        if x is False:
            break
        area: list[tuple[int, int]] = get_area(x, y, grid, visited_grid, length, width)
        result += area_price(area, length, width)
    
    return result

if __name__ == "__main__":
    input_file: str = os.path.dirname(os.path.abspath(__file__)) + r"\\input.txt"
    data: tuple[int, int, list[str], list[str]] = read_input(input_file)

    length: int = data[0]
    width: int = data[1]
    grid: list[str] = data[2]
    visited_grid: list[str] = data[3]
    
    print(f"Part 2: {main(length, width, grid, visited_grid)}")