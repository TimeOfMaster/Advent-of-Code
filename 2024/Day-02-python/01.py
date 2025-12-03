import unittest, os

def read_input(filename: str) -> list[int]:
    reports: list[int] = []
    with open(filename, 'r') as f:
        for line in f.readlines():
            reports.append([int(z) for z in line.split()])
    
    return reports

def is_safe(l):
    lenght = len(l)
    return ((all(1 <= l[i+1] - l[i] <= 3 for i in range(lenght-1)))
            or (all(1 <= l[i] - l[i+1] <= 3 for i in range(lenght-1))))

def main(reports: list[int]) -> int:
    safe_count = sum(map(is_safe, reports))

    return safe_count

class TestSafetyFunctions(unittest.TestCase):
    def test_example_reports(self):
        reports: list[list[int]] = [
            [7, 6, 4, 2, 1],  # Safe
            [1, 2, 7, 8, 9],  # Unsafe
            [9, 7, 6, 2, 1],  # Unsafe
            [1, 3, 2, 4, 5],  # Unsafe
            [8, 6, 4, 4, 1],  # Unsafe
            [1, 3, 6, 7, 9]   # Safe
        ]
        self.assertEqual(main(reports), 2)

if __name__ == '__main__':
    input_file = os.path.dirname(os.path.abspath(__file__)) + r"\\input.txt"
    reports: list[int] = read_input(input_file)
    print(main(reports))

    unittest.main()