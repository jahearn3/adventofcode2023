# Day 20: Pulse Propagation

import load_data as ld 
import os 

f = os.path.basename(__file__)
day = f[3:5]

data = ld.load_data(f'example{day}.txt')
# data = ld.load_data(f'example{day}b.txt')
# data = ld.load_data(f'input{day}.txt')

modules = {} 
for line in data:
    a, b = line.split('->')
    a = a.strip()
    b = b.strip()
    if a == 'broadcaster':
        modules[a] = b
    else:
        c = a[0]
        a = a[1:]
        if c == '%':
            modules[a] = (c, b, 0)
            # c = type of module (flip-flop or conjunction)
            # b = destination(s)
            # 0 for off
        elif c == '&':
            modules[a] = (c, b, [])
            # if ',' in b:
            #     dests = b.split(',')

print(modules)

low_pulses = 0
high_pulses = 0

for i in range(1000):
    print('button', 'low', 'broadcaster')
    low_pulses += 1
    destination = modules['broadcaster']
    q = []
    if ',' in destination:
        dests = destination.split(',')
        for d in dests:
            d = d.strip()
            print('broadcaster', 'low', d)
            low_pulses += 1
            q.append(d)
    else:
        d = destination.strip()
        print('broadcaster', 'low', d)
        low_pulses += 1
        q.append(d)
    
    most_recent = 'low'
    propagating = True 
    while propagating:
        cur = q.pop()
        if cur == 'broadcaster':
            pass #!TODO
        else:
            mod_type, dest, state = modules[cur]
            if mod_type == '%':
                if state == 0:
                    modules[cur] = (mod_type, dest, 1)
                    if ',' in dest:
                        dests = dest.split(',')
                        for d in dests:
                            d = d.strip()
                            print(cur, 'high', d)
                            high_pulses += 1
                            q.append(d)
                    else:
                        d = dest.strip()
                        print(cur, 'high', d)
                        high_pulses += 1
                        q.append(d)
                else:
                    modules[cur] = (mod_type, dest, 0)
                    if ',' in dest:
                        dests = dest.split(',')
                        for d in dests:
                            d = d.strip()
                            print(cur, 'low', d)
                            low_pulses += 1
                            q.append(d)
                    else:
                        d = dest.strip()
                        print(cur, 'low', d)
                        low_pulses += 1
                        q.append(d)
            elif mod_type == '&':
                mod_type, dest, state = modules[cur]

print(low_pulses * high_pulses)