# Day 21: Step Counter

import load_data as ld 
import os 

f = os.path.basename(__file__)
day = f[3:5]

data = ld.load_data(f'example{day}.txt')
# data = ld.load_data(f'input{day}.txt')

for i, line in enumerate(data):
    for j, char in enumerate(line):
        if char == 'S':
            start = (j, i)
            xmax = len(line)
            ymax = len(data)

garden = ['.', 'S']
q = [start]
final_step = 10
for i in range(final_step):
    next = []
    while len(q) > 0:
        x, y = q.pop(0)
        if x > 0 and data[y][x-1] in garden:
            next.append((x-1, y))
        if x + 1 < xmax and data[y][x+1] in garden:
            next.append((x+1, y))
        if y > 0 and data[y-1][x] in garden:
            next.append((x, y-1))
        if y + 1 < ymax and data[y+1][x] in garden:
            next.append((x, y+1))
    q = list(set(next))
    if i + 1 == final_step:
        print(len(q))


# Part 2
for i in range(final_step):
    next = []
    while len(q) > 0:
        xx, yy = q.pop(0)
        if 0 < xx < xmax:
            x = xx 
        else:
            if xx > xmax:
                x = xx % xmax
        if 0 < yy < ymax:
            y = yy 
        else:
            if yy > ymax:
                y = y % ymax

        if data[y][x-1] in garden:
            next.append((x-1, y))
        if data[y][x+1] in garden:
            next.append((x+1, y))
        if data[y-1][x] in garden:
            next.append((x, y-1))
        if data[y+1][x] in garden:
            next.append((x, y+1))
    q = list(set(next))
    if i + 1 == final_step:
        print(len(q))
