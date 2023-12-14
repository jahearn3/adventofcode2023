# Day 14: Parabolic Reflector Dish

import load_data as ld 
import os 

f = os.path.basename(__file__)
day = f[3:5]

data = ld.load_data(f'example{day}.txt')
data = ld.load_data(f'input{day}.txt')

# Transposition
transposed_data = list(map(list, zip(*data)))

altered_data = []
# Do one row at a time
for row in transposed_data:
    # Get indices of all round rocks
    roundlocs = [j for j, ltr in enumerate(row) if ltr == 'O']
    for c in roundlocs:
        d = c
        rolling = True
        # Move round rocks to the left until the edge or up to a cube rock 
        while rolling:
            if d == 0:
                rolling = False
            elif row[d-1] == '#':
                rolling = False
            elif row[d-1] == 'O':
                rolling = False
            else:
                row[d-1] = 'O'
                row[d] = '.'
                d -= 1
    altered_data.append(row)

# Count the load
ans = 0
for i, line in enumerate(altered_data):
    for j, char in enumerate(line):
        dist = len(line) - j
        if char == 'O':
            ans += dist

print(ans)