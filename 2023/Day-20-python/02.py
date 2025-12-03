import math
from collections import deque
import os

input_path = os.path.dirname(os.path.abspath(__file__)) + r"\\input.txt"


class Module:
    def __init__(self, name, type, outputs):
        self.name = name
        self.type = type
        self.outputs = outputs

        if type == "%":
            self.memory = "off"
        else:
            self.memory = {}
    def __repr__(self):
        return self.name + "{type=" + self.type + ",outputs=" + ",".join(self.outputs) + ",memory=" + str(self.memory) + "}"

modules = {}
broadcast_targets = []

with open(input_path, 'r') as f:
    for line in f:
        left, right = line.strip().split(" -> ")
        outputs = right.split(", ")
        if left == "broadcaster":
            broadcast_targets = outputs
        else:
            type = left[0]
            name = left[1:]
            modules[name] = Module(name, type, outputs)

for name, module in modules.items():
    for output in module.outputs:
        if output in modules and modules[output].type == "&":
            modules[output].memory[name] = "low"

(feed,) = [name for name, module in modules.items() if "rx" in module.outputs]

cycle_lengths = {}
seen = {name: 0 for name, module in modules.items() if feed in module.outputs}

presses = 0

while True:
    presses += 1
    queue = deque([("broadcaster", x, "low") for x in broadcast_targets])
    
    while queue:
        origin, target, pulse = queue.popleft()
        
        if target not in modules:
            continue
        
        module = modules[target]
        
        if module.name == feed and pulse == "high":
            seen[origin] += 1

            if origin not in cycle_lengths:
                cycle_lengths[origin] = presses
            else:
                assert presses == seen[origin] * cycle_lengths[origin]
                
            if all(seen.values()):
                x = 1
                for cycle_length in cycle_lengths.values():
                    x = math.lcm(x, cycle_length)
                print(x)
                exit(0)
        
        if module.type == "%":
            if pulse == "low":
                module.memory = "on" if module.memory == "off" else "off"
                outgoing = "high" if module.memory == "on" else "low"
                for x in module.outputs:
                    queue.append((module.name, x, outgoing))
        else:
            module.memory[origin] = pulse
            outgoing = "low" if all(x == "high" for x in module.memory.values()) else "high"
            for x in module.outputs:
                queue.append((module.name, x, outgoing))