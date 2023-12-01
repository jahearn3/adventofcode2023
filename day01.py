# Day 1: Trebuchet?!

import load_data as ld 
import re

data = ld.load_data('example01.txt')
data = ld.load_data('input01.txt')

ans = 0

for line in data:
    digits = re.findall(r'\d+', line)
    first_digit = str(digits[0])[0]
    last_digit = str(digits[-1])[-1]
    add = int(f'{first_digit}{last_digit}')
    ans += add
    
print(ans)

# Part 2

data = ld.load_data('example01b.txt')
data = ld.load_data('input01.txt')

ans = 0
numbers = {'one':1, 
           'two':2, 
           'three':3, 
           'four':4, 
           'five':5, 
           'six':6, 
           'seven':7, 
           'eight':8, 
           'nine':9,
           '1':1,
           '2':2,
           '3':3,
           '4':4,
           '5':5,
           '6':6,
           '7':7,
           '8':8,
           '9':9}

for line in data:
    # Find occurrences of numbers dictionary keys in line, and get their positions
    digits = []
    for k,v in numbers.items():
        for m in re.finditer(k, line):
            digits.append((v, m.start()))
    # Get digit that corresponds to minimum of position
    first_digit = min(digits, key=lambda x: x[1])[0]
    # Get digit that corresponds to maximum of position
    last_digit = max(digits, key=lambda x: x[1])[0]
    # Combine them and add to ans
    ans += int(f'{first_digit}{last_digit}')

print(ans)