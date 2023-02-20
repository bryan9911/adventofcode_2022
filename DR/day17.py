import numpy as np
import sys
from util import read_input
lines = read_input()

sys.setrecursionlimit(10000)

shapes = [
    [
        [1, 1, 1, 1],
        [0, 0, 0, 0]
    ], [
        [2, 3, 2],
        [1, 0, 1]
    ], [
        [1, 1, 3],
        [0, 0, 0]
    ], [
        [4],
        [0]
    ], [
        [2, 2],
        [0, 0]
    ], 
]

def does_intersect(pos, rock):
    x = pos[0]; y = pos[1]
    rock_width = len(rock[0])
    for i in range(rock_width):
        rock_range = range(rock[1][i], rock[0][i])
        for j in rock_range:
            if world[y+j][x+i]:
                return False
    return True

def can_rock_move_left(pos, rock):
    x = pos[0]; y = pos[1]
    if x <= 0:
        return False
    return does_intersect([x-1,y], rock)

def can_rock_move_right(pos, rock):
    x = pos[0]; y = pos[1]
    if 7 <= x + rock_width:
        return False
    return does_intersect([x+1,y], rock)

def can_rock_fall(pos, rock):
    x = pos[0]; y = pos[1]
    if y == 0:
        return False
    return does_intersect([x,y-1], rock)

def is_valid_coord(x, y):
    return (0 <= x < 7) and (0 <= y)

dirs = [[1, 0], [-1, 0], [0, -1]]
def reachable(x, y, max_y, s):
    s.add((x, max_y - y))
    for d in dirs:
        new_x = x+d[0]; new_y = y+d[1]
        if not is_valid_coord(new_x, new_y):
            continue
        if (new_x, max_y - new_y) not in s and not world[new_y][new_x]:
            reachable(new_x, new_y, max_y, s)

def skyline_hash():
    ret = set()
    reachable(0, max(skyline) + 1, max(skyline) + 1, ret)
    return tuple(ret)

world = [[0]*7]
skyline = [0] * 7
shape_idx = 0
new_rock = True
rock_cnt = 0
jet_cnt = 0
cache = {}
solved_cnt = 0
cache_hit = False
while True:
    c = lines[0][jet_cnt]
    jet_cnt  = (jet_cnt + 1) % len(lines[0])
    if new_rock:
        rock_cnt += 1
        if rock_cnt % 100000 == 0:
            print(f"trying rock #{rock_cnt}")
        new_rock = False
        rock = shapes[shape_idx]
        shape_idx = (shape_idx + 1) % len(shapes)

        rock_width = len(rock[0])
        left_bottom_pos = [2, max(skyline) + 3]

        while len(world) < left_bottom_pos[1] + max(rock[0]) + 1:
            world.append([0]*7)


    if c == '<' and can_rock_move_left(left_bottom_pos, rock):
        left_bottom_pos[0] -= 1
    if c == '>' and can_rock_move_right(left_bottom_pos, rock):
        left_bottom_pos[0] += 1
    
    if can_rock_fall(left_bottom_pos, rock):
        left_bottom_pos[1] -= 1
    
    else:
        for i in range(rock_width):
            skyline[left_bottom_pos[0]+i] = max(skyline[left_bottom_pos[0]+i], left_bottom_pos[1] + rock[0][i])
            for j in range(left_bottom_pos[1]+rock[1][i], left_bottom_pos[1]+rock[0][i]):
                world[j][left_bottom_pos[0]+i] = 1
        
        if rock_cnt == 2022:
            print("part1:", max(skyline))
            solved_cnt += 1
        new_rock = True
        
        uid = (jet_cnt, shape_idx, skyline_hash())

        if not cache_hit:
            if uid in cache:
                print("Cache hit!", cache[uid], rock_cnt)
                cache_rock_cnt = cache[uid][0]
                cache_skyline_height = cache[uid][1]
                cycle = (rock_cnt - cache_rock_cnt)
                target_cnt = (1000000000000 - rock_cnt) % cycle + rock_cnt
                height_per_cycle = max(skyline) - cache_skyline_height
                print("Target Rock # =", target_cnt)
                cache_hit = True
            cache[uid] = (rock_cnt, max(skyline))
        else:
            if rock_cnt == target_cnt:
                print("part2:", max(skyline) + height_per_cycle * (1000000000000-rock_cnt) // cycle)
                solved_cnt += 1

        if solved_cnt == 2:
            break