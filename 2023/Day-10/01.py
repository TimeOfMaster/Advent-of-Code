from collections import defaultdict
from queue import Queue
import os

input_path = os.path.dirname(os.path.abspath(__file__)) + r"\\input.txt"

class Position:
    def __init__(self, r, c):
        self.r = r
        self.c = c
    def __eq__(self, other):
        return (self.r, self.c) == (other.r, other.c)
    def __hash__(self):
        return hash((self.r, self.c))
    def __repr__(self):
        return '({}, {})'.format(self.r, self.c)

class Graph:
    def __init__(self):
        self.edges = defaultdict(set)
    def add_edge(self, u, v):
        self.edges[u].add(v)

graph = Graph()

def bfs(start):
    distance = {start: 0}
    queue = Queue()
    queue.put(start)
    while not queue.empty():
        current = queue.get()
        for nbr in graph.edges[current]:
            if nbr in distance:
                continue
            distance[nbr] = distance[current]+1
            queue.put(nbr)
    return distance

with open(input_path, 'r') as f:
    for i, line in enumerate(f.readlines()):
        for j, char in enumerate(line.strip()):
            pos = Position(i, j)
            if char == 'S':
                animal = pos
            elif char == '|':
                graph.add_edge(pos, Position(i-1, j))
                graph.add_edge(pos, Position(i+1, j))
            elif char == '-':
                graph.add_edge(pos, Position(i, j-1))
                graph.add_edge(pos, Position(i, j+1))
            elif char == 'L':
                graph.add_edge(pos, Position(i-1, j))
                graph.add_edge(pos, Position(i, j+1))
            elif char == 'J':
                graph.add_edge(pos, Position(i-1, j))
                graph.add_edge(pos, Position(i, j-1))
            elif char == '7':
                graph.add_edge(pos, Position(i, j-1))
                graph.add_edge(pos, Position(i+1, j))
            elif char == 'F':
                graph.add_edge(pos, Position(i, j+1))
                graph.add_edge(pos, Position(i+1, j))
        m = j + 1
    n = i + 1
    
for delta in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
    dr, dc, = delta
    nbr = Position(animal.r + dr, animal.c + dc)
    if animal in graph.edges[nbr]:
        graph.add_edge(animal, nbr)

distance = bfs(animal)
print(max(distance.values()))
