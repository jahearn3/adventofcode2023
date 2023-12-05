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
    # source, destination = m.split('-to-')
    for k,v in maps.items(): 
        # src, dest = k.split('-to-')
        # if src == prv_dest:
        if mo == k:
            print(k)
            mapping = {}
            for vv in v:
                dest_rng_start = int(vv[0])
                src_rng_start = int(vv[1])
                rng_length = int(vv[2])
                print(dest_rng_start, src_rng_start, rng_length)
                for m in range(rng_length):
                    mapping[src_rng_start + m] = dest_rng_start + m
                    if len(mapping) % 100 == 0:
                        print(f'mapping has length {len(mapping)}')
            print(mapping)
            # Look up dest for each src
            next_src = []
            for s in seed_trajectory:
                if s not in mapping:
                    next_src.append(s)
                else:
                    next_src.append(mapping[s])
                
            print(next_src)
            seed_trajectory = next_src
            


print(min(seed_trajectory))