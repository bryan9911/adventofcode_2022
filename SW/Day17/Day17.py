import re
from collections import deque


def generate_rocks(num: int, chamber: list):
    res = deque(chamber)
    for _ in range(3):
        res.extendleft([['.']*7])
    if num == 1:
        rocks = [['@', '@', '@', '@']]
    elif num == 2:
        rocks = [['.', '@', '.'], ['@', '@', '@'], ['.', '@', '.']]
    elif num == 3:
        rocks = [['.', '.', '@'], ['.', '.', '@'], ['@', '@', '@']]
    elif num == 4:
        rocks = [['@'], ['@'], ['@'], ['@']]
    elif num == 0:
        rocks = [['@', '@'], ['@', '@']]
    for i in reversed(range(len(rocks))):
        temp_row = ['.']*7
        for j in range(0, len(rocks[i])):
            if rocks[i][j] == '@':
                temp_row[j+2] = rocks[i][j]
        res.extendleft([temp_row])
    return list(res)


def tetris(chamber: list, inst: list, jet_index: int):
    jet_index = jet_index % len(inst)
    ins = inst[jet_index]
    jet_index += 1
    rock_loca = [[x, y] for x, li in enumerate(chamber) for y, val in enumerate(li) if val == '@']
    temp_y = sorted([i[1]+ins for i in rock_loca])
    if temp_y[0] >= 0 and temp_y[-1] <= 6:
        side_check = False
        for rock in rock_loca:
            if chamber[rock[0]][rock[1]+ins] == '#':
                side_check = True
        if side_check is False:
            for rock in rock_loca:
                chamber[rock[0]][rock[1]] = '.'
            for rock in rock_loca:
                rock[1] += ins
                chamber[rock[0]][rock[1]] = '@'
    down_check = False
    for rock in rock_loca:
        if chamber[rock[0]+1][rock[1]] == '#':
            down_check = True
    if down_check is False:
        for rock in rock_loca:
            chamber[rock[0]][rock[1]] = '.'
            rock[0] += 1
        for rock in rock_loca:
            chamber[rock[0]][rock[1]] = '@'
        if '#' not in chamber[0]:
            del chamber[0]
        temp_c = tetris(chamber, inst, jet_index)
        chamber, jet_index = temp_c[0], temp_c[1]
    elif down_check is True:
        for rock in rock_loca:
            chamber[rock[0]][rock[1]] = '#'
    return [chamber, jet_index]


lines = open('Day17.txt').readlines()
left, jet = '<', []
lefts = [i.start() for i in re.finditer(left, lines[0])]
for i in range(len(lines[0])):
    if i in lefts:
        jet.append(-1)
    else:
        jet.append(1)

Chamber, Jetindex = [['#']*7], 0

# part 1
for k in range(1, 2023):
    temp = tetris(generate_rocks(k % 5, Chamber), jet, Jetindex)
    Chamber, Jetindex = temp[0], temp[1]
print(len(Chamber)-1)

# part 2
jet_indexes = [0]*len(jet)
rock_index, k = [], 1
while k:
    temp = tetris(generate_rocks(k % 5, Chamber), jet, Jetindex)
    Chamber, Jetindex = temp[0], temp[1]
    rock_index.append([k, Jetindex, len(Chamber)-1, Chamber[0]])
    jet_indexes[Jetindex] += 1
    k += 1
    if jet_indexes[Jetindex] == 3:
        tpi = []
        for ri in rock_index:
            if ri[1] == Jetindex and ri[0] % 5 == (k-1) % 5 and ri[3] == Chamber[0]:
                tpi.append(ri)
        if len(tpi) == 3:
            cand = tpi
            k = 0
start, period, p_height = cand[1][0], cand[2][0]-cand[1][0], cand[2][2]-cand[1][2]
tot = 1000000000000
iteration, remainder = divmod(tot-start, period)
print(iteration*p_height + rock_index[start+remainder-1][2])
