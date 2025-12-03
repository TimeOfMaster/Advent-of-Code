import os
from collections import Counter

input_path = os.path.dirname(os.path.abspath(__file__)) + r"\\input.txt"

def get_numerical(card):
    if card.isdigit():
        return int(card)
    return {'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}[card]

def get_strength(hand):
    trick_strength = tuple(sorted(Counter(hand).values(), reverse=True))
    return trick_strength, hand

hands = []
with open(input_path, 'r') as f:
    for line in f.readlines():
        hand, bid = line.strip().split()
        bid = int(bid)
        hand = tuple(get_numerical(card) for card in hand)
        hands.append((hand, bid))

hands.sort(key=lambda p: get_strength(p[0]))

print(sum(pair[1] * (i + 1) for i, pair in enumerate(hands)))
