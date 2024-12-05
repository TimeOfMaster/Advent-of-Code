from collections import defaultdict
from typing import DefaultDict, Set
import unittest, os

def read_input(filename: str) -> list[str]:
    with open(filename, 'r') as f:
        input: list[str] = f.readlines()
        return input

def main(input: list[str]) -> int:
    result: int = 0
    edge_list: DefaultDict[set] = defaultdict(set)
    is_section_one: bool = True
    
    for line in input:
        if not line.strip():
            is_section_one = False
            continue
        
        if is_section_one:
            # section 1
            x, y = (int(z) for z in line.split('|'))
            edge_list[x].add(y)
            
        else:
            # section 2
            l: list[int] = [int(z) for z in line.strip().split(',')]
            valid: bool = True
            # check for violations
            for i in range(len(l)):
                for j in range(i+1, len(l)):
                    if l[i] in edge_list[l[j]]:
                        valid = False
                        break
                if not valid:
                    break
            
            if valid:
                result += l[len(l)//2]
                
    return result                

class TestSafetyManuals(unittest.TestCase):
    def test_example(self):
        example_input: list[str] = [
            "47|53",
            "97|13",
            "97|61",
            "97|47",
            "75|29",
            "61|13",
            "75|53",
            "29|13",
            "97|29",
            "53|29",
            "61|53",
            "97|53",
            "61|29",
            "47|13",
            "75|47",
            "97|75",
            "47|61",
            "75|61",
            "47|29",
            "75|13",
            "53|13",
            "",
            "75,47,61,53,29",
            "97,61,53,29,13",
            "75,29,13",
            "75,97,47,61,53",
            "61,13,29",
            "97,13,75,29,47",
        ]
        result: int = main(example_input)
        self.assertEqual(result, 143)

if __name__ == '__main__':
    input_file = os.path.dirname(os.path.abspath(__file__)) + r"\\input.txt"
    input: list[str] = read_input(input_file)
    print(main(input))
    
    unittest.main()