import re, os

def read_input(filename: str) -> list[str]:
    lines: list[str] = []
    with open(filename) as file:
        lines = list(file.read().splitlines())
    return lines

def parse_input(lines: list[str]) -> list[tuple[list[int], list[int]]]:
    systems: list[tuple[list[int], list[int]]] = []
    i: int = 0
    while i < len(lines):
        if lines[i] == "":
            i += 1
            continue
        eq1: list[int] = [0, 0, 0]
        eq2: list[int] = [0, 0, 0]
        matches = re.findall(r"(\d+)", lines[i])
        eq1[0], eq2[0] = int(matches[0]), int(matches[1])
        matches = re.findall(r"(\d+)", lines[i + 1])
        eq1[1], eq2[1] = int(matches[0]), int(matches[1])
        matches = re.findall(r"(\d+)", lines[i + 2])
        eq1[2], eq2[2] = 10000000000000 + int(matches[0]), 10000000000000 + int(matches[1])
        systems.append((eq1, eq2))
        i += 3
    return systems

def cramer(e1: list[int], e2: list[int]) -> tuple[int, int]:
    determinant: int = e1[0] * e2[1] - e1[1] * e2[0]
    if not determinant:
        return 0, 0
    a: float = (e1[2] * e2[1] - e1[1] * e2[2]) / determinant
    b: float = (e1[0] * e2[2] - e1[2] * e2[0]) / determinant
    if not a.is_integer() or not b.is_integer():
        return 0, 0
    return int(a), int(b)


def main(data: list[str]) -> int:
    systems: list[tuple[list[int], list[int]]] = parse_input(data)
    A_TOKENS: int = 3
    B_TOKENS: int = 1
    sum_tokens: int = 0
    for e1, e2 in systems:
        cramer_return = cramer(e1, e2)
        a:int = cramer_return[0]
        b: int = cramer_return[1]
        sum_tokens += A_TOKENS * a + B_TOKENS * b
    return sum_tokens


if __name__ == "__main__":
    input_file: str = os.path.dirname(os.path.abspath(__file__)) + r"\\input.txt"
    data: list[str] = read_input(input_file)
    
    print(f"Part 2: {main(data)}")