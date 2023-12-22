# Day 22: Sand Slabs

import load_data as ld 
import os 

f = os.path.basename(__file__)
day = f[3:5]

data = ld.load_data(f'example{day}.txt')
# data = ld.load_data(f'input{day}.txt')

ans = 0

bricks = []
zmax = 0
for line in data:
    a, b = line.split('~')
    x1, y1, z1 = list(int(map(a.split(','))))
    x2, y2, z2 = list(int(map(a.split(','))))
    if z1 > zmax:
        zmax = z1
    if z2 > zmax:
        zmax = z2


for z in range(zmax + 1):
    pass

print(ans)