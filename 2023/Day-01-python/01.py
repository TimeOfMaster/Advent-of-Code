import os

total_part1 = 0

digit_words = {'one':'1', 'two':'2', 'three':'3', 'four':'4', 'five':'5', 'six':'6',
'seven':'7', 'eight':'8', 'nine':'9'}

input_path = os.path.dirname(os.path.abspath(__file__)) + r"\\input.txt"

with open(input_path, 'r') as f:
    for line in f.readlines():
        digits = [char for char in line.strip() if char.isdigit()]
        calib = int(digits[0] + digits[-1])
        total_part1 += calib

print(total_part1)
