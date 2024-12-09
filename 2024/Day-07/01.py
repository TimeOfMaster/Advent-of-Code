import unittest, os
from itertools import product

def is_valid_equation(test_value, equation, operator_symbols):
    for operators in product(operator_symbols, repeat=len(equation)-1):
        p = equation[0]
        for i, o in enumerate(operators):
            if o == '+':
                p += equation[i+1]
            elif o == '*':
                p *= equation[i+1]
            elif o == '|':
                p = int(str(p) + str(equation[i+1]))
            if p > test_value:
                break
        if p == test_value:
            return True
    return False

def read_input(filename: str) -> list[str]:
    with open(filename, 'r') as f:
        lines: list[str] = [line.strip() for line in f]
    return lines
    
def main(data: list[str]) -> int:
    result: int = 0
    
    for i, line in enumerate(data):
        ints = line.strip().split()
        test_value = int(ints[0][:-1])
        equation = [int(x) for x in ints[1:]]
        if is_valid_equation(test_value, equation, '+*'):
            result += test_value
    return result

class TestCalibration(unittest.TestCase):
    def test_sample_input(self):
        sample_data: list[str] = [
            "190: 10 19",
            "3267: 81 40 27",
            "83: 17 5",
            "156: 15 6",
            "7290: 6 8 6 15",
            "161011: 16 10 13",
            "192: 17 8 14",
            "21037: 9 7 18 13",
            "292: 11 6 16 20"
        ]
        expected_sum: int = 3749
        result: int = main(sample_data)
        self.assertEqual(result, expected_sum)

if __name__ == '__main__':
    input_file: str = os.path.dirname(os.path.abspath(__file__)) + r"\\input.txt"
    data: list[str] = read_input(input_file)
    print(f'Part 1: {main(data)}')

    unittest.main()