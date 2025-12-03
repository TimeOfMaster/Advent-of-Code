from math import log10
import os, unittest
from functools import lru_cache

def read_input(filename: str) -> list[int]:
    numbers: list[int] = []
    with open(filename, 'r') as f:
        numbers = list(map(int, f.readline().split()))
    return numbers

@lru_cache(None)
def calc(n: int, blinks: int) -> int:
	if blinks == 0:
		return 1

	if n == 0:
		return calc(1, blinks - 1)

	n_digits: int = int(log10(n)) + 1
	if n_digits % 2 == 0:
		power: int = 10**(n_digits // 2)
		return calc(n // power, blinks - 1) + calc(n % power, blinks - 1)

	return calc(n * 2024, blinks - 1)

def main(numbers: list[int]) -> int:
    return sum(calc(n, 75) for n in numbers)

if __name__ == "__main__":
	input_file: str = os.path.dirname(os.path.abspath(__file__)) + r"\\input.txt"
	data: list[int] = read_input(input_file)
 
	print(f"Part 2: {main(data)}")
	
	unittest.main()
