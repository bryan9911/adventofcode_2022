import re
from collections import deque
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def adjacents(drops: list):
    sides = [6] * len(Droplet)
    for i in range(len(drops)):
        lrus = [[1, 0, 0], [-1, 0, 0], [0, 1, 0], [0, -1, 0], [0, 0, 1], [0, 0, -1]]
        for lru in lrus:
            check = [drops[i][0] + lru[0], drops[i][1] + lru[1], drops[i][2] + lru[2]]
            if check in drops:
                sides[i] -= 1
    return sides


def obsidian(mini: list, maxi: list, drops: list):
    out_side = 0
    queue, visited, edge = deque([maxi]), deque(), []
    leriups = [[1, 0, 0], [-1, 0, 0], [0, 1, 0], [0, -1, 0], [0, 0, 1], [0, 0, -1]]
    while queue:
        drop = queue.popleft()
        visited.append(drop)
        for lru in leriups:
            check = [drop[0]+lru[0], drop[1]+lru[1], drop[2]+lru[2]]
            if mini[0] <= check[0] <= maxi[0] and mini[1] <= check[1] <= maxi[1] and mini[2] <= check[2] <= maxi[2]:
                if check not in visited and check not in queue:
                    if check in drops:
                        edge.append(check)
                        out_side += 1
                    else:
                        queue.append(check)
    return out_side, edge


Lines = open('Day18.txt').readlines()
digits = [re.findall(r'\d+', line) for line in Lines]
Droplet = [[int(di) for di in dig] for dig in digits]
x, y, z = [i[0] for i in Droplet], [j[1] for j in Droplet], [k[2] for k in Droplet]
mindrop, maxdrop = [min(x)-1, min(y)-1, min(z)-1], [max(x)+1, max(y)+1, max(z)+1]
Droplet.sort(key= lambda row: (row[0], row[1], row[2]))
Side = adjacents(Droplet)
ext_side, vis = obsidian(mindrop, maxdrop, Droplet)
print(sum(Side))
print(ext_side)

vx, vy, vz = [i[0] for i in vis], [j[1] for j in vis], [k[2] for k in vis]
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(vx, vy, vz, color='b')
plt.show()
