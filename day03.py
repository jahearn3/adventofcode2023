# Day 3: Gear Ratios

import load_data as ld 

def check_line(ans, data, x, y):
    line = data[x]
    mid = data[x][y]
    if y != 0: 
        left = data[x][y-1]
    if y != len(line) - 1:
        right = data[x][y+1]
    if left.isdigit(): # Need to backtrack to the beginning of the number
        k = y - 1
        start = None
        end = None
        while data[x][k].isdigit():
            start = k
            k -= 1
        pn = ''
        k = start
        if start is not None:
            while data[x][k].isdigit():
                pn += data[x][k]
                k += 1
            end = k - 1
            ans += int(pn)
    elif mid.isdigit():  
        pn = ''
        k = y 
        while data[x][k].isdigit():
            pn += data[x][k]
            k += 1
        ans += int(pn)
    if right.isdigit() and (mid.isdigit() == False):
        pn = ''
        k = y + 1
        while data[x][k].isdigit():
            pn += data[x][k]
            if k == len(line) - 1:
                break
            k += 1
        ans += int(pn)
    return ans

data = ld.load_data('example03.txt')
data = ld.load_data('input03.txt')

ans = 0

symbols = ['#', '*', '$','-', '+', '@', '&', '!', '?', '%', '^', '/', ')', '<', '>', '=', '(', '|', '~', '_']
for i, line in enumerate(data):
    for j, char in enumerate(line):
        if char in symbols:
            # check above 
            if i != 0:
                ans = check_line(ans, data, i-1, j)
            # check below
            if i != len(data) - 1:
                ans = check_line(ans, data, i+1, j)
            # check left and right
            if j != 0:
                ans = check_line(ans, data, i, j)

print(ans)

# Part 2

def check_line2(pns, data, x, y):
    line = data[x]
    mid = data[x][y]
    if y != 0: 
        left = data[x][y-1]
    if y != len(line) - 1:
        right = data[x][y+1]
    if left.isdigit(): # Need to backtrack to the beginning of the number
        k = y - 1
        start = None
        end = None
        while data[x][k].isdigit():
            start = k
            k -= 1
        pn = ''
        k = start
        if start is not None:
            while data[x][k].isdigit():
                pn += data[x][k]
                k += 1
            end = k - 1
            pns.append(int(pn))
    elif mid.isdigit():  
        pn = ''
        k = y 
        while data[x][k].isdigit():
            pn += data[x][k]
            k += 1
        pns.append(int(pn))
    if right.isdigit() and (mid.isdigit() == False):
        pn = ''
        k = y + 1
        while data[x][k].isdigit():
            pn += data[x][k]
            if k == len(line) - 1:
                break
            k += 1
        pns.append(int(pn))
    return pns

ans = 0
for i, line in enumerate(data):
    for j, char in enumerate(line):
        if char == '*':
            pns = []
            # check above 
            if i != 0:
                pns = check_line2(pns, data, i-1, j)
            # check below
            if i != len(data) - 1:
                pns = check_line2(pns, data, i+1, j)
            # check left and right
            if j != 0:
                pns = check_line2(pns, data, i, j)
            if len(pns) == 2:
                ans += pns[0] * pns[1]

print(ans)
