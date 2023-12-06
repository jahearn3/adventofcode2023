# Day 5: If You Give A Seed A Fertilizer

import load_data as ld 
import os 

f = os.path.basename(__file__)
day = f[3:5]

data = ld.load_data(f'example{day}.txt')
# data = ld.load_data(f'input{day}.txt')

ans = 0

seeds = data[0].split(':')[1].strip().split()
maps = {'seed-to-soil': [], 
        'soil-to-fertilizer': [],
        'fertilizer-to-water': [],
        'water-to-light': [],
        'light-to-temperature': [],
        'temperature-to-humidity': [],
        'humidity-to-location': []
        }

map_order = ['seed-to-soil', 
        'soil-to-fertilizer',
        'fertilizer-to-water',
        'water-to-light',
        'light-to-temperature',
        'temperature-to-humidity',
        'humidity-to-location']

for i, line in enumerate(data):
    if(i > 0):
        for k in maps.keys():
            if k in line:
                j = i + 1
                while len(data[j]) > 0:
                    maps[k].append(data[j].strip().split())
                    j += 1
                    if j == len(data):
                        break

seed_trajectory = list(map(int, seeds))
for mo in map_order:
    for k,v in maps.items(): 
        if mo == k:
            next_src = []
            for s in seed_trajectory:
                s_next = s
                for vv in v:
                    dest_rng_start = int(vv[0])
                    src_rng_start = int(vv[1])
                    rng_length = int(vv[2])
                    if src_rng_start <= s <= src_rng_start + rng_length:
                        s_next = dest_rng_start + s - src_rng_start
                next_src.append(s_next)
            seed_trajectory = next_src
      
print(min(seed_trajectory))

# Part 2, with help from HyperNeutrino's YouTube video
seed_trajectory = list(map(int, seeds))
seeds = []
for i in range(1, len(seed_trajectory), 2):
    start = seed_trajectory[i-1]
    rng = seed_trajectory[i]
    seeds.append((start, start + rng))

for mo in map_order:
    for k,v in maps.items(): 
        if mo == k:
            new = []
            while len(seeds) > 0:
                start, end = seeds.pop()
                for a, b, c in v:
                    dest_rng_start = int(a)
                    src_rng_start = int(b)
                    rng_length = int(c)
                    overlap_start = max(start, src_rng_start)
                    overlap_end = min(end, src_rng_start + rng_length)
                    if overlap_start < overlap_end:
                        new.append((overlap_start - src_rng_start + dest_rng_start, overlap_end - src_rng_start + dest_rng_start))
                        if overlap_start > start:
                            seeds.append((start, overlap_start))
                        if end > overlap_end:
                            seeds.append((overlap_end, end))
                        break 
                else:
                    new.append((start, end))
            seeds = new
            
print(min(seeds)[0])