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
    safe_count: int = 0

    for report in reports:
        safe_count += (is_safe(report)
                    or any(is_safe(report[:i] + report[i+1:]) for i in range(len(report))))
        
    return safe_count

class TestSafetyFunctions(unittest.TestCase):
    def test_example_reports(self):
        reports: list[list[int]] = [
                [7, 6, 4, 2, 1],  # Safe
                [1, 2, 7, 8, 9],  # Unsafe
                [9, 7, 6, 2, 1],  # Unsafe
                [1, 3, 2, 4, 5],  # Safe by removing 3
                [8, 6, 4, 4, 1],  # Safe by removing one 4
                [1, 3, 6, 7, 9]   # Safe
            ]
        self.assertEqual(main(reports), 4)

if __name__ == '__main__':
    input_file = os.path.dirname(os.path.abspath(__file__)) + r"\\input.txt"
    reports: list[int] = read_input(input_file)
    print(main(reports))

    unittest.main()