import os

input_path = os.path.dirname(os.path.abspath(__file__)) + r"\\input.txt"

def num_arrangements(record, pattern):
    table = {}
    # dynamic programming with memoisation
    def num_array(i, j):
        # subroutine to find num of arrangements, where we restrict to first i characters, and first j nums
        if (i, j) in table:
            return table[(i, j)]
        if i == 0 and j == 0:
            return 1
        elif i == 0:
            return 0
        elif j == 0:
            return int(all(char != '#' for char in record[:i]))
        elif record[i - 1] == '.':
            result = num_array(i - 1, j)
        else:
            num = pattern[j-1]
            if num > i or any(char == '.' for char in record[i - num:i]):
                result = 0
            elif i > num and record[i - num - 1] == '#':
                result = 0
            else:
                result = num_array(max(i - num - 1, 0), j-1)
            if record[i - 1] == '?':
                result += num_array(i - 1, j)
        table[(i, j)] = result
        return result
    return num_array(len(record), len(pattern))

total = 0
with open(input_path, 'r') as f:
    for line in f.readlines():
        l, r = line.strip().split()
        r = tuple(int(x) for x in r.split(','))
        total += num_arrangements(l, r)

print(total)