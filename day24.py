# Day 24: Never Tell Me The Odds

import load_data as ld 
import os 

f = os.path.basename(__file__)
day = f[3:5]

data_source = f'example{day}.txt'
# data_source = f'input{day}.txt'
data = ld.load_data(data_source)

hailstones = []

for line in data:
    pos, vel = line.split('@')
    x, y, z = list(map(int, pos.strip().split(',')))
    u, v, w = list(map(int, vel.strip().split(',')))
    hailstones.append((x, y, x + u, y + v)) # ignoring z-axis for part 1

if data_source[0] == 'e':
    xmin, xmax = 7, 27
    ymin, ymax = 7, 27
elif data_source[0] == 'i':
    xmin, xmax = 200000000000000, 400000000000000
    ymin, ymax = 200000000000000, 400000000000000


ans = 0

for i, h1 in enumerate(hailstones):
    for j, h2 in enumerate(hailstones):
        if i < j:
            # Evaluate whether h1 and h2 cross paths
            # using line-line intersection
            x1, y1, x2, y2 = h1
            print(x1, y1, x2, y2)
            x3, y3, x4, y4 = h2
            print(x3, y3, x4, y4)
            # Calculate denominator first to check if it is zero
            d = ((x1 - x2) * (y3 - y4)) - ((y1 - y2) * (x3 - x4))
            if d == 0:
                print('paths are parallel or coincident')
            else:
                xc = (((x1 * y2) - (y1 * x2)) * (x3 - x4)) - ((x1 * x2) * ((x3 * y4) - (y3 * x4)))
                xc /= d 
                yc = (((x1 * y2) - (y1 * x2)) * (y3 - y4)) - ((y1 * y2) * ((x3 * y4) - (y3 * x4)))
                yc /= d
                print(xc, yc)
                if xmin <= xc <= xmax and ymin <= yc <= ymax:
                    ans += 1
            



print(ans)