# Day 17: Clumsy Crucible

import load_data as ld 
import os 

f = os.path.basename(__file__)
day = f[3:5]

data = ld.load_data(f'example{day}.txt')
data = ld.load_data(f'input{day}.txt')

ans = 0

# Dijkstra's algorithm (weighted search)
# 3-block limit is a wrench



print(ans)