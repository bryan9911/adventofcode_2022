import numpy as np
from util import read_input
lines = read_input()

def parse(l:str):
    s = l.replace(', ', '#').replace('=', ' ').replace(';','').split()
    return s[1], int(s[5]), s[-1].split('#')

def visited(idx:int, visit:int):
    return visit | (1 << idx) == visit

def max_release(cur_pos:str, remaining_time:int, visit:int, forward_release:int):
    cur_idx = rename_map[cur_pos]
    if cur_pos != 'AA':
        remaining_time -= 1
        visit += 1 << cur_idx
    
    for e in rename_map.keys():
        nxt_idx = rename_map[e]
        if flow[nxt_idx] and (remaining_time-dist[cur_idx][nxt_idx] > 0) and (not visited(nxt_idx, visit)):
            max_release(e, 
                        remaining_time-dist[cur_idx][nxt_idx], 
                        visit, 
                        forward_release + remaining_time * flow[cur_idx]
                       )

    results[visit] = max(results.get(visit, 0), forward_release + remaining_time * flow[cur_idx])

flow = {}
edge = {}
rename_map = {}
for i, l in enumerate(lines):
    name, rate, tunnels = parse(l)
    rename_map[name] = i
    flow[i] = rate
    edge[i] = tunnels

INF = 54321 
N = len(lines)
dist = np.empty(shape=(N, N))
dist.fill(INF)
for i in range(N):
    dist[i][i] = 0
for k, v in edge.items():
    for n in v:
        dist[k][rename_map[n]] = 1

for k in range(N):
    for i in range(N):
        for j in range(N):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

results = {}
max_release('AA', 30, 0, 0)
print(int(max(results.values())))

print(len(results))

results = {}
max_release('AA', 26, 0, 0)
part2 = -1
for visit1, v1 in results.items():
    for visit2, v2 in results.items():
        if not (visit1 & visit2):
            part2 = max(part2, v1 + v2)
print(int(part2))