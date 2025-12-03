import os
input_path = os.path.dirname(os.path.abspath(__file__)) + r"\\input.txt"

sum_possible = 0
sum_powers = 0
limit = {'red': 12, 'green': 13, 'blue': 14}

with open(input_path, 'r') as f:
    for i, line in enumerate(f.readlines()):
        min_possible = {'red': 0, 'green': 0, 'blue': 0}
        picks = line.strip()[line.find(':')+2:].split('; ')
        for p in picks:
            for part in p.split(', '):
                num, colour = part.split(' ')
                num = int(num)
                
                min_possible[colour] = max(min_possible[colour], num)
        power = 1
        for v in min_possible.values():
            power *= v
        sum_powers += power

# part 2
print(sum_powers)