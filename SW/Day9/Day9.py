import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def direction(name: str):
    if name == 'D':
        return [0, -1]
    elif name == 'U':
        return [0, 1]
    elif name == 'L':
        return [-1, 0]
    elif name == 'R':
        return [1, 0]


def tailmove(tail, head):
    head_tail = head-tail
    ht_scalar = head_tail[0]**2 + head_tail[1]**2
    if ht_scalar == 4:
        if head_tail[0] == 0:
            if head_tail[1] > 0:
                return [0, 1]
            else:
                return [0, -1]
        elif head_tail[1] == 0:
            if head_tail[0] > 0:
                return [1, 0]
            else:
                return [-1, 0]
    elif ht_scalar >= 5:
        if head_tail[0] > 0:
            if head_tail[1] > 0:
                return [1, 1]
            else:
                return [1, -1]
        elif head_tail[0] < 0:
            if head_tail[1] > 0:
                return [-1, 1]
            else:
                return [-1, -1]
    else:
        return [0, 0]


headmotion = pd.read_csv('Day9.txt', sep=' ')
dist = headmotion.Distance.to_numpy(dtype=int)
tot_dist = sum(dist)

headloca = np.zeros((tot_dist+1, 2), dtype=int)
tailloca = np.zeros((tot_dist+1, 2), dtype=int)
numloca = np.zeros((tot_dist+1, 9, 2), dtype=int)
origin = [0, 0]
cur = origin
headloca[0] = origin
tailloca[0] = origin

ind = 1
for h in range(0, len(headmotion)):
    key = headmotion['Direction'][h]
    D = direction(key)
    n = dist[h]
    for i in range(ind, ind+n):
        headloca[i] = headloca[i-1] + D
    ind += n

for i in range(1, len(headloca)):
    Dd = tailmove(tailloca[i-1], headloca[i])
    tailloca[i] = tailloca[i-1] + Dd
    numloca[i, 0] = tailloca[i]
    for j in range(1, 9):
        d = tailmove(numloca[i-1, j], numloca[i, j-1])
        numloca[i, j] = numloca[i-1, j] + d
        d = origin

tcount = np.unique(tailloca, axis=0)
print(len(tcount))
ncount = np.unique(numloca[:, 8], axis=0)
print(len(ncount))
