import os

total_part2 = 0

digit_words = {'one':'1', 'two':'2', 'three':'3', 'four':'4', 'five':'5', 'six':'6',
'seven':'7', 'eight':'8', 'nine':'9'}

input_path = os.path.dirname(os.path.abspath(__file__)) + r"\\input.txt"

with open(input_path, 'r') as f:
    for line in f.readlines():
        
        s = line.strip()

        # first digit
        first_digit = None
        for i in range(len(s)):
            if s[i].isdigit():
                first_digit = s[i]
                break
            for word in digit_words:
                if s[i:].startswith(word):
                    first_digit = digit_words[word]
                    break
            if first_digit:
                break

        # last digit
        last_digit = None
        for i in range(len(s)-1, -1, -1):
            if s[i].isdigit():
                last_digit = s[i]
                break
            for word in digit_words:
                if s[i:].startswith(word):
                    last_digit = digit_words[word]
                    break
            if last_digit:
                break

        calib = int(first_digit + last_digit)
        total_part2 += calib

print(total_part2)