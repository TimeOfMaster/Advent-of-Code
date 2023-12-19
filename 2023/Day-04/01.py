import os

input_path = os.path.dirname(os.path.abspath(__file__)) + r"\\input.txt"

points = 0
cards = []

with open(input_path, 'r') as f:
    for line in f.readlines():
        row = line.strip().split()[2:]
        i = row.index('|')
        win_set = set(row[:i])
        my_set = set(row[i+1:])
        num_matches = len(win_set & my_set)
        if num_matches:
            points += (2**(num_matches-1))
        cards.append(num_matches)

print(points)