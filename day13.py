# Day 13: Point of Incidence

import load_data as ld 
import os 

f = os.path.basename(__file__)
day = f[3:5]

data = ld.load_data(f'example{day}.txt')
# data = ld.load_data(f'input{day}.txt')

chunks = []
chunk = []
for line in data:
    if len(line) > 0:
        chunk.append(line)
    else:
        chunks.append(chunk)
        chunk = []
chunks.append(chunk)

ans = 0
for chunk in chunks:
    # Check for horizontal and vertical reflections
    for i in range(1, len(chunk)):
        if chunk[i] == chunk[i-1]:
            print('horizontal mirror') # TODO Try doing something with slices
            # Make sure other rows are reflected
            if 1 < i < len(chunk) - 1:
                if chunk[i+1] == chunk[i-2]: # Just one other row for now
                    print('add1', 100 * i)
                    ans += 100 * i 
                    break
            else:
                print('add2', 100 * i)
                ans += 100 * i 
                break
    

    for j in range(1, len(chunk[0])):
        col1 = [x for x in chunk[:][j-1]]
        col2 = [x for x in chunk[:][j]]
        print(j, col1)
        # print(col2)
        if col1 == col2:
            print('vertical mirror')
            # Make sure other columns are reflected
            if 1 < j < len(chunk[0]) - 1:
                col1 = [x for x in chunk[:][j-2]]
                col2 = [x for x in chunk[:][j+1]]
                if col1 == col2:
                    print('add1', j)
                    ans += j
                    break
            else:
                if col1 == col2:
                    print('add2', j)
                    ans += j
                    break

print(ans)