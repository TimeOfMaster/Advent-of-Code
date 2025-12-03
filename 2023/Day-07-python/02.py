import os
from collections import Counter

input_path = os.path.dirname(os.path.abspath(__file__)) + r"\\input.txt"

def get_numerical(card):
    if card.isdigit():
        return int(card)
    return {'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}[card]

def get_strength2(hand):
    num_jokers = hand.count(11)
    hand_without_jokers = tuple(card for card in hand if card != 11)
    trick_strength = list(sorted(Counter(hand_without_jokers).values(), reverse=True))
    if not trick_strength:
        trick_strength = (5,)
    else:
        trick_strength[0] += num_jokers
    trick_strength = tuple(trick_strength)

    new_hand = tuple(1 if card == 11 else card for card in hand)
    return trick_strength, new_hand

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


hands.sort(key=lambda p: get_strength2(p[0]))
print(sum(pair[1] * (i+1) for i, pair in enumerate(hands)))