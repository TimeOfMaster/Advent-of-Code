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

def max_clique(graph: Graph, nodes: Set[str]) -> Set[str]:
    if len(nodes) == 0:
        return set()
    if len(nodes) == 1:
        return nodes
    temp_nodes = nodes.copy()
    node = temp_nodes.pop()
    clique_without = max_clique(graph, temp_nodes)
    clique_with = max_clique(graph, graph.edges[node] & temp_nodes) | {node}
    return clique_with if len(clique_with) > len(clique_without) else clique_without

def main(graph: Graph) -> str:
    nodes: Set[str] = set(graph.edges.keys())
    result: str = ','.join(x for x in sorted(max_clique(graph, nodes)))
    return result

if __name__ == '__main__':
    input_file: str = os.path.dirname(os.path.abspath(__file__)) + r"\\input.txt"
    graph: Graph = read_input(input_file)

    print(f"Part 2: {main(graph)}")