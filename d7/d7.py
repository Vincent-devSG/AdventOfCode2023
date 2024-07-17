import numpy as np
import functools
from collections import Counter 

with(open('input.txt', 'r') as file):
    lines = file.readlines()

lines = [line.strip().split() for line in lines] 

size = len(lines)
ranking = np.arange(1, size + 1, dtype=int) 

order = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}

hand_list = []
for line in lines:

    hand = Counter(line[0])
    bid = line[1]

    hand_list.append([hand, int(bid)])




def rate_hand(hand):

    rank = []
    for elem in hand:
        rank.append(elem[1])
    
    
    if max(rank) == 1:
        return 1
    
    if max(rank) == 2 and rank.count(2) == 2:
        return 2.5
    
    if max(rank) == 2:
        return 2
    
    if max(rank) == 3 and rank.count(2) == 1:
        return 3.5
    
    if max(rank) == 3:
        return 3
    
    if max(rank) == 4:
        return 4
    
    if max(rank) == 5:
        return 5

def compare_hands(hand1, hand2):
    
    hand1 = hand1[0].most_common()
    hand2 = hand2[0].most_common()

    rate_hand_1 = rate_hand(hand1)
    rate_hand_2 = rate_hand(hand2)

    if rate_hand_1 > rate_hand_2:
        return 1
    
    if rate_hand_1 < rate_hand_2:
        return -1
    
    if rate_hand_1 == rate_hand_2:
        mvc1 = []
        for elem in hand1:
            mvc1.append(order[elem[0]])
        mvc2 = []
        for elem in hand2:
            mvc2.append(order[elem[0]])
        
        for elem1, elem2 in zip(mvc1, mvc2):
            if elem1 > elem2:
                return 1
            if elem1 < elem2:
                return -1
        

print(hand_list)

for elem in hand_list:
    hand = elem[0].most_common()
    rank = []
    for elem in hand:
        rank.append(elem[1])
    
    print(rank)
    
sorted_hands = sorted(hand_list, key=functools.cmp_to_key(compare_hands))
print(sorted_hands)