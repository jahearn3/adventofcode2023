# Day 0: Template

import load_data as ld 
import os 
import time
start_time = time.time()

f = os.path.basename(__file__)
day = f[3:5]

data = ld.load_data(f'example{day}.txt')
data = ld.load_data(f'input{day}.txt')

ans1 = 0
ans2 = 0

copies = [] # for part 2
for i, line in enumerate(data):
    first, have = line.split('|')
    card, winning = first.split(':')
    w = winning.strip().split(' ')
    h = have.strip().split(' ')
    for n in w:
        if n == ' ' or n == '': 
            w.remove(n)
    for n in h:
        if n == ' ' or n == '': 
            h.remove(n)
    matches = []
    for n in w:
        if n == ' ' or n == '': 
            print('removing ' + n + ' from w')
            w.remove(n)
        if n in h:
            matches.append(n)
    # Part 1
    if len(matches) > 0:
        add = 2**(len(matches)-1)
        ans1 += add
    # Part 2
    ans2 += 1 # counting the originals
    id = card.split(' ')[-1]
    n_copies = 0
    for copy in copies:
        if int(id) == copy:
            n_copies += 1
            ans2 += 1 # counting the copies 
    # Make copies if there are matches
    if len(matches) > 0:
        for j in range(len(matches)):
            for c in range(n_copies + 1):
                copies.append(int(id) + j + 1)
    print(f'Counted stratchcards: {ans2}')
    #* Part 2 takes several minutes to run

print(ans1)
print(ans2)

print("--- %s seconds ---" % (time.time() - start_time))