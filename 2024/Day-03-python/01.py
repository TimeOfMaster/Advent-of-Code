import re, unittest, os

def read_input(filename: str) -> str:
    with open(filename, 'r') as f:
        data = f.read()
    return data


def get_result(s, pattern:str) -> int:
    result = 0
    for m in re.findall(pattern, s):
        l, r = m.split(',')
        result += int(l[4:])*int(r[:-1])
    return result

def main(data: str) -> int:
    pattern: str = r'mul\(\d\d?\d?,\d\d?\d?\)'
    return get_result(data, pattern=pattern)

class TestGetResult(unittest.TestCase):
    def test_example(self):
        example_input = r"xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
        self.assertEqual(main(example_input), 161)

if __name__ == '__main__':
    input_file = os.path.dirname(os.path.abspath(__file__)) + r"\\input.txt"
    data: str = read_input(input_file)
    print(main(data))
    
    unittest.main()