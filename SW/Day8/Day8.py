import numpy as np

Tree = np.genfromtxt('Day8.txt', delimiter=1, dtype=int)
X = len(Tree)
Y = len(Tree[0])
vis_score = np.zeros((X, Y))

vis_count = 0

for x in range(0, X):
    for y in range(0, Y):
        if x == 0 or y == 0 or x == X-1 or y == Y-1:
            vis_count += 1
        else:
            count = True
            for rcheck in range(y+1, Y):
                if Tree[x, y] <= Tree[x, rcheck]:
                    count = False
                    break
                else:
                    count = True
            if not count:
                for lcheck in range(0, y):
                    if Tree[x, y] <= Tree[x, lcheck]:
                        count = False
                        break
                    else:
                        count = True
            if not count:
                for dcheck in range(x+1, X):
                    if Tree[x, y] <= Tree[dcheck, y]:
                        count = False
                        break
                    else:
                        count = True
            if not count:
                for ucheck in range(0, x):
                    if Tree[x, y] <= Tree[ucheck, y]:
                        count = False
                        break
                    else:
                        count = True
            if count:
                vis_count += 1

print(vis_count)

for x in range(0, X):
    for y in range(0, Y):
        if x != 0 and y != 0 and x != X-1 and y != Y-1:
            rscore = 0
            lscore = 0
            dscore = 0
            uscore = 0
            for rcheck in range(y+1, Y):
                if Tree[x, y] <= Tree[x, rcheck]:
                    rscore = rcheck-y
                    break
                else:
                    rscore = Y-1-y
            for lcheck in range(0, y):
                if Tree[x, y] <= Tree[x, y-lcheck-1]:
                    lscore = lcheck+1
                    break
                else:
                    lscore = y
            for dcheck in range(x+1, X):
                if Tree[x, y] <= Tree[dcheck, y]:
                    dscore = dcheck-x
                    break
                else:
                    dscore = X-1-x
            for ucheck in range(0, x):
                if Tree[x, y] <= Tree[x-ucheck-1, y]:
                    uscore = ucheck+1
                    break
                else:
                    uscore = x
            vis_score[x][y] = rscore * lscore * uscore * dscore

print(np.max(vis_score))
