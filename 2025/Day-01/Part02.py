import os

def read_input(filename: str) -> list[str]:
    data: list[str] = []
    with open(filename, 'r') as f:
        data = [line.strip() for line in f.readlines()]
    return data

def dial(position: int, instruction: str, dial_size: int = 100) -> tuple[int, int]:
    direction: str = instruction[0]
    distance: int = int(instruction[1:])
    hits: int = 0
    new_position: int = 0
    
    if direction == "R":
        # Count how many times we cross or land on 0 going right
        # From position, we need to reach 0, then every dial_size after that
        if position == 0:
            # Starting at 0, we hit it again after every full loop
            hits = distance // dial_size
        else:
            # Distance to first 0 is (dial_size - position)
            # Then we hit 0 every dial_size after that
            remaining = distance - (dial_size - position)
            if distance >= (dial_size - position):
                hits = 1 + max(0, remaining // dial_size)
        new_position = (position + distance) % dial_size
    elif direction == "L":
        # Count how many times we cross or land on 0 going left
        if position == 0:
            # Starting at 0, we hit it again after every full loop
            hits = distance // dial_size
        else:
            # Distance to first 0 is position
            # Then we hit 0 every dial_size after that
            remaining = distance - position
            if distance >= position:
                hits = 1 + max(0, remaining // dial_size)
        new_position = (position - distance) % dial_size
    
    return new_position, hits

def main(data: list[str]) -> int:
    position: int = 50
    hits: int = 0
    
    for instruction in data:
        position, hits_on_dial = dial(position, instruction)
        if hits_on_dial:
            hits += hits_on_dial
    
    return hits

if __name__ == "__main__":
    input_file: str = os.path.dirname(os.path.abspath(__file__)) + r"\\input.txt"
    data: list[str] = read_input(input_file)
    
    print(f"Part 2: {main(data)}")