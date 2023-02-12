import re
import numpy as np
from collections import deque


def neighbor(cur: [int, int], x, y):
    out = [[cur[0]+1, cur[1]], [cur[0]-1, cur[1]], [cur[0], cur[1]+1], [cur[0], cur[1]-1]]
    if cur[0] == 0:
        out.remove([cur[0]-1, cur[1]])
    elif cur[0] == x-1:
        out.remove([cur[0]+1, cur[1]])
    if cur[1] == 0:
        out.remove([cur[0], cur[1]-1])
    elif cur[1] == y-1:
        out.remove([cur[0], cur[1]+1])
    return out


def navigation(start: [int, int], end: [int, int], x, y):
    queue = deque()
    done = []
    queue.append([start])
    while queue:
        route = queue.popleft()
        current = route[-1]
        cur_height = grid[current[0]][current[1]]
        if current not in done:
            if current[0] == end[0] and current[1] == end[1]:
                return len(route)-1
            else:
                done.append(current)
                for nei in neighbor(current, x, y):
                    nei_height = grid[nei[0]][nei[1]]
                    if nei_height - cur_height <= 1:
                        temp = route[:]
                        temp.append(nei)
                        queue.append(temp)
    if not queue:
        return 0


Lines = open('Day12.txt').readlines()
amap = []
for line in Lines:
    amap.append(re.findall(r'\w', line))

grid = np.zeros((len(amap), len(amap[0])), dtype=int)
a_s = []
for i in range(len(amap)):
    for j in range(len(amap[0])):
        if amap[i][j] == 'S':
            h = 1
            Start_point = [i, j]
        elif amap[i][j] == 'E':
            h = 27
            End_point = [i, j]
        else:
            h = ord(amap[i][j]) - 96
        grid[i][j] = h
        if grid[i][j] == 1:
            a_s.append([i, j, 0])
print(navigation(Start_point, End_point, len(grid), len(grid[0])))

t = 10000
for a in a_s:
    a[2] = navigation([a[0], a[1]], End_point, len(grid), len(grid[0]))
    if 0 < a[2] < t:
        t = a[2]
        a_index = [a[0], a[1]]
print(t)
print(a_index)
