import re
import math
from collections import deque


def mining(b_print: list, minute: int):
    bp = [[b_print[1], 0, 0, 0], [b_print[2], 0, 0, 0], [b_print[3], b_print[4], 0, 0], [b_print[5], 0, b_print[6], 0]]
    initial_robot, initial_mineral, best = [1, 0, 0, 0], [0, 0, 0, 0], 0
    max_req = [max(bps[i]for bps in bp) for i in range(4)]  # KEYPOINT
    queue = deque([[initial_robot, initial_mineral, minute]])
    while queue:
        curr = queue.popleft()
        robot, mineral, time = curr[0], curr[1], curr[2]
        best = max(mineral[3]+robot[3]*time, best)
        ind_n_time = possibility(robot, mineral, time, bp, max_req)
        if ind_n_time:
            for i_n_t in ind_n_time:
                new_mineral = [mineral[i]+robot[i]*i_n_t[1]-bp[i_n_t[0]][i] for i in range(4)]
                new_robot = robot[:]
                new_robot[i_n_t[0]] += 1
                queue.append([new_robot, new_mineral, time-i_n_t[1]])
    return best


def possibility(robots: list, minerals: list, timeleft: int, blueprints: list, maximum_req: list):
    pos, ret = [], []
    for i in range(4):
        if all(robots[j] > 0 if blueprints[i][j] > 0 else 1 for j in range(4)):
            pos.append(i)
    for po in pos:
        if maximum_req[po] > robots[po] if maximum_req[po] > 0 else 1:  # KEYPOINT
            req = [blueprints[po][i] - minerals[i] for i in range(4)]
            det = (math.ceil(max(req)/robots[req.index(max(req))]) + 1 if max(req) > 0 else 1)
            if timeleft - det > 0:
                ret.append([po, det])
    return ret


Lines = open('Day19.txt').readlines()
digits = [re.findall(r'\d+', line) for line in Lines]
Blueprint = [[int(di) for di in dig] for dig in digits]
geodes = []

# part1
for blue in Blueprint:
    geodes.append(mining(blue, 24))
    print(blue[0], end='')
    print(' done')
print(geodes)
part1 = 0
for ii in range(len(geodes)):
    part1 += geodes[ii]*(ii+1)
print(part1)

# part2
for i in range(3):
    geodes.append(mining(Blueprint[i], 32))
    print(i, end='')
    print(' done')
print(geodes[0]*geodes[1]*geodes[2])
