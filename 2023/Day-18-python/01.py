import os
from dataclasses import dataclass

input_path = os.path.dirname(os.path.abspath(__file__)) + r"\\input.txt"

@dataclass(frozen=True)
class Pos:
    row: int
    col: int
    def __add__(self, other):
        return Pos(row=self.row + other.row, col=self.col + other.col)
    def __mul__(self, other):
        return Pos(row=self.row * other, col=self.col * other)

directions = {'U': Pos(-1, 0), 'L': Pos(0, -1), 'D': Pos(1, 0), 'R': Pos(0, 1)}

pos1, pos2 = Pos(0, 0), Pos(0, 0)
boundary1, boundary2 = [pos1], [pos2]
perimeter1, perimeter2 = 0, 0

with open(input_path, 'r') as f:
    for line in f.readlines():
        udlr, num, colour = line.strip().split()

        direction = directions[udlr]
        pos1 += (direction * int(num))
        boundary1.append(pos1)
        perimeter1 += int(num)


def shoelace(boundary):
    det = 0
    for i in range(len(boundary) - 1):
        p1, p2 = boundary[i], boundary[i+1]
        det += (p1.row * p2.col - p2.row * p1.col)
    return abs(det // 2)

area1 = shoelace(boundary1) + perimeter1 // 2 + 1
print(area1)
