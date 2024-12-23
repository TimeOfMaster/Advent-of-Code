import os
from collections import defaultdict
from typing import DefaultDict

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

def get_price_list(secrets: list[int]) -> list[list[int]]:
    price_lists: list[list[int]] = []
    for secret in secrets:
        num: int = secret
        price_lists.append([num%10])
        for _ in range(2000):
            num = evolve(num)
            price_lists[-1].append(num%10)
    return price_lists

def main(secrets: list[int]) -> int:
    price_lists: list[list[int]] = get_price_list(secrets)
    diff_table: DefaultDict[tuple[int, int, int, int], int] = defaultdict(int)
    for price in price_lists:
        d: set = set()
        for i in range(4, len(price)):
            diff = (price[i-3] - price[i-4], price[i-2] - price[i-3], price[i-1] - price[i-2], price[i] - price[i-1])
            if diff in d:
                continue
            diff_table[diff] += price[i]
            d.add(diff)
    return max(diff_table.values())

if __name__ == '__main__':
    input_file: str = os.path.dirname(os.path.abspath(__file__)) + r"\\input.txt"
    secrets: list[int] = read_input(input_file)

    print(f"Part 2: {main(secrets)}")
