import os

input_path = os.path.dirname(os.path.abspath(__file__)) + r"\\input.txt"

def s_hash(s):
    current = 0
    for char in s:
        current += ord(char)
        current = (current * 17) % 256
    return current

total = 0
boxes = [{} for _ in range(256)]

with open(input_path, 'r') as f:
    for line in f.readlines():
        for s in line.strip().split(','):
            total += s_hash(s)

print(total)
