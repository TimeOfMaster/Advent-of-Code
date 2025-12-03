from collections import defaultdict
from typing import DefaultDict, Set
import os

class Graph:
    def __init__(self):
        self.edges: DefaultDict[str, Set[str]] = defaultdict(set)
    def add_edge(self, u, v) -> None:
        self.edges[u].add(v)
        self.edges[v].add(u)
    def get_nbrs(self, u):
        return self.edges[u]

def read_input(filename: str) -> Graph:
    graph: Graph= Graph()
    with open(filename, 'r') as f:
        for line in f.readlines():
            u, v = line.strip().split('-')
            graph.add_edge(u, v)
    return graph

def main(graph: Graph) -> int:
    result: int = 0
    for u in graph.edges:
        for v in graph.edges[u]:
            for w in graph.edges[u]:
                if w == v:
                    continue
                if v in graph.edges[w]:
                    result += any(node.startswith('t') for node in (u, v, w))
    return result//6

if __name__ == '__main__':
    input_file: str = os.path.dirname(os.path.abspath(__file__)) + r"\\input.txt"
    graph: Graph = read_input(input_file)

    print(f"Part 1: {main(graph)}")
