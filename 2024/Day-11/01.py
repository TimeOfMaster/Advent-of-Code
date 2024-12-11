from math import log10
import os, unittest
from functools import lru_cache
from itertools import repeat

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

def main(numbers: list[int], blinks: int=25) -> int:
    return sum(map(calc, numbers, repeat(blinks)))

class TestStoneTransformation(unittest.TestCase):
    
    def test_single_blink_example(self):
        initial: list[int] = [0, 1, 10, 99, 999]
        expected_after_1: int = sum([1, 2024, 1, 0, 9, 9, 2021976])
        result: int = main(initial, 1)
        self.assertEqual(result, expected_after_1)
    
    def test_large_number_of_blinks(self):
        initial: list[int] = [125, 17]
        result: int = main(initial, 25)
        self.assertEqual(len(result), 55312)

if __name__ == "__main__":
	input_file: str = os.path.dirname(os.path.abspath(__file__)) + r"\\input.txt"
	data: list[int] = read_input(input_file)
 
	print(f"Part 1: {main(data)}")
	
	unittest.main()
