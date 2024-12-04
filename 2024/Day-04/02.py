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
            if word_search[i][j] != 'A':
                continue
            if not is_inbounds(i+1, j+1, length=length):
                continue
            if not is_inbounds(i+1, j-1, length=length):
                continue
            if not is_inbounds(i-1, j+1, length=length):
                continue
            if not is_inbounds(i-1, j-1, length=length):
                continue
            if not (word_search[i-1][j-1], word_search[i+1][j+1]) in (('M', 'S'), ('S', 'M')):
                continue
            if not (word_search[i+1][j-1], word_search[i-1][j+1]) in (('M', 'S'), ('S', 'M')):
                continue
            result += 1

    return result

class TestWordSearch(unittest.TestCase):
     def test_example_case(self):
        word_search = [
            list(".M.S......"),
            list("..A..MSMS."),
            list(".M.S.MAA.."),
            list("..A.ASMSM."),
            list(".M.S.M...."),
            list(".........."),
            list("S.S.S.S.S."),
            list(".A.A.A.A.."),
            list("M.M.M.M.M."),
            list(".........."),
        ]
        length: int = 10
        result: int = main(length, word_search)
        self.assertEqual(result, 9)

if __name__ == '__main__':
    input_file = os.path.dirname(os.path.abspath(__file__)) + r"\\input.txt"
    length, word_search = read_input(input_file)
    print(main(length, word_search))
    
    unittest.main()