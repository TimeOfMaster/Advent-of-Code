import os

def read_input(filename: str) -> list[int]:
    secrets: list[int] = []
    with open(filename, 'r') as f:
        for line in f.readlines():
            secrets.append(int(line))
    return secrets

def evolve(num: int) -> int:
    result: int = num
    result = ((result*64) ^ result) % 16777216
    result = ((result//32) ^ result) % 16777216
    result = ((result*2048) ^ result) % 16777216
    return result

def main(secrets: list[int]) -> int:
    price_lists: list[list[int]] = []
    result: int = 0
    for secret in secrets:
        num: int = secret
        price_lists.append([num%10])
        for _ in range(2000):
            num = evolve(num)
            price_lists[-1].append(num%10)
        result += num
    return result

if __name__ == '__main__':
    input_file: str = os.path.dirname(os.path.abspath(__file__)) + r"\\input.txt"
    secrets: list[int] = read_input(input_file)

    print(f"Part 1: {main(secrets)}")
