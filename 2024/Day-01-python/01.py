import unittest, os

def read_input(filename: str) -> tuple[list[int], list[int]]:
    left: list[int] = []
    right: list[int] = []
    
    with open(filename, 'r') as f:
        for line in f.readlines():
            x, y = (int(z) for z in line.split())
            left.append(x)
            right.append(y)
            
    return left, right

def main(left: list[int], right: list[int]) -> int:
    left.sort()
    right.sort()
    lenght = len(left)
    
    return(sum(abs(left[i]-right[i]) for i in range(lenght)))

class TestTotalDistance(unittest.TestCase):
    def test_example_case(self):
        # Test case using the example numbers
        left: list[int] = [3, 4, 2, 1, 3, 3]
        right: list[int] = [4, 3, 5, 3, 9, 3]
        expected = 11
        self.assertEqual(main(left, right), expected)

if __name__ == '__main__':
    input_file = os.path.dirname(os.path.abspath(__file__)) + r"\\input.txt"
    left, right = read_input(input_file)
    print(main(left, right))
    
    unittest.main()