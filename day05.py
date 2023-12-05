# Day 5: If You Give A Seed A Fertilizer

import load_data as ld 
import os 

f = os.path.basename(__file__)
day = f[3:5]

data = ld.load_data(f'example{day}.txt')
data = ld.load_data(f'input{day}.txt')

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
prv_dest = 'seed'
destination = 'soil'
for mo in map_order:
    for k,v in maps.items(): 
        if mo == k:
            print(k)
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