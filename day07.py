# Day 7: Camel Cards

import load_data as ld 
import os 

f = os.path.basename(__file__)
day = f[3:5]

data = ld.load_data(f'example{day}.txt')
data = ld.load_data(f'input{day}.txt')

strength = {'A':14,
            'K':13,
            'Q':12,
            'J':11,
            'T':10,
            '9':9,
            '8':8,
            '7':7,
            '6':6,
            '5':5,
            '4':4,
            '3':3,
            '2':2,
            }

hand_type_strength = {
    '5K':700,
    '4K':600,
    'FH':500,
    '3K':400,
    '2P':300,
    '1P':200,
    'HC':100
}

ans = 0
hands = []
for line in data:
    hand, bid = line.split(' ')
    counts = []
    for k in strength.keys():
        c = hand.count(k)
        counts.append(c)
    cs = sorted(counts)
    max_count = cs[-1]
    if max_count == 5:
        hand_strength = hand_type_strength['5K']
    elif max_count == 4:
        hand_strength = hand_type_strength['4K']
    elif max_count == 3:
        # distinguish between Full House and 3 of a Kind
        hand_strength = hand_type_strength['3K'] # default
        if cs[-2] == 2:
            hand_strength = hand_type_strength['FH']
    elif max_count == 2:
        # distinguish between 2 Pair and 1 Pair
        hand_strength = hand_type_strength['1P'] # default
        if cs[-2] == 2:
            hand_strength = hand_type_strength['2P']
    elif max_count == 1:
        hand_strength = hand_type_strength['HC']
    else:
        print('error')
        hand_strength = 0
    hand_strength += strength[hand[0]]
    hand_strength += strength[hand[1]] / 100
    hand_strength += strength[hand[2]] / 10000
    hand_strength += strength[hand[3]] / 1000000
    hand_strength += strength[hand[4]] / 100000000
    hands.append((hand, bid, hand_strength))

hands = sorted(hands, key=lambda tup: tup[2])

for i, hand in enumerate(hands):
    rank = i + 1
    b = int(hand[1])
    ans += (i + 1) * int(hand[1])

print(ans)

# Part 2
strength = {'A':14,
            'K':13,
            'Q':12,
            'J':1, 
            'T':10,
            '9':9,
            '8':8,
            '7':7,
            '6':6,
            '5':5,
            '4':4,
            '3':3,
            '2':2,
            }

ans = 0
hands = []
for line in data:
    hand, bid = line.split(' ')
    counts = []
    for k in strength.keys():
        if k != 'J':
            c = hand.count(k)
            counts.append(c)
    js = hand.count('J')
    cs = sorted(counts)
    cs[-1] += js
    max_count = cs[-1]
    if max_count == 5:
        hand_strength = hand_type_strength['5K']
    elif max_count == 4:
        hand_strength = hand_type_strength['4K']
    elif max_count == 3:
        # distinguish between Full House and 3 of a Kind
        hand_strength = hand_type_strength['3K'] # default
        if cs[-2] == 2:
            hand_strength = hand_type_strength['FH']
    elif max_count == 2:
        # distinguish between 2 Pair and 1 Pair
        hand_strength = hand_type_strength['1P'] # default
        if cs[-2] == 2:
            hand_strength = hand_type_strength['2P']
    elif max_count == 1:
        hand_strength = hand_type_strength['HC']
    else:
        print('error')
        hand_strength = 0
    hand_strength += strength[hand[0]]
    hand_strength += strength[hand[1]] / 100
    hand_strength += strength[hand[2]] / 10000
    hand_strength += strength[hand[3]] / 1000000
    hand_strength += strength[hand[4]] / 100000000
    hands.append((hand, bid, hand_strength))

hands = sorted(hands, key=lambda tup: tup[2])

for i, hand in enumerate(hands):
    rank = i + 1
    b = int(hand[1])
    ans += (i + 1) * int(hand[1])

print(ans)