# Day 9: Mirage Maintenance

import load_data as ld 
import os 

f = os.path.basename(__file__)
day = f[3:5]

data = ld.load_data(f'example{day}.txt')
data = ld.load_data(f'input{day}.txt')

ans = 0

for line in data:
    vals = list(map(int, line.split(' ')))
    zeros = 0
    sequences = {}
    n = len(vals)
    while zeros != 1:
        diffs = []
        zeros = 0
        for i in range(1, len(vals)):
            diffs.append(vals[i] - vals[i-1])
            if vals[i] == vals[i-1]:
                zeros += 1
        sequences[f'{len(vals)}'] = vals
        vals = diffs
        zeros /= len(vals)
    sequences[f'{len(vals)}'] = vals
    # Start extrapolating
    sequences[f'{len(vals)}'].append(0)
    # print(sequences)
    # print(len(vals), n)
    for i in range(len(vals), n + 1):
        lst = sequences[f'{i}']
        sub = sequences[f'{i-1}']
        # print(lst)
        # print(sub)
        nxt = lst[-1] + sub[-1]
        sequences[f'{i}'].append(nxt)
        if i == n:
            print(nxt)
            ans += nxt

print(ans)