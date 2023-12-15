# Day 15: Lens Library

import load_data as ld 
import os 

f = os.path.basename(__file__)
day = f[3:5]

data = ld.load_data(f'example{day}.txt')
data = ld.load_data(f'input{day}.txt')

lst = data[0].split(',')
# lst = ['H', 'A', 'S', 'H']
ans = 0
for item in lst:
    a = 0
    for char in item:
        a += ord(char)
        a *= 17
        a %= 256
    ans += a

print(ans)