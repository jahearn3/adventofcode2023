# Day 2: Cube Conundrum

import load_data as ld 

data = ld.load_data('example02.txt')
data = ld.load_data('input02.txt')

ans = 0

for line in data:
    game, draws = line.split(':')
    _, id = game.split(' ')
    idx = int(id)
    games = draws.split(';')
    for i, g in enumerate(games):
        n_colors = g.split(',')
        for n_color in n_colors:
            n, c = n_color.strip().split(' ')
            if c == 'red' and int(n) > 12:
                idx = 0
                break 
            elif c == 'green' and int(n) > 13:
                idx = 0
                break
            elif c == 'blue' and int(n) > 14:
                idx = 0
                break 
    if i == len(games) - 1:
        ans += idx

print(ans)

# Part 2

ans = 0

for line in data:
    game, draws = line.split(':')
    _, id = game.split(' ')
    games = draws.split(';')
    min_red = 0
    min_green = 0
    min_blue = 0
    for i, g in enumerate(games):
        n_colors = g.split(',')
        for n_color in n_colors:
            n, c = n_color.strip().split(' ')
            if c == 'red' and int(n) > min_red:
                min_red = int(n)
            elif c == 'green' and int(n) > min_green:
                min_green = int(n)
            elif c == 'blue' and int(n) > min_blue:
                min_blue = int(n)
    if i == len(games) - 1:
        power = min_red * min_green * min_blue
        ans += power

print(ans)