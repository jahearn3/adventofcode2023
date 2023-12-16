# Day 16: The Floor Will Be Lava

import load_data as ld 
import os 

f = os.path.basename(__file__)
day = f[3:5]

data = ld.load_data(f'example{day}.txt')
# data = ld.load_data(f'input{day}.txt')

start = ('0', '0', 'r') # coordinates and direction
energized = []
energcoor = []
q = [start]
while len(q) > 0:
    # print('q:', q)
    (x, y, dir) = q.pop()
    # print(f'popped ({x}, {y}, {dir})' )
    x, y = int(x), int(y)
    energized.append((str(x), str(y), dir))
    energcoor.append((x, y))
    # print(f'found {data[y][x]}')
    # Empty space
    if data[y][x] == '.':
        if dir == 'r':
            if x + 1 < len(data[0]):
                # q.append((str(y), str(x+1), dir))
                if ((str(x+1), str(y), dir)) not in energized:
                    q.append((str(x+1), str(y), dir))
        elif dir == 'l':
            if x > 0:
                if (str(x-1), str(y), dir) not in energized:
                # q.append((str(y), str(x-1), dir))
                    q.append((str(x-1), str(y), dir))
        elif dir == 'u':
            if y > 0:
                if (str(x), str(y-1), dir) not in energized:
                # q.append((str(y-1), str(x), dir))
                    q.append((str(x), str(y-1), dir))
        elif dir == 'd':
            if y + 1 < len(data):
                if (str(x), str(y+1), dir) not in energized:
                # q.append((str(y+1), str(x), dir))
                    q.append((str(x), str(y+1), dir))
    # Mirrors
    elif data[y][x] == '\\':
        # print('backslash')
        if dir == 'r':
            if y + 1 < len(data):
                if (str(x), str(y+1), 'd') not in energized:
                # q.append((str(y+1), str(x), 'd'))
                    q.append((str(x), str(y+1), 'd'))
        elif dir == 'l':
            if y > 0:
                if (str(x), str(y-1), 'u') not in energized:
                # q.append((str(y-1), str(x), 'u'))
                    q.append((str(x), str(y-1), 'u'))
        elif dir == 'u':
            if x > 0:
                if (str(x-1), str(y), 'l') not in energized:
                # q.append((str(y), str(x+1), 'r'))
                    q.append((str(x-1), str(y), 'l'))
        elif dir == 'd':
            if x + 1 < len(data[0]):
                if (str(x+1), str(y), 'l') not in energized:
                # q.append((str(y), str(x-1), 'l'))
                    q.append((str(x+1), str(y), 'l'))
    elif data[y][x] == '/':
        if dir == 'r':
            if y > 0:
                if (str(x), str(y-1), 'u') not in energized:
                # q.append((str(y-1), str(x), 'u'))
                    q.append((str(x), str(y-1), 'u'))
        elif dir == 'l':
            if y + 1 < len(data):
                if (str(x), str(y+1), 'd') not in energized:
                # q.append((str(y+1), str(x), 'd'))
                    q.append((str(x), str(y+1), 'd'))
        elif dir == 'u':
            if x > 0:
                if (str(x+1), str(y), 'r') not in energized:
                # q.append((str(y), str(x-1), 'l'))
                    q.append((str(x+1), str(y), 'r'))
        elif dir == 'd':
            if x + 1 < len(data[0]):
                if (str(x-1), str(y), 'l') not in energized:
                # q.append((str(y), str(x+1), 'r'))
                    q.append((str(x-1), str(y), 'l'))
    # Splitters
    elif data[y][x] == '|':
        if dir == 'r' or dir == 'l':
            if y > 0:
                if (str(x), str(y-1), 'u') not in energized:
                # q.append((str(y-1), str(x), 'u'))
                    q.append((str(x), str(y-1), 'u'))
            if y + 1 < len(data):
                if (str(x), str(y+1), 'd') not in energized:
                # q.append((str(y+1), str(x), 'd'))
                    q.append((str(x), str(y+1), 'd'))
        elif dir == 'u':
            if y > 0:
                if (str(x), str(y-1), dir) not in energized:
                # q.append((str(y-1), str(x), dir))
                    q.append((str(x), str(y-1), dir))
        elif dir == 'd':
            if y + 1 < len(data):
                if (str(x), str(y+1), dir) not in energized:
                # q.append((str(y+1), str(x), dir))
                    q.append((str(x), str(y+1), dir))
    elif data[y][x] == '-':
        if dir == 'u' or dir == 'd':
            if x + 1 < len(data[0]):
                if (str(x+1), str(y), 'r') not in energized:
                # q.append((str(y), str(x+1), 'r'))
                    q.append((str(x+1), str(y), 'r'))
            if x > 0:
                if (str(x-1), str(y), 'l') not in energized:
                # q.append((str(y), str(x-1), 'l'))
                    q.append((str(x-1), str(y), 'l'))
        elif dir == 'r':
            if x + 1 < len(data[0]):
                if (str(x+1), str(y), dir) not in energized:
                # q.append((str(y), str(x+1), dir))
                    q.append((str(x+1), str(y), dir))
        elif dir == 'l':
            if x > 0:
                if (str(x-1), str(y), dir) not in energized:
                # q.append((str(y), str(x-1), dir))
                    q.append((str(x-1), str(y), dir))
    # if len(q) > len(data) * len(data[0]):
    #     break



print(len(set(energcoor)))
# 47 incorrect

# for y, line in enumerate(data):
#     new_line = ''
#     for x, char in enumerate(line):
#         if (x, y) in energcoor:
#             new_line += '#'
#         else:
#             new_line += '.'
#     print(new_line)
