# Day 19: Aplenty 

import load_data as ld 
import os 

f = os.path.basename(__file__)
day = f[3:5]

data = ld.load_data(f'example{day}.txt')
data = ld.load_data(f'input{day}.txt')

workflows = []
ratings = [] 
accepted = []
rejected = []

initial = True 
for line in data:
    if len(line) == 0:
        initial = False
    elif initial:
        workflows.append(line)
    else:
        ratings.append(line)

# Set up workflows dict
wf = {}
for line in workflows:
    workflow, rules = line.strip('}').split('{')
    wf[workflow] = rules.split(',')

# Loop through ratings, assigning them to workflows
ans = 0
for r in ratings:
    print(r)
    x, m, a, s = r.strip('{}').split(',')
    x = int(x.split('=')[1])
    m = int(m.split('=')[1])
    a = int(a.split('=')[1])
    s = int(s.split('=')[1])

    running = True
    cur = 'in'
    count = 0
    while running:
        if count > 10:
            break 
        count += 1
        steps = wf[cur]
        for step in steps:
            if step in wf[cur]:
                print('step', step)
                if ':' in step:
                    condition, next = step.split(':')
                    print('condition', condition)
                    if '>' in condition:
                        # print('case 1')
                        var, num = condition.split('>')
                        # print(var, num)
                        num = int(num)
                        if var == 'x':
                            if x > num:
                                cur = next
                                # print(f'cur is now {cur}')
                        elif var == 'm':
                            if m > num:
                                cur = next
                                # print(f'cur is now {cur}')
                        elif var == 'a': 
                            if a > num:
                                cur = next
                                # print(f'cur is now {cur}')
                        elif var == 's':
                            if s > num:
                                cur = next
                                # print(f'cur is now {cur}')
                    if '<' in condition:
                        # print('case 2')
                        var, num = condition.split('<')
                        # print(var, num)
                        num = int(num)
                        if var == 'x':
                            if x < num:
                                cur = next
                                # print(f'cur is now {cur}')
                        elif var == 'm':
                            if m < num:
                                cur = next
                                # print(f'cur is now {cur}')
                        elif var == 'a': 
                            if a < num:
                                cur = next
                                # print(f'cur is now {cur}')
                        elif var == 's':
                            if s < num:
                                cur = next
                                # print(f'cur is now {cur}')
                else:
                    # print('case 0')
                    cur = step 
                if step == 'A' or cur == 'A':
                    print('accepted')
                    accepted.append(r)
                    ans += x + m + a + s 
                    print(ans)
                    running = False
                    break
                elif step == 'R' or cur == 'R':
                    # print('curr', cur)
                    print('rejected')
                    rejected.append(r)
                    running = False
                    break
                # print('cur', cur)
            



print(ans)
# 355385 too low
print()
print('Total: ')
print(len(ratings))

print()
print('Accepted: ')
print(len(accepted))

print()
print('Rejected: ')
print(len(rejected))