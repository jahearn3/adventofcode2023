# Day 8: Haunted Wasteland

import load_data as ld 
import os 

f = os.path.basename(__file__)
day = f[3:5]

data = ld.load_data(f'example{day}.txt')
# data = ld.load_data(f'example{day}b.txt')
# data = ld.load_data(f'input{day}.txt')

instructions = data[0]
network = {}
for line in data[2:]:
    a, b = line.split(' = ')
    l, r = b.strip('()').split(',')
    r = r.strip()
    network[a] = (l, r)

start = 'AAA'
cur = 'AAA'
end = 'ZZZ'
ans = 0

while cur != end:
    for i, char in enumerate(instructions):
        if cur == end:
            break
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
network = {}
for line in data[2:]:
    a, b = line.split(' = ')
    l, r = b.strip('()').split(',')
    r = r.strip()
    network[a] = (l, r)

start = []
end = []
for k in network.keys():
    if k[-1] == 'A':
        start.append(k)
    elif k[-1] == 'Z':
        end.append(k)

print(start, end)

# cur = start
# ans = 0
# zs = 0
# maxzs = 0

# while zs != len(start):
#     for char in instructions:
#         next = []
#         if char == 'L':
#             for c in cur:
#                 next.append(network[c][0])
#         elif char == 'R':
#             for c in cur:
#                 next.append(network[c][1])
#         # print(next)
#         cur = next
#         zs = 0
#         for c in cur:
#             if c[-1] == 'Z':
#                 zs += 1
#         ans += 1
#         if zs > maxzs:
#             maxzs = zs
#             print(zs, ans, cur)

# print(ans)

# 293 incorrect

# Could find least common multiple 
# but don't know which start maps to which end, 
# so would need to do it for all

for s in start:
    # for e in end:
    cur = s
    ans = 0
    while cur[-1] != 'Z':
        for char in instructions:
            if char == 'L':
                next = network[cur][0]
            elif char == 'R':
                next = network[cur][1]
            # print(next)
            cur = next
            ans += 1
            if cur[-1] == 'Z':
                print(s, cur, ans)
                break

import math
a = 17873
b = 19631
c = 17287
d = 12599
e = 21389
f = 20803
lcm1 = (a*b)/math.gcd(a,b)
print(lcm1)
lcm2 = (c*d)/math.gcd(c,d)
print(lcm2)
lcm3 = (e*f)/math.gcd(e,f)
print(lcm3)
lcm4 = (int(lcm1)*int(lcm2))/math.gcd(int(lcm1),int(lcm2))
print(lcm4)
lcm5 = (int(lcm3)*int(lcm4))/math.gcd(int(lcm3),int(lcm4))
print(lcm5)
            