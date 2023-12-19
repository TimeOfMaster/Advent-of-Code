import os
from math import lcm

input_path = os.path.dirname(os.path.abspath(__file__)) + r"\\input.txt"

with open(input_path, 'r') as f:
    lr_sequence = f.readline().strip()
    f.readline()
    edges = {}
    for line in f.readlines():
        left, right = line.strip().split(' = ')
        edges[left] = list(right[1:-1].split(', '))

starts = [s for s in edges.keys() if s.endswith('A')]

def get_loop(start):
    current = start
    lr_counter = 0
    steps = 0
    while not current.endswith('Z'):
        edge_index = 0 if lr_sequence[lr_counter] == 'L' else 1
        current = edges[current][edge_index]
        lr_counter = (lr_counter + 1) % len(lr_sequence)
        steps += 1
    first = True
    steps = 0
    while first or not current.endswith('Z'):
        edge_index = 0 if lr_sequence[lr_counter] == 'L' else 1
        current = edges[current][edge_index]
        lr_counter = (lr_counter + 1) % len(lr_sequence)
        first = False
        steps += 1
    return steps

loop_sizes = [get_loop(start) for start in starts]
print(lcm(*loop_sizes))