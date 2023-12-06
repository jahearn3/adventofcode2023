# Day 6: Wait For It

import load_data as ld 
import os 

f = os.path.basename(__file__)
day = f[3:5]

data = ld.load_data(f'example{day}.txt')
data = ld.load_data(f'input{day}.txt')

ans = 1

times = list(map(int, data[0].split(':')[1].split()))
dists = list(map(int, data[1].split(':')[1].split()))


for i in range(len(times)):
    count = 0
    for j in range(times[i]):
        v = j
        d = v * (times[i] - j)
        if d > dists[i]:
            count += 1
    ans *= count
print(ans)

# Part 2

t = 50748685
dist = 242101716911252
count = 0
for j in range(t):
    v = j
    d = v * (t - j)
    if d > dist:
        count += 1
print(count)
# not 48