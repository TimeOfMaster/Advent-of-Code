import os

input_path = os.path.dirname(os.path.abspath(__file__)) + r"\\input.txt"

sum_possible = 0
limit = {'red': 12, 'green': 13, 'blue': 14}

with open(input_path, 'r') as f:
    for i, line in enumerate(f.readlines()):
        impossible = False
        min_possible = {'red': 0, 'green': 0, 'blue': 0}
        picks = line.strip()[line.find(':')+2:].split('; ')
        for p in picks:
            for part in p.split(', '):
                num, colour = part.split(' ')
                num = int(num)
                
                if num > limit[colour]:
                    impossible = True
        if not impossible:
            sum_possible += (i+1)
        power = 1

print(sum_possible)