# Day 8: Haunted Wasteland

import load_data as ld 
import os 
import math

def get_network(data):
    network = {}
    for line in data[2:]:
        a, b = line.split(' = ')
        l, r = b.strip('()').split(',')
        r = r.strip()
        network[a] = (l, r)
    return network

f = os.path.basename(__file__)
day = f[3:5]

data = ld.load_data(f'example{day}.txt')
data = ld.load_data(f'example{day}b.txt')
data = ld.load_data(f'input{day}.txt')

instructions = data[0]
network = get_network(data)

start = 'AAA'
cur = 'AAA'
end = 'ZZZ'
ans = 0

while cur != end:
    for char in instructions:
        if char == 'L':
            next = network[cur][0]
        elif char == 'R':
            next = network[cur][1]
        cur = next
        ans += 1

print(ans)

# Part 2
data = ld.load_data(f'example{day}c.txt')
data = ld.load_data(f'input{day}.txt')

instructions = data[0]
network = get_network(data)

# Get starting points and ending points
start = []
end = []
for k in network.keys():
    if k[-1] == 'A':
        start.append(k)
    elif k[-1] == 'Z':
        end.append(k)

# Get the first solution for each starting point
ss = []
for s in start:
    cur = s
    ans = 0
    while cur[-1] != 'Z':
        for char in instructions:
            if char == 'L':
                next = network[cur][0]
            elif char == 'R':
                next = network[cur][1]
            cur = next
            ans += 1
            if cur[-1] == 'Z':
                ss.append(ans)
                break

# Find the least common multiple of the combination
while len(ss) > 1:
    a = ss.pop(0)
    b = ss.pop(0)
    ss.append(int((a * b) / math.gcd(a, b)))
print(ss[0])
