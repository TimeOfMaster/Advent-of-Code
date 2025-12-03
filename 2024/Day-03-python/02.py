import re, unittest, os

def read_input(filename: str) -> str:
    with open(filename, 'r') as f:
        data = f.read()
    return data


def get_result(s, pattern: str) -> int:
    result = 0
    for m in re.findall(pattern, s):
        l, r = m.split(',')
        result += int(l[4:])*int(r[:-1])
    return result

def clean_data(data: str) -> list[str]:
    clean_data = []
    i = 0
    do = True
    while i < len(data):
        if do:
            if data[i:i+5] == 'don\'t':
                do = False
                i += 5
            else:
                clean_data.append(data[i])
                i += 1
        else:
            if data[i:i+2] == 'do' and data[i:i+5] != 'don\'t':
                do = True
                i += 2
            else:
                i += 1
    clean_data = ''.join(clean_data)
    
    return clean_data
    
def main(data: str) -> int:
    pattern: str = r'mul\(\d\d?\d?,\d\d?\d?\)'
    return get_result(clean_data(data), pattern=pattern)

class TestGetResult(unittest.TestCase):
    def test_example(self):
        example_input = r"xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
        self.assertEqual(main(example_input), 48)

if __name__ == '__main__':
    input_file = os.path.dirname(os.path.abspath(__file__)) + r"\\input.txt"
    data: str = read_input(input_file)
    print(main(data))
    
    unittest.main()