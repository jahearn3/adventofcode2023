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

# The following code is close but still not quite right
for i in range(min_y, max_y + 1):
    # print('y=', i)
    trench_edges = []
    for j in range(min_x, max_x + 1):
        if (j, i) in trench:
            trench_edges.append(j)
            full_trench.append((j, i))
    if len(trench_edges) == 2: 
        for k in range(trench_edges[0], trench_edges[1] + 1):
            full_trench.append((k, i))
    elif len(trench_edges) == 4 and trench_edges[3] - trench_edges[2] > 1 and trench_edges[2] - trench_edges[1] > 1 and trench_edges[1] - trench_edges[0] > 1:
        for k in range(trench_edges[0], trench_edges[1] + 1):
            full_trench.append((k, i))
        for k in range(trench_edges[2], trench_edges[3] + 1):
            full_trench.append((k, i)) 
    else:    
        trench_diffs = []
        for k in range(1, len(trench_edges)):
            trench_diffs.append(trench_edges[k] - trench_edges[k-1])
        if sum(trench_diffs) == len(trench_diffs):
            for k in range(trench_edges[0], trench_edges[-1] + 1):
                full_trench.append((k, i))
        else:
            # print('case C')
            # print(trench_edges)
            fill = True 
            for k, edge in enumerate(trench_edges):
            # for k in range(trench_edges[1], trench_edges[-1] + 1):
                # print((k, i))
                if k > 0:
                    if trench_edges[k] - trench_edges[k-1] == 1:
                        # print(f'c2: ({k},{i})')
                        full_trench.append((k, i))
                    elif fill:
                        for l in range(trench_edges[k-1], trench_edges[k] + 1):
                            # print(f'c3: ({l},{i})')
                            full_trench.append((l, i))
                        fill = False 
                    elif fill == False:
                        fill = True 
                    # else:
                    #     print(f'c4: ({k},{i})')
                    #     full_trench.append((k, i))
                else:
                    full_trench.append((k, i))

print(len(set(full_trench))) 

for i in range(min_y, max_y + 1):
    trench_viz = f'{i}'
    for j in range(min_x, max_x + 1):
        if (j, i) in trench:
            trench_viz += '#'
        else:
            trench_viz += '.'
    # print(trench_viz)
    with open('data/output18.txt', 'a') as myfile:
        myfile.write(trench_viz + '\n')

# Manually filled in the trenches

data = ld.load_data('output18edges_filledin.txt')
ans = 0
for line in data:
    for char in line:
        if char == '#':
            ans += 1
print(ans)