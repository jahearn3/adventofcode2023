# Day 14: Parabolic Reflector Dish

import load_data as ld 
import os 

f = os.path.basename(__file__)
day = f[3:5]

data = ld.load_data(f'example{day}.txt')
# data = ld.load_data(f'input{day}.txt')

# Tilt northward
for i, line in enumerate(data):
    if i > 0:
        # Get indices of all rolling rocks
        locs = [j for j, ltr in enumerate(line) if ltr == 'O']
        k = i
        prev_line = data[k-1]
        
        for j in locs:
            rolling = True
            while rolling:
                if k == -1:
                    rolling = False 
                elif data[k-1][j] == '.':
                    data[k-1] = data[k-1][:j] + 'O' + data[k-1][j+1:]
                    data[k] = data[k][:j] + '.' + data[k][j+1:]
                    k -= 1
                else:
                    rolling = False 



        # for j, char in enumerate(line):
        #     if j == 3:
        #         print(i, j)
        #         print(data[i-1])
        #         print(data[i])


        #     if char == 'O':
        #         rolling = True 
        #         k = i
        #         while rolling:
        #             if data[k-1][j] == '#' or data[k-1][j] == 'O':
        #                 rolling = False
        #             else:
        #                 if j == 3:
        #                     # print(i, j, k)
        #                     # print('Hey')
        #                     # print(data[k-1][:j])
        #                     # print('O')
        #                     # print(data[k-1][j+1:])
        #                     # print('Now')
        #                     # print(data[k][:j])
        #                     # print('.')
        #                     # print(data[k][j+1:])
        #                     print('Before')
        #                     print(data[k-1])
        #                     print(data[k])
                            
        #                 data[k-1] = data[k-1][:j] + 'O' + data[k-1][j+1:]
        #                 data[k] = data[k][:j] + '.' + data[k][j+1:]
        #                 if j == 3:
        #                     print('After')
        #                     print(data[k-1])
        #                     print(data[k])
        #                 k -= 1

ans = 0
# Count the load
for i, line in enumerate(data):
    dist = len(data) - i 
    for char in line:
        if char == 'O':
            ans += dist 

    print(line)          

print(ans)