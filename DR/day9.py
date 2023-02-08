from util import read_input
lines = read_input()

knot = [[0, 0] for _ in range(10)]
part1_visit = {tuple(knot[0])}
part2_visit = {tuple(knot[0])}
d2coord = {
    'R': [1,0],
    'L': [-1,0],
    'U': [0,1],
    'D': [0,-1]
}

def dist(x, y):
    return max(abs(x[1]-y[1]), abs(x[0]-y[0]))

def move(x, y):
    if dist(x, y) < 2:
        return [0, 0]

    delta = [x[0] - y[0], x[1] - y[1]]
    return [delta[0] // abs(delta[0]) if delta[0] else 0, delta[1] // abs(delta[1]) if delta[1] else 0]

for l in lines:
    d, cnt = l.split()
    cnt = int(cnt)

    for _ in range(cnt):
        knot[0] = [sum(x) for x in zip(knot[0], d2coord[d])]

        for i in range(9):
            knot[i+1] = [sum(x) for x in zip(knot[i+1], move(knot[i], knot[i+1]))]

        part1_visit.add(tuple(knot[1]))
        part2_visit.add(tuple(knot[-1]))

print(len(part1_visit), len(part2_visit))