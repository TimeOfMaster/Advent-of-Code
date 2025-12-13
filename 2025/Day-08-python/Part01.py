import os
from collections import defaultdict

def read_input(filename: str) -> list[tuple[int, int, int]]:
    """
    Read junction box positions from input file.
    
    Args:
        filename: Path to the input file containing junction box coordinates.
        
    Returns:
        List of junction box positions as (x, y, z) tuples.
    """
    with open(filename, 'r') as f:
        content: str = f.read().strip()
    
    data: list[tuple[int, int, int]] = []
    for line in content.splitlines():
        x: str
        y: str
        z: str
        x, y, z = line.split(",")
        data.append((int(x), int(y), int(z)))
    return data

def distance(p1: tuple[int, int, int], p2: tuple[int, int, int]) -> float:
    """
    Calculate Euclidean distance between two junction boxes in 3D space.
    
    Args:
        p1: First junction box position as (x, y, z) coordinates.
        p2: Second junction box position as (x, y, z) coordinates.
        
    Returns:
        Straight-line distance between the two junction boxes.
    """
    return ((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2 + (p1[2] - p2[2])**2) ** 0.5

class UnionFind:
    """
    Union-Find (Disjoint Set Union) data structure for tracking electrical circuits.
    
    Maintains which junction boxes are connected in the same circuit and tracks
    circuit sizes efficiently using path compression and union by rank.
    """
    
    parent: list[int]
    rank: list[int]
    size: list[int]
    
    def __init__(self, n: int) -> None:
        """
        Initialize Union-Find structure with n junction boxes.
        
        Args:
            n: Number of junction boxes (each starts in its own circuit).
        """
        self.parent = list(range(n))
        self.rank = [0] * n
        self.size = [1] * n
    
    def find(self, x: int) -> int:
        """
        Find the root (representative) junction box of the circuit containing x.
        
        Uses path compression to optimize future queries by flattening the tree structure.
        
        Args:
            x: Index of the junction box to query.
            
        Returns:
            Index of the root junction box representing this circuit.
        """
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x: int, y: int) -> bool:
        """
        Connect two junction boxes, merging their circuits if different.
        
        Uses union by rank to keep the tree structure balanced. Only creates a
        connection if the junction boxes are in different circuits.
        
        Args:
            x: Index of first junction box.
            y: Index of second junction box.
            
        Returns:
            True if junction boxes were in different circuits and got connected,
            False if they were already in the same circuit (no connection made).
        """
        root_x: int = self.find(x)
        root_y: int = self.find(y)
        
        if root_x == root_y:
            return False
        
        # Union by rank to keep tree balanced
        if self.rank[root_x] < self.rank[root_y]:
            root_x, root_y = root_y, root_x
        
        self.parent[root_y] = root_x
        self.size[root_x] += self.size[root_y]
        
        if self.rank[root_x] == self.rank[root_y]:
            self.rank[root_x] += 1
        
        return True
    
    def get_circuit_sizes(self) -> list[int]:
        """
        Get the sizes of all electrical circuits.
        
        Returns:
            List of circuit sizes (number of junction boxes in each circuit).
        """
        circuits: defaultdict[int, int] = defaultdict(int)
        for i in range(len(self.parent)):
            root: int = self.find(i)
            circuits[root] = self.size[root]
        return list(circuits.values())

def solve(junction_boxes: list[tuple[int, int, int]], num_connections: int = 1000) -> int:
    """
    Connect junction boxes by processing the closest pairs and calculate circuit statistics.
    
    Processes the first num_connections closest pairs of junction boxes by distance.
    When two junction boxes are connected with lights, electricity can flow between them,
    forming circuits. Some connection attempts may fail if the boxes are already in the
    same circuit.
    
    Args:
        junction_boxes: List of junction box positions as (x, y, z) tuples.
        num_connections: Number of closest pairs to attempt connecting (default: 1000).
        
    Returns:
        Product of the three largest circuit sizes after making all connections.
    """
    n: int = len(junction_boxes)
    
    # Build a list of all pairwise distances with their junction box indices
    print(f"Computing distances for {n} junction boxes...")
    distances: list[tuple[float, int, int]] = []
    i: int
    j: int
    for i in range(n):
        for j in range(i + 1, n):
            dist: float = distance(junction_boxes[i], junction_boxes[j])
            distances.append((dist, i, j))
    
    # Sort all distances to process closest pairs first
    print(f"Sorting {len(distances)} distances...")
    distances.sort()
    
    # Initialize Union-Find to track which junction boxes form circuits
    uf: UnionFind = UnionFind(n)
    
    # Attempt to connect the closest pairs of junction boxes
    connections_made: int = 0
    attempt_num: int
    for attempt_num, (dist, i, j) in enumerate(distances, 1):
        if attempt_num > num_connections:
            break
        if uf.union(i, j):
            connections_made += 1
    
    # Get circuit sizes and find the three largest
    circuit_sizes: list[int] = uf.get_circuit_sizes()
    circuit_sizes.sort(reverse=True)
    
    # Multiply the three largest circuit sizes together
    result: int = circuit_sizes[0] * circuit_sizes[1] * circuit_sizes[2]
    
    return result

if __name__ == "__main__":
    input_file: str = os.path.dirname(os.path.abspath(__file__)) + r"\\input.txt"
    data: list[tuple[int, int, int]] = read_input(input_file)
    
    result: int = solve(data, num_connections=1000)
    print(f"Part 1: {result}")
