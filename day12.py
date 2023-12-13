# Day 12: Hot Springs

import load_data as ld 
import os 
import re 

f = os.path.basename(__file__)
day = f[3:5]

data = ld.load_data(f'example{day}.txt')
# data = ld.load_data(f'input{day}.txt')

ans = 0
for line in data:
    conditions, b = line.split(' ')
    arrangements = list(map(int, b.split(',')))
    if '?' not in conditions:
        ans += 1
    else:
        # d1 = conditions.count('#') # number of damaged springs
        # d2 = conditions.count('##')
        # d3 = conditions.count('###')
        # d4 = conditions.count('####')
        # d5 = conditions.count('#####')
        # d6 = conditions.count('#' * 6)
        # p = conditions.count('.') # number of operational springs
        # q = conditions.count('?') # number of unknown springs
        # print(d1, d2, d3, d4, d5, d6, p, q, arrangements)

        # set_arr = set(arrangements)

        # print(set_arr)

        # for arr in set_arr:
        #     sub = '#' * arr
        #     temp = set(conditions)
        #     occ = {ele: [x.start() for x in re.finditer(sub, conditions)] for ele in temp}
        #     print(occ)
        # for char in conditions:
        #     if char == '#'

        print(conditions, arrangements)

        # for i in set(arrangements):
            
            


print(ans)