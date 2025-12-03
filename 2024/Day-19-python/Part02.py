from functools import cache
import os

def read_input(filename: str) -> tuple[list[str], list[str]]:
    designs: list[str] = []
    with open(filename, 'r') as f:
        towels: list[str] = f.readline().strip().split(', ')
        f.readline()
        for line in f.readlines():
            designs.append(line.strip())

    return designs, towels

@cache
def num_arrangements(design: list[str], towels: list[str], start: int=0,):
    if start >= len(design):
        return 1
    result = 0
    for towel in towels:
        if design[start: start+len(towel)] == towel:
            result += num_arrangements(design, towels, start+len(towel))
    return result

def main(designs: list[str], towels: list[str]) -> int:
    return sum(map(num_arrangements, designs, towels)) # BUG: List not hashable

if __name__ == "__main__":
    input_file: str = os.path.dirname(os.path.abspath(__file__)) + r"\\input.txt"
    data: tuple[list[str], list[str]] = read_input(input_file)

    designs: list[str] = data[0]
    towels: list[str] = data[1]
    
    print(f"Part 2: {main(designs, towels)}")
    