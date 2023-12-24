import os

input_path = os.path.dirname(os.path.abspath(__file__)) + r"\\input.txt"

class Hailstone:
    def __init__(self, start_x, start_y, start_z, velocity_x, velocity_y, velocity_z):
        self.start_x = start_x
        self.start_y = start_y
        self.start_z = start_z
        self.velocity_x = velocity_x
        self.velocity_y = velocity_y
        self.velocity_z = velocity_z
        
        # a x + b y = c
        self.a = velocity_y
        self.b = -velocity_x
        self.c = velocity_y * start_x - velocity_x * start_y
    
    def __repr__(self):
        return "Hailstone{" + f"a={self.a}, b={self.b}, c={self.c}" + "}"

hailstones = [Hailstone(*map(int, line.replace("@", ",").split(","))) for line in open(input_path, 'r')]

total = 0

for i, hailstone_1 in enumerate(hailstones):
    for hailstone_2 in hailstones[:i]:
        a1, b1, c1 = hailstone_1.a, hailstone_1.b, hailstone_1.c
        a2, b2, c2 = hailstone_2.a, hailstone_2.b, hailstone_2.c
        if a1 * b2 == b1 * a2:
            continue
        
        
        x = (c1 * b2 - c2 * b1) / (a1 * b2 - a2 * b1)
        y = (c2 * a1 - c1 * a2) / (a1 * b2 - a2 * b1)
        if 200000000000000 <= x <= 400000000000000 and 200000000000000 <= y <= 400000000000000:
            if all((x - hailstone.start_x) * hailstone.velocity_x >= 0 and (y - hailstone.start_y) * hailstone.velocity_y >= 0 for hailstone in (hailstone_1, hailstone_2)):
                total += 1

print(total)