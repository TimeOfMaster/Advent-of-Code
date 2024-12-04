import unittest, os

def read_input(filename: str) -> tuple[int, list[list[str]]]:
    word_search: list[list[str]] = []
    with open(filename, 'r') as f:
        for line in f.readlines():
            word_search.append(list(line.strip()))
    length: int = len(word_search)
    
    return length, word_search

def is_inbounds(i: int, j: int,length: int) -> bool:
    return 0 <= i < length and 0 <= j < length

def main(length: int, word_search: list[list[str]]) -> int:
    result: int = 0
    for i in range(length):
        for j in range(length):
            if word_search[i][j] != 'X':
                continue
            for di in [-1, 0, 1]:
                for dj in [-1, 0, 1]:
                    if (di, dj) == (0, 0):
                        continue
                    if is_inbounds(i+3*di, j+3*dj, length=length):
                        if ''.join(word_search[i+k*di][j+k*dj] for k in range(4)) == 'XMAS':
                            result += 1
    return result

class TestWordSearch(unittest.TestCase):
     def test_example_case(self):
        word_search: list[list[str]] = [
            list("MMMSXXMASM"),
            list("MSAMXMSMSA"),
            list("AMXSXMAAMM"),
            list("MSAMASMSMX"),
            list("XMASAMXAMM"),
            list("XXAMMXXAMA"),
            list("SMSMSASXSS"),
            list("SAXAMASAAA"),
            list("MAMMMXMMMM"),
            list("MXMXAXMASX"),
        ]
        length = 10
        result: int = main(length, word_search)
        self.assertEqual(result, 18)

if __name__ == '__main__':
    input_file = os.path.dirname(os.path.abspath(__file__)) + r"\\input.txt"
    length, word_search = read_input(input_file)
    print(main(length, word_search))
    
    unittest.main()