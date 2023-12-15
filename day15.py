# Day 15: Lens Library

import load_data as ld 
import os 

f = os.path.basename(__file__)
day = f[3:5]

data = ld.load_data(f'example{day}.txt')
data = ld.load_data(f'input{day}.txt')

lst = data[0].split(',')
# lst = ['H', 'A', 'S', 'H']
ans = 0
for item in lst:
    a = 0
    for char in item:
        a += ord(char)
        a *= 17
        a %= 256
    ans += a

print(ans)

# Part 2
import re 

boxes = {}

for i, item in enumerate(lst):
    match = re.match(r'(\D*?)(?=[-=]*\d*$)([-=]*)(\d*)', item)
    label = match.group(1)
    operation = match.group(2)
    focal_length = match.group(3)
    box = 0
    for char in label:
        box += ord(char)
        box *= 17
        box %= 256
    if operation == '-':
        # Remove lens with given label if it is present in the box
        if box in boxes:
            slots = boxes[box]
            for s, slot in enumerate(slots):
                if label == slot[0]:
                    slots.pop(s)
    elif operation == '=':
        if box in boxes:
            slots = boxes[box]
            labels = [x[0] for x in slots]
            if label in labels:
                for s, slot in enumerate(slots):
                    if label == slot[0]:
                        slots.pop(s)
                        slots.insert(s, (label, focal_length))
            else:
                slots.append((label, focal_length))
        else:
            boxes[box] = [(label, focal_length)]

# Add up the focusing power
ans = 0
for k, v in boxes.items():
    box_no = int(k) + 1
    slots = boxes[k]
    for s, slot in enumerate(slots):
        (label, focal_length) = slot
        ans += box_no * (s + 1) * int(focal_length)
print(ans)