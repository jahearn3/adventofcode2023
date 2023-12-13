# Day 13: Point of Incidence

import load_data as ld 
import os 

f = os.path.basename(__file__)
day = f[3:5]

data = ld.load_data(f'example{day}.txt')
data = ld.load_data(f'input{day}.txt')

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
    # print('---chunk---')
    # for line in chunk:
    #     print(line)
    # print('-----------')
    # Check for horizontal and vertical reflections
    for i in range(1, len(chunk)):
        if chunk[i] == chunk[i-1]:
            # Make sure other rows are reflected
            if 1 < i < len(chunk) - 1:
                j = i - 2
                k = i + 1
                right = [chunk[i]]
                left  = [chunk[i-1]]
                equal = True
                while -1 < j and k < len(chunk): 
                    right.append(chunk[k])
                    left.append(chunk[j])
                    if left != right: 
                        equal = False
                        break
                    j -= 1
                    k += 1
                if equal:
                    ans += 100 * i 
                    break
            else:
                ans += 100 * i 
                break

    inverse_chunk = list(map(list, zip(*chunk)))
    # for i in range(len(chunk)):
    # print('---inverse chunk---')
    # # print(inverse_chunk)
    # for line in inverse_chunk:
    #     print(line)
    # print('-------------------')


    for i in range(1, len(inverse_chunk)):
        col1 = inverse_chunk[i-1]
        col2 = inverse_chunk[i]
        if col1 == col2:
            # Make sure other columns are reflected
            if 1 < i < len(inverse_chunk):
                j = i - 2
                k = i + 1
                bottom = [col2]
                top  = [col1]
                equal = True
                while -1 < j and k < len(inverse_chunk): 
                    new_bottom = inverse_chunk[j]
                    new_top    = inverse_chunk[k]
                    bottom.append(new_bottom)
                    top.append(new_top)
                    if bottom != top:
                        equal = False
                        break
                    j -= 1
                    k += 1
                if equal:
                    ans += i
                    break
            else:
                ans += i
                break
    print(ans)
print(ans)