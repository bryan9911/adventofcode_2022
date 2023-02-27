import re
import math
from collections import deque


def options(current: list):
    dirs = [[0, 1], [1, 0], [0, -1], [-1, 0], [0, 0]]
    return [(current[0]+di[0], current[1]+di[1]) for di in dirs]


def bliz_gen(blizzard: dict, xl: int, yl: int):
    bliz_count = math.lcm(xl-2, yl-2)
    al_blizzard = [None]*bliz_count
    for i in range(bliz_count):
        cur_bliz = set()
        for bliz, dirs in blizzard.items():
            if dirs == '>':
                cur_bliz.add((bliz[0], (bliz[1] + i - 1) % (yl - 2) + 1))
            elif dirs == '<':
                cur_bliz.add((bliz[0], (bliz[1] - i - 1) % (yl - 2) + 1))
            elif dirs == '^':
                cur_bliz.add(((bliz[0] - i - 1) % (xl - 2) + 1, bliz[1]))
            elif dirs == 'v':
                cur_bliz.add(((bliz[0] + i - 1) % (xl - 2) + 1, bliz[1]))
            else:
                cur_bliz.add(bliz)
        al_blizzard[i] = cur_bliz
    return al_blizzard, bliz_count


def navigate(grid: list, blizz: list, lcm: int):
    x_len, y_len, start = len(grid), len(grid[0]), [0, grid[0].index('.'), 0]
    end, loopcount = [x_len-1, grid[x_len-1].index('.')], 0
    queue = deque([start])
    while queue:
        cur = queue.popleft()
        if cur[0] == end[0] and cur[1] == end[1]:
            loopcount += 1
            print(cur[2])
            if loopcount == 3:
                return cur[2]
            else:
                queue.clear()
                new_end = start
                start = [end[0], end[1], cur[2]]
                end = new_end
                queue.append(start)
        else:
            next_option = options(cur)
            for ne in next_option:
                if ne not in blizz[(cur[2]+1) % lcm]:
                    if 0 <= ne[0] <= x_len and 0 <= ne[1] <= y_len and [ne[0], ne[1], cur[2]+1] not in queue:
                        queue.append([ne[0], ne[1], cur[2]+1])
    if not queue:
        return 0


Lines = open('Day24.txt').readlines()
ini_grid = [re.findall(r'[#.<>v^]', line) for line in Lines]
blizzards = {(i, j): ini_grid[i][j] for i in range(len(ini_grid)) for j in range(len(ini_grid[0]))
             if ini_grid[i][j] != '.'}
all_blizzards, LCM = bliz_gen(blizzards, len(ini_grid), len(ini_grid[0]))
print(navigate(ini_grid, all_blizzards, LCM))
