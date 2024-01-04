# Day 24: Never Tell Me The Odds

import load_data as ld 
import os 

f = os.path.basename(__file__)
day = f[3:5]

data_source = f'example{day}.txt'
data_source = f'input{day}.txt'
data = ld.load_data(data_source)

hailstones = []

for line in data:
    pos, vel = line.split('@')
    x, y, z = list(map(int, pos.strip().split(',')))
    u, v, w = list(map(int, vel.strip().split(',')))
    hailstones.append((x, y, u, v)) 

if data_source[0] == 'e':
    xmin, xmax = 7, 27
    ymin, ymax = 7, 27
elif data_source[0] == 'i':
    xmin, xmax = 200000000000000, 400000000000000
    ymin, ymax = 200000000000000, 400000000000000


ans = 0

# Using insight from HyperNeutrino
for i, h1 in enumerate(hailstones):
    for j, h2 in enumerate(hailstones):
        if i < j:
            x1, y1, u1, v1 = h1
            a1 = v1
            b1 = -u1
            c1 = v1 * x1 - u1 * y1
            x2, y2, u2, v2 = h2
            a2 = v2
            b2 = -u2
            c2 = v2 * x2 - u2 * y2
            if a1 * b2 == a2 * b1:
                continue
            x = (c1 * b2 - c2 * b1) / (a1 * b2 - a2 * b1)
            y = (c2 * a1 - c1 * a2) / (a1 * b2 - a2 * b1)
            if xmin <= x <= xmax and ymin <= y <= ymax:
                if (x - x1) * u1 >= 0 and (y - y1) * v1 >= 0 and (x - x2) * u2 >= 0 and (y - y2) * v2 >= 0:
                    ans += 1
     
print(ans)