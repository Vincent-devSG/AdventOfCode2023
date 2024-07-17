import numpy as np
import functools
from collections import Counter 

with(open('input.txt', 'r') as file):
    lines = file.readlines()

lines = [line.strip().split() for line in lines] 

size = len(lines)
ranking = np.arange(1, size + 1, dtype=int) 

order = {'J': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, '_': 11, 'Q': 12, 'K': 13, 'A': 14}

hand_list = []
for line in lines:
    hand = line[0]
    bid = line[1]
    hand_list.append([hand, int(bid)])


def rate_hand(hand, joker_transform=False):

    hand_copy = hand[0]
    if joker_transform:
        rank = Counter(hand_copy)
        if 'J' in rank:
            ranked_hand = sorted(rank.most_common(), key=lambda x: (x[1], order[x[0]]), reverse=True)
            stg = ''
            for elem in ranked_hand:
                if elem[0] != 'J':
                    stg = elem[0]
                    break
            
            if stg != '':
                hand_copy = hand_copy.replace('J', stg)

    rank = sorted(Counter(hand_copy).values(), reverse=True)

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

    rate_hand_1 = rate_hand(hand1, joker_transform=True)
    rate_hand_2 = rate_hand(hand2, joker_transform=True)

    if rate_hand_1 > rate_hand_2:
        return 1
    
    if rate_hand_1 < rate_hand_2:
        return -1
    
    if rate_hand_1 == rate_hand_2:
        for (card1, card2) in zip(hand1[0], hand2[0]):
            if order[card1[0]] > order[card2[0]]:
                return 1
            if order[card1[0]] < order[card2[0]]:
                return -1 
        
    return 0
    

sorted_hands = sorted(hand_list, key=functools.cmp_to_key(compare_hands))


total = 0
for i, hand in enumerate(sorted_hands):
   total += hand[1] * (i+1)

print(total)



