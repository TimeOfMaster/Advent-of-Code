import os

def read_input(filename: str) -> tuple[list[list[int]], list[list[int]]]:
    locks: list[list[int]] = []
    keys: list[list[int]] = []
    
    for block in open(filename).read().split("\n\n"):
        grid = list(zip(*block.splitlines()))
        if grid[0][0] == "#": 
            locks.append([row.count("#") - 1 for row in grid])
        else:
            keys.append([row.count("#") - 1 for row in grid])

    return locks, keys

def main(locks: list[list[int]], keys: list[list[int]]) -> int:
    total: int = 0

    for lock in locks:
        for key in keys:
            if all(x + y <= 5 for x, y in zip(lock, key)):
                total += 1

    return total

if __name__ == '__main__':
    input_file: str = os.path.dirname(os.path.abspath(__file__)) + r"\\input.txt"
    data: tuple[list[list[int]], list[list[int]]] = read_input(input_file)
    
    locks: list[list[int]] = data[0]
    keys: list[list[int]] = data[1]

    print(f"Part 1: {main(locks, keys)}")
    print(f"Part 2: Part 2 is just a button press ")