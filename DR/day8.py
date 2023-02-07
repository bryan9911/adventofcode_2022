from functools import reduce
from operator import imul
from util import read_input
lines = read_input()

X = len(lines)
Y = len(lines[0])
trees = [[] for _ in range(Y)]

def is_valid_coord(x, y):
    return (0 <= x < X) and (0 <= y < Y)

def is_visible_dir(x, y, d, height):
    if not is_valid_coord(x, y):
        return True
    return is_visible_dir(x+d[0], y+d[1], d, height) and (trees[x][y] < height)

def is_visible(x, y):
    for d in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
        if is_visible_dir(x+(d[0]), y+d[1], d, trees[x][y]):
            return True
    return False

def scenic_score_dir(x, y, d, height):
    if not is_valid_coord(x, y):
        return 0
    return scenic_score_dir(x+d[0], y+d[1], d, height) + 1 if  (trees[x][y] < height) else 1

def scenic_score(x, y):
    return reduce(imul, [scenic_score_dir(x+(d[0]), y+d[1], d, trees[x][y]) for d in [[0, 1], [1, 0], [0, -1], [-1, 0]]])

for i, l in enumerate(lines):
    trees[i].extend([int(v) for v in l])

part1 = 0
part2 = -1
for x in range(X):
    for y in range(Y):
        part1 += is_visible(x, y)
        part2 = max(part2, scenic_score(x, y))
        
print(part1, part2)