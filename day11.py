# Day 11: Cosmic Expansion

import load_data as ld 
import os 

f = os.path.basename(__file__)
day = f[3:5]

data = ld.load_data(f'example{day}.txt')
data = ld.load_data(f'input{day}.txt')

# To look at original positions
# gal1 = []
# for i, line in enumerate(data):
#     for c, char in enumerate(line):
#         if char == '#':
#             gal1.append((c,i))
# print(gal1)

# Look at rows, keep track of columns
n_cols = len(data[0])
filled_cols = []
empty_rows = []
rcount = 0
for i, line in enumerate(data):
    if '#' not in line:
        empty_rows.append(i + rcount)
        rcount += 1
    else:
        for c, char in enumerate(line):
            if char == '#':
                if c not in filled_cols:
                    filled_cols.append(c)
empty_cols = []
ccount = 0
for i in range(max(filled_cols)):
    if i not in filled_cols:
        empty_cols.append(i + ccount)
        ccount += 1
        # Whenever I insert a column, it will offset future columns by one
# print('empty rows', empty_rows)
# print('empty cols', empty_cols)

# Expand the Universe
for col in empty_cols:
    for i, line in enumerate(data):
        # slice previous to col
        prev_slice = line[:col]
        # slice after col
        after_slice = line[col:]
        data[i] = prev_slice + '.' + after_slice

for row in empty_rows:
    data.insert(row, '.' * len(data[0]))

galaxies = []
for i, line in enumerate(data):
    for c, char in enumerate(line):
        if char == '#':
            galaxies.append((c,i))

# Count the steps
ans = 0
for i, g1 in enumerate(galaxies):
    for j, g2 in enumerate(galaxies):
        if i > j: # to avoid double counting
            ans += abs(g1[0] - g2[0]) + abs(g1[1] - g2[1]) # manhattan distance

print(ans)

# Part 2

# This did not work
# ans = 0
# for i, g1 in enumerate(galaxies):
#     for j, g2 in enumerate(galaxies):
#         if i > j: # to avoid double counting
#             # print('g1', g1, g1[1])
#             # print('g2', g2, g2[1])
#             dist = abs(g1[0] - g2[0]) + abs(g1[1] - g2[1]) # manhattan distance
#             # add a million for every empty row and column in between
#             for row in empty_rows:
#                 if g1[0] < row < g2[0]:
#                     # print('row', g1[0], row, g2[0])
#                     dist += 9 # 1_000_000
#                 elif g2[0] < row < g1[0]:
#                     dist += 9 # 1_000_000
#             for col in empty_cols:
#                 # print('col', col)
#                 if g1[1] < col < g2[1]:
#                     # print('col', g1[1], col, g2[1])
#                     dist += 9 # 1_000_000
#                 elif g2[1] < col < g1[1]:
#                     dist += 9 # 1_000_000
#             ans += dist


# print(ans)

# 580925188807 too low
# 580925769724 too low
# 603021166712 too high
# 603020563700

expansion = 999_999

# Look at rows, keep track of columns
n_cols = len(data[0])
filled_cols = []
empty_rows = []
for i, line in enumerate(data):
    if '#' not in line:
        empty_rows.append(i)
    else:
        for c, char in enumerate(line):
            if char == '#':
                if c not in filled_cols:
                    filled_cols.append(c)
empty_cols = []
for i in range(max(filled_cols)):
    if i not in filled_cols:
        empty_cols.append(i)

# print('empty rows', empty_rows)
# print('empty cols', empty_cols)

galaxies = []
for i, line in enumerate(data):
    for c, char in enumerate(line):
        if char == '#':
            galaxies.append((c,i))

# Change coordinates due to expansion
gal2 = []
for g in galaxies:
    (x, y) = g # Get initial coordinates
    x2 = x
    y2 = y
    for c in empty_cols:
        if x > c:
            x2 += expansion 
    for r in empty_rows:
        if y > r:
            y2 += expansion
    gal2.append((x2, y2))

# Count the steps
ans = 0
for i, g1 in enumerate(gal2):
    for j, g2 in enumerate(gal2):
        if i > j: # to avoid double counting
            ans += abs(g1[0] - g2[0]) + abs(g1[1] - g2[1]) # manhattan distance

print(ans)