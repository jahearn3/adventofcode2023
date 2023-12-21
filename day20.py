# Day 20: Pulse Propagation

import load_data as ld 
import os 
import copy 

f = os.path.basename(__file__)
day = f[3:5]

data = ld.load_data(f'example{day}.txt')
data = ld.load_data(f'example{day}b.txt')
data = ld.load_data(f'input{day}.txt')

# Setting up modules dict 
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
            modules[a] = [c, b, 0]
            # c = type of module (flip-flop or conjunction)
            # b = destination(s)
            # 0 for off
        elif c == '&':
            modules[a] = [c, b, {}]
            # if ',' in b:
            #     dests = b.split(',')

# For conjunction modules, populating the dict of their connected input modules
for key, val in modules.items():
    mod_type = val[0]
    if mod_type == '&':
        memory = {}
        for k, v in modules.items():
            if k != 'broadcaster':
                destinations = v[1]
                if key in destinations:
                    memory[k] = 'low' # default
                    val[2] = memory
                    modules[key] = val

modules_before = copy.deepcopy(modules)
# print(modules)
low_pulses = 0
high_pulses = 0

for i in range(1000):
    # print('button', 'low', 'broadcaster')
    low_pulses += 1
    destination = modules['broadcaster']
    q = []
    if ',' in destination:
        dests = destination.split(',')
        for d in dests:
            d = d.strip()
            # print('broadcaster', 'low', d)
            low_pulses += 1
            q.append(('broadcaster', 'low', d))
    else:
        d = destination.strip()
        # print('broadcaster', 'low', d)
        low_pulses += 1
        q.append(('broadcaster', 'low', d))
    
    while len(q) > 0:
        prev, pulse_type, cur = q.pop(0)
        if cur in modules:
            mod_type, dest, state = modules[cur]
            if mod_type == '%':
                if pulse_type == 'low':
                    if state == 0:
                        modules[cur] = [mod_type, dest, 1]
                        if ',' in dest:
                            dests = dest.split(',')
                            for d in dests:
                                d = d.strip()
                                # print(cur, 'high', d)
                                high_pulses += 1
                                q.append((cur, 'high', d)) 
                        else:
                            d = dest.strip()
                            # print(cur, 'high', d)
                            high_pulses += 1
                            q.append((cur, 'high', d)) 
                    else:
                        modules[cur] = [mod_type, dest, 0]
                        if ',' in dest:
                            dests = dest.split(',')
                            for d in dests:
                                d = d.strip()
                                # print(cur, 'low', d)
                                low_pulses += 1
                                q.append((cur, 'low', d))
                        else:
                            d = dest.strip()
                            # print(cur, 'low', d)
                            low_pulses += 1
                            q.append((cur, 'low', d))
            elif mod_type == '&':
                mod_type, dest, memory = modules[cur]

                # update memory for that input
                for k, v in memory.items():
                    if k == prev:
                        memory[k] = pulse_type
                        #* Not sure if I need to update the dict this way too
                        # val[2] = memory
                        # modules[key] = val

                # if it remembers high pulses for all inputs, send a low pulse
                count_values = 0
                count_highs = 0
                for v in memory.values():
                    count_values += 1
                    if v == 'high':
                        count_highs += 1
                if count_highs == count_values:
                    if ',' in dest:
                        dests = dest.split(',')
                        for d in dests:
                            d = d.strip()
                            # print(cur, 'low', d)
                            low_pulses += 1
                            q.append((cur, 'low', d))
                    else:
                        d = dest.strip()
                        # print(cur, 'low', d)
                        low_pulses += 1
                        q.append((cur, 'low', d))
                # otherwise send a high pulse
                else:
                    if ',' in dest:
                        dests = dest.split(',')
                        for d in dests:
                            d = d.strip()
                            # print(cur, 'high', d)
                            high_pulses += 1
                            q.append((cur, 'high', d))
                    else:
                        d = dest.strip()
                        # print(cur, 'high', d)
                        high_pulses += 1
                        q.append((cur, 'high', d))

    # with open('data/output20.txt', 'a') as myfile:
    #     myfile.write(str(i + 1) + '\t' + str(low_pulses * high_pulses) + '\n')
    # if (i + 1) % 100 == 0:
        # print(i + 1, low_pulses * high_pulses)
    # if modules == modules_before:
    #     print(f'match on iteration = {i+1}')
    #     print('Extrapolation:', int(low_pulses * high_pulses * 1000 / (i + 1)))
    #     break

print(low_pulses * high_pulses)

