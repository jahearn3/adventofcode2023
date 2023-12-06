# Day 6: Wait For It

import load_data as ld 
import os 

f = os.path.basename(__file__)
day = f[3:5]
data = ld.load_data(f'example{day}.txt')
data = ld.load_data(f'input{day}.txt')

times = list(map(int, data[0].split(':')[1].split()))
dists = list(map(int, data[1].split(':')[1].split()))
ans = 1
for i in range(len(times)):
    count = 0
    for j in range(times[i]):
        if j * (times[i] - j) > dists[i]:
            count += 1
    ans *= count
print(ans)

# Part 2
t = int(data[0].split(':')[1].strip().replace(' ',''))
dist = int(data[1].split(':')[1].strip().replace(' ',''))
ans = 0
for j in range(t):
    if j * (t - j) > dist:
        ans += 1
print(ans)