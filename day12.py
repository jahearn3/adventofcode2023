# Day 12: Hot Springs

import load_data as ld 
import os 
import re 

f = os.path.basename(__file__)
day = f[3:5]

data = ld.load_data(f'example{day}.txt')
# data = ld.load_data(f'input{day}.txt')

ans = 0
for line in data:
    conditions, b = line.split(' ')
    arrangements = list(map(int, b.split(',')))
    if '?' not in conditions:
        ans += 1
    else:
        d = conditions.count('#') # number of damaged springs
        p = conditions.count('.') # number of operational springs
        q = conditions.count('?') # number of unknown springs
        print(d, p, q, arrangements)

        # for a, arr in enumerate(arrangements):




print(ans)