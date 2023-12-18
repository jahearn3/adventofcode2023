# Day 18: Lavaduct Lagoon

import load_data as ld 
import os 

f = os.path.basename(__file__)
day = f[3:5]

data = ld.load_data(f'example{day}.txt')
# data = ld.load_data(f'input{day}.txt')

ans = 0
start = (0, 0)
trench = [start]
cur = start 
for line in data:
    direction, distance, color = line.split(' ')
    distance = int(distance)
    # print(direction, distance)
    x, y = cur
    # print(f'from ({x}, {y})')
    if direction == 'U':
        for i in range(distance):
            y += 1 
            trench.append((x, y))
            # print(f'appending ({x}, {y})')
    elif direction == 'D':
        for i in range(distance):
            y -= 1 
            trench.append((x, y))
            # print(f'appending ({x}, {y})')
    elif direction == 'L':
        for i in range(distance):
            x -= 1 
            trench.append((x, y))
            # print(f'appending ({x}, {y})')
    elif direction == 'R':
        for i in range(distance):
            x += 1 
            trench.append((x, y))
            # print(f'appending ({x}, {y})')
    cur = (x, y)
    # print(f'cur ended at ({x}, {y})')

# Digging out what is in between trenches
max_x, max_y = 0, 0
min_x, min_y = 0, 0
for x, y in trench:
    if x > max_x:
        max_x = x 
    if y > max_y:
        max_y = y 
    if x < min_x:
        min_x = x 
    if y < min_y:
        min_y = y 

print(min_x, max_x)
print(min_y, max_y)

full_trench = []
# For each row, find min and max for that row, and fill in the rest
for i in range(min_y, max_y + 1):
    min_x_i = max_x 
    max_x_i = min_x 
    for x, y in trench:
        if y == i:
            # print((x, y))
            if x > max_x_i:
                max_x_i = x 
            elif x < min_x_i:
                min_x_i = x 
    for j in range(min_x_i, max_x_i + 1):
        full_trench.append((j, i))


print(len(full_trench))
# 44867 too high

print(len(set(full_trench))) # 44867

print(len(set(trench))) # 4064