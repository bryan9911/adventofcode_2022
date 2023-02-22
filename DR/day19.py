import numpy as np
from functools import reduce
import time
from util import read_input
lines = read_input()

s = time.time()

def parse(l):
    ret = []

    msg = "costs "
    s_idx = l.find(msg)+len(msg)
    c1 = int(l[s_idx:].split()[0])
    ret.append([[c1,0,0,0], [1,0,0,0]])

    l = l[s_idx+1:]
    msg = "costs "
    c1 = int(l[l.find(msg)+len(msg):].split()[0])
    ret.append([[c1,0,0,0], [0,1,0,0]])

    l = l[s_idx+1:]
    msg = "costs "
    s_idx = l.find(msg)+len(msg)
    c1 = int(l[s_idx:].split()[0])
    c2 = int(l[s_idx:].split()[3])
    ret.append([[c1,c2,0,0], [0,0,1,0]])

    l = l[s_idx+1:]
    msg = "costs "
    s_idx = l.find(msg)+len(msg)
    c1 = int(l[s_idx:].split()[0])
    c2 = int(l[s_idx:].split()[3])
    ret.append([[c1,0,c2,0], [0,0,0,1]])

    return ret

def time_to_create_robot(resource, cur_robots, robot):
    delta = robot[0] - resource
    if max(delta) <= 0:
        return 0
    
    for i in range(4):
        if delta[i] > 0 and cur_robots[i] == 0:
            return -1

    t = -1
    for i in range(4):
        if delta[i] <= 0:
            continue
        t = max(t, (delta[i]+cur_robots[i]-1) // cur_robots[i])

    return t

def search(robots, robot_limits, cur_resource, cur_robots, remaining_time):
    global max_geode_found
    has_child = False
    # A*, I thought reversing robots will make faster, but **MAYBE** due to limiting robots, original order makes program 1/3 faster
    for i, r in enumerate(robots):
        t = time_to_create_robot(cur_resource, cur_robots, r)
        # A*, Cut branches if algorithm tries to create more robots than needed(max from resources required)
        if t >= 0 and cur_robots[i] < robot_limits[i] and remaining_time - t - 1 >= 0:
            # A*, Cut branches if maximum geode is less than max_geode_found
            expected_max = cur_resource[-1] + remaining_time * cur_robots[-1] + remaining_time*(remaining_time-1)//2
            if expected_max < max_geode_found:
                continue
            has_child = True
            search(robots, robot_limits, cur_resource+cur_robots*(t+1)-r[0], cur_robots+r[1], remaining_time-t-1)

    # If used all time, update max_geode_found
    if not has_child:
        final_resource = cur_resource + remaining_time * cur_robots[-1]
        max_geode_found = max(max_geode_found, final_resource[-1])

part1 = 0
part2 = 1
for i, l in enumerate(lines):
    max_geode_found = 0
    robots = parse(l)
    limits = reduce(np.maximum, [r[0] for r in robots])
    limits[-1] = 100000
    search(robots, limits, np.array([0,0,0,0]), np.array([1,0,0,0]), 24)
    part1 += (i+1) * max_geode_found
    if i < 3:
        search(robots, limits, np.array([0,0,0,0]), np.array([1,0,0,0]), 32)
        part2 *= max_geode_found

print("part1:", part1)
print("part2:", part2)


print("Time spent :", time.time() - s)	