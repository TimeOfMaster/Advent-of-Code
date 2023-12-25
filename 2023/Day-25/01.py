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

g = nx.Graph()

for line in open(input_path, 'r'):
    left, right = line.split(":")
    for node in right.strip().split():
        g.add_edge(left, node)
        g.add_edge(node, left)

g.remove_edges_from(nx.minimum_edge_cut(g))
a, b = nx.connected_components(g)

print(len(a) * len(b))