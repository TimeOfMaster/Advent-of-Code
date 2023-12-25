import os
try:
    import networkx as nx
except ImportError:
    import subprocess
    import sys
    
    subprocess.check_call([sys.executable, "-m", "pip", "install", "networkx"])
finally:
    import networkx as nx

input_path = os.path.dirname(os.path.abspath(__file__)) + r"\\input.txt"

graph = nx.Graph()

for line in open(input_path, 'r'):
    left, right = line.split(":")
    for node in right.strip().split():
        graph.add_edge(left, node)
        graph.add_edge(node, left)

graph.remove_edges_from(nx.minimum_edge_cut(graph))
a, b = nx.connected_components(graph)

print(len(a) * len(b))