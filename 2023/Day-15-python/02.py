import os

input_path = os.path.dirname(os.path.abspath(__file__)) + r"\\input.txt"

def s_hash(s):
    current = 0
    for char in s:
        current += ord(char)
        current = (current * 17) % 256
    return current

boxes = [{} for _ in range(256)]

with open(input_path, 'r') as f:
    for line in f.readlines():
        for s in line.strip().split(','):
            if '-' in s:
                label = s[:-1]
                box = boxes[s_hash(label)]
                if label in box:
                    box.pop(label)
            else:
                label, focal = s.split('=')
                box = boxes[s_hash(label)]
                box[label] = int(focal)

total = 0
for i, box in enumerate(boxes):
    for j, lens in enumerate(box.items()):
        total += ((i + 1) * (j + 1) * lens[1])
print(total)