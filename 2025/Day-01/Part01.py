import os

def read_input(filename: str) -> list[str]:
    data: list[str] = []
    with open(filename, 'r') as f:
        data = [line.strip() for line in f.readlines()]
    return data

def dial(position: int, instruction: str, dial_size: int = 100) -> int:
    direction: str = instruction[0]
    distance: int = int(instruction[1:])
    
    if direction == "R":
        position = (position + distance) % dial_size
    elif direction == "L":
        position = (position - distance) % dial_size   
    return position

def main(data: list[str]) -> int:
    position: int = 50
    hits: int = 0
    
    for instruction in data:
        position = dial(position, instruction)
        if position == 0:
            hits += 1
    
    return hits

if __name__ == "__main__":
    input_file: str = os.path.dirname(os.path.abspath(__file__)) + r"\\input.txt"
    data: list[str] = read_input(input_file)
    
    print(f"Part 1: {main(data)}")