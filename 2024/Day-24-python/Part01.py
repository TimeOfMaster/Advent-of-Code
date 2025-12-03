import re, os
from typing import Optional, Tuple, Set, Dict

def read_input(filename: str) -> Tuple[Dict[str, Optional[int]], Set[Tuple[str, str, str, str]], int, int, int]:
    init_wires: Dict[str, Optional[int]] = {}
    init_gates: Set[Tuple[str, str, str, str]] = set()
    with open(filename, 'r') as f:
        pattern1 = r'(\w\w\w): (\d)'
        pattern2 = r'(\w\w\w) (\D+) (\w\w\w) -> (\w\w\w)'
        for line in f.readlines():
            if re.match(pattern1, line.strip()):
                wire, val = re.match(pattern1, line.strip()).groups()
                init_wires[wire] = int(val)
            elif re.match(pattern2, line.strip()):
                wire1, op, wire2, wire3 = re.match(pattern2, line.strip()).groups()
                init_gates.add((wire1, wire2, op, wire3))
                for w in (wire1, wire2, wire3):
                    if w not in init_wires:
                        init_wires[w] = None
    num_x_bits: int = sum(w[0] == 'x' for w in init_wires)
    num_y_bits: int = sum(w[0] == 'y' for w in init_wires)
    num_z_bits: int = sum(w[0] == 'z' for w in init_wires)
    
    return init_wires, init_gates, num_x_bits, num_y_bits, num_z_bits

def get_z(gates: Set[Tuple[str, str, str, str]], 
          init_wires: Dict[str, Optional[int]], 
          num_x_bits: int, 
          num_y_bits: int, 
          xy: Optional[Tuple[int, int]]=None) -> Optional[str]:
    wire_map = init_wires.copy()
    if xy is not None:
        x, y = xy
        bin_x: str = bin(x)[2:].zfill(num_x_bits)
        for i, bit in enumerate(reversed(bin_x)):
            wire_map['x'+str(i).zfill(2)] = int(bit)
        bin_y: str = bin(y)[2:].zfill(num_y_bits)
        for i, bit in enumerate(reversed(bin_y)):
            wire_map['y'+str(i).zfill(2)] = int(bit)
    while any(w[0] == 'z' and wire_map[w] is None for w in wire_map):
        to_remove: list[Tuple[str, str, str, str]] = []
        for gate in gates:
            wire1, wire2, op, wire3 = gate
            if wire_map[wire3] is not None:
                to_remove.append(gate)
                continue
            if wire_map[wire1] is not None and wire_map[wire2] is not None:
                if op == 'AND':
                    wire_map[wire3] = wire_map[wire1] & wire_map[wire2]
                elif op == 'OR':
                    wire_map[wire3] = wire_map[wire1] | wire_map[wire2]
                elif op == 'XOR':
                    wire_map[wire3] = wire_map[wire1] ^ wire_map[wire2]
                to_remove.append(gate)
        if not to_remove:
            return None
        for gate in to_remove:
            gates.remove(gate)
    z_bits: list[str] = []
    for w in sorted(wire for wire in wire_map if wire[0] == 'z'):
        z_bits.append(str(wire_map[w]))
    z: str = ''.join(reversed(z_bits))
    return z

def main(init_wires: Dict[str, Optional[int]],
        init_gates: Set[Tuple[str, str, str, str]],
        num_x_bits: int, 
        num_y_bits: int) -> int:
    z: Optional[str] = get_z(init_gates.copy(), init_wires, num_x_bits, num_y_bits)
    return int("0b" + z, 2)

if __name__ == '__main__':
    input_file: str = os.path.dirname(os.path.abspath(__file__)) + r"\\input.txt"
    data: Tuple[Dict[str, Optional[int]], Set[Tuple[str, str, str, str]], int, int, int] = read_input(input_file)
    
    init_wires: Dict[str, Optional[int]] = data[0]
    init_gates: Set[Tuple[str, str, str, str]] = data[1]
    num_x_bits: int = data[2]
    num_y_bits: int = data[3]
    num_z_bits: int = data[4]

    print(f"Part 1: {main(init_wires.copy(), init_gates.copy(), num_x_bits, num_y_bits)}")