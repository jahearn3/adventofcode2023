# Day 10: Pipe Maze

import load_data as ld 
import os 

f = os.path.basename(__file__)
day = f[3:5]

data = ld.load_data(f'example{day}.txt')
data = ld.load_data(f'example{day}b.txt')
data = ld.load_data(f'input{day}.txt')

ans = 0

for l, line in enumerate(data):
    for c, char in enumerate(line):
        if char == 'S':
            start = (l, c)
            print(f'Starting at {start}')
            break

connecting = True
# For both examples
# cur1 = 'F'
# cur2 = 'F'
# For Puzzle input
cur1 = 'L' 
cur2 = 'L'
x1 = start[0]
y1 = start[1]
x2 = start[0]
y2 = start[1]
xmax = len(data[0]) - 1
ymax = len(data) - 1
visited = [start]
while connecting:
    for dir in range(1,3):
        if dir == 1:
            cur = cur1
            x = x1 
            y = y1 
        else:
            cur = cur2
            x = x2 
            y = y2 
        
        next = []
        if cur == '|':
            # next.append((x, y-1))
            # next.append((x, y+1))
            next.append((x-1, y))
            next.append((x+1, y))
        elif cur == '-':
            # next.append((x-1, y))
            # next.append((x+1, y))
            next.append((x, y-1))
            next.append((x, y+1))
        elif cur == 'L':
            # next.append((x, y-1))
            # next.append((x+1, y))
            next.append((x-1, y))
            next.append((x, y+1))
        elif cur == 'J':
            # next.append((x, y-1))
            # next.append((x-1, y))
            next.append((x-1, y))
            next.append((x, y-1))
        elif cur == '7':
            # next.append((x, y+1))
            # next.append((x-1, y))
            next.append((x+1, y))
            next.append((x, y-1))
        elif cur == 'F':
            # next.append((x, y+1))
            # next.append((x+1, y))
            next.append((x+1, y))
            next.append((x, y+1))
        elif cur == '.':
            print('Ground')
        else:
            print('Error')
        print('next', next)
        for n, neighbor in enumerate(next):
            print('neighbor', neighbor, data[neighbor[0]][neighbor[1]])
            if neighbor in visited:
                print('pop')
                next.pop(n)
        # print('visited', visited)
        n = next[0]
        visited.append((n[0], n[1]))
        prev = cur 
        cur = data[n[0]][n[1]]
        print(f'{prev} at ({x},{y}) connecting to {cur} at {n}')
        if dir == 1:  
            x1 = n[0]
            y1 = n[1]
            cur1 = cur
        else:
            x2 = n[0]
            y2 = n[1]
            cur2 = cur
    ans += 1
    if (x1, y1) == (x2, y2):
        print('Code 1')
        connecting = False 
    elif ans > 8 and abs(x1 - x2) < 2 and abs(y1 - y2) < 2:
        print('Code 2')
        connecting = False
    elif ans > xmax * ymax:
        print('Code 3')
        connecting = False
            
print(ans)

# 38 incorrect
# 6886 correct

# Part 2
