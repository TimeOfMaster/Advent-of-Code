import os

input_path = os.path.dirname(os.path.abspath(__file__)) + r"\\input.txt"

sequences = []
with open(input_path, 'r') as f:
    for line in f.readlines():
        sequences.append(list(map(int, line.strip().split())))

def get_next_term(seq):
    rows = [seq[:]]
    while not all(x == 0 for x in rows[-1]):
        new_row = []
        for i in range(len(rows[-1])-1):
            new_row.append(rows[-1][i+1] - rows[-1][i])
        rows.append(new_row)
    rows[-1].append(0)
    for i in range(len(rows)-2, -1, -1):
        rows[i].append(rows[i][-1] + rows[i+1][-1])
    return rows[0][-1]

total = sum(get_next_term(seq) for seq in sequences)
print(total)
