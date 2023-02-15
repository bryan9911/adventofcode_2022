from util import read_input
lines = read_input()

max_y  = -1

def draw_rocks_from_points(p1, p2, bias):
    global max_y
    max_y = max(max_y, p1[1], p2[1])
    if p1[0] == p2[0]:
        s = min(p1[1], p2[1])
        e = max(p1[1], p2[1])
        for i in range(s, e+1): world[p1[0]+bias][i] = 1

    else:
        s = min(p1[0], p2[0])
        e = max(p1[0], p2[0])
        for i in range(s, e+1): world[i+bias][p1[1]] = 1

def create_rocks(line, bias=0):
    rock_points = [list(map(int, p.split(','))) for p in l.split(' -> ')]
    for i in range(1, len(rock_points)):
        draw_rocks_from_points(rock_points[i-1], rock_points[i], bias)

def is_valid_coord(x, y):
    return (0 <= x < world_size[0]-1) and (0 <= y < world_size[1]-1)

def drop_sand(x, y):
    if not is_valid_coord(x, y):
        return (-1, -1)
    
    if world[x][y+1] == 0:
        return drop_sand(x, y+1)
    elif world[x-1][y+1] == 0:
        return drop_sand(x-1, y+1)
    elif world[x+1][y+1] == 0:
        return drop_sand(x+1, y+1)
    
    world[x][y] = 2
    return (x, y)

# Part 1
world_size = (600, 180)
world = [[0]*world_size[1] for _ in range(world_size[0])]
for l in lines:
    create_rocks(l)

part1 = 0
while drop_sand(500, 0) != (-1, -1):
    part1 += 1
print(part1)

# Part 2
world_size = (1800, 180)
bias = 600
world = [[0]*world_size[1] for _ in range(world_size[0])]
for l in lines:
    create_rocks(l, bias)
draw_rocks_from_points([0, max_y+2], [world_size[0]-1, max_y+2], 0)

part2 = 0
while not world[500+bias][0]:
    drop_sand(500+bias, 0)
    part2 += 1
print(part2)