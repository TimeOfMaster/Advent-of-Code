import os
try:
    import sympy
except ImportError:
    import subprocess
    import sys
    
    subprocess.check_call([sys.executable, "-m", "pip", "install", "sympy"])
finally:
    import sympy

input_path = os.path.dirname(os.path.abspath(__file__)) + r"\\input.txt"

hailstones = [tuple(map(int, line.replace("@", ",").split(","))) for line in open(input_path, 'r')]

xr, yr, zr, vxr, vyr, vzr = sympy.symbols("xr, yr, zr, vxr, vyr, vzr")

equations = []

for i, (sx, sy, sz, vx, vy, vz) in enumerate(hailstones):
    equations.append((xr - sx) * (vy - vyr) - (yr - sy) * (vx - vxr))
    equations.append((yr - sy) * (vz - vzr) - (zr - sz) * (vy - vyr))
    if i < 2:
        continue
    answers = [solution for solution in sympy.solve(equations) if all(x % 1 == 0 for x in solution.values())]
    if len(answers) == 1:
        break
    
answer = answers[0]

print(answer[xr] + answer[yr] + answer[zr])