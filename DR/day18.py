import numpy as np
import sys
from util import read_input
lines = read_input()

WORLD_SIZE = 25
sys.setrecursionlimit(3*WORLD_SIZE**3)

def parse(l:str):
    return list(map(lambda x: int(x)+1, l.split(',')))

def is_lava(x, y, z):
    return world[x, y, z]

def count_surfaces(x, y, z, count_airpockets=True):
    dir = [[1, 0, 0], [0, 1, 0], [0, 0, 1], [-1, 0, 0], [0, -1, 0], [0, 0, -1]]
    ret = 0
    for d in dir:
        new_pos = np.array([x,y,z])+d
        if not is_valid_coord(*new_pos):
            continue
        ret += (not is_lava(*new_pos)) and (count_airpockets or not is_airpocket(*new_pos))
    
    return ret

not_airpocket_near_lava = set()

def is_valid_coord(x, y, z):
    return (0 <= x < WORLD_SIZE) and (0 <= y < WORLD_SIZE) and (0 <= z < WORLD_SIZE)

def scan_air(x, y, z, visit):
    if not is_valid_coord(x, y, z):
        return
    
    dir = [[1, 0, 0], [0, 1, 0], [0, 0, 1], [-1, 0, 0], [0, -1, 0], [0, 0, -1]]

    visit.add((x, y, z))
    has_lava_near = False
    for d in dir:
        new_pos = np.array([x,y,z])+d

        if not is_valid_coord(*new_pos):
            continue
        if world[*new_pos] == 1:
            has_lava_near = True
        if tuple(new_pos) not in visit and world[*new_pos] == 0:
            scan_air(*new_pos, visit)

    if has_lava_near:
        not_airpocket_near_lava.add((x, y, z))

def is_airpocket(x, y, z):
    return (x, y, z) not in not_airpocket_near_lava

world = a = np.zeros((WORLD_SIZE, WORLD_SIZE, WORLD_SIZE))

for l in lines:
    world[*parse(l)] = 1

part1 = 0
part2 = 0
scan_air(0, 0, 0, set())
for l in lines:
    args = parse(l)
    part1 += count_surfaces(*args)
    part2 += count_surfaces(*args, False)

print(int(part1))
print(int(part2))