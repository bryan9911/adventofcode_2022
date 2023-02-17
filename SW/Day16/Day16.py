import re


def find_distance(inp: list):
    dist = {}
    for i in inp:
        for j in inp:
            if j[0] in i[2]:
                dist[i[0], j[0]] = 1
            else:
                dist[i[0], j[0]] = 100
    return dist


def update_distance(dis: dict, inp: list):
    for k in inp:
        for i in inp:
            if k != i:
                for j in inp:
                    if j != k and j != i:
                        dis[i, j] = min(dis[i, j], dis[i, k] + dis[k, j])


def find_route(dep: str, minute: int, pressure: int, visited: int, res: dict):
    if visited not in res or res[visited] < pressure:
        res[visited] = pressure
    for w in w_valves:
        if w[0] & visited == 0:
            det = minute - distance[dep, w[1]] - 1
            if det >= 0:
                find_route(w[1], det, pressure + det * w[2], visited + w[0], res)
            else:
                continue
        else:
            continue


Lines = open('Day16.txt').readlines()
Lines = list(map(lambda s: s.strip(), Lines))
valves = []
for line in Lines:
    te = re.sub(r'[,;]', '', line)
    temp = re.split(r'[ ,=;]', te)
    valves.append([temp[1], int(temp[5]), temp[10:]])

distance = find_distance(valves)
valve_name = list(zip(*valves))[0]
update_distance(distance, valve_name)
w_valves = []
for val in valves:
    if val[1] > 0:
        w_valves.append([2**len(w_valves), val[0], val[1]])

result, result2 = {}, {}
find_route('AA', 30, 0, 0, result)
print(max(result.values()))
find_route('AA', 26, 0, 0, result2)
pos_res2 = []
for rek1 in result2.keys():
    for rek2 in result2.keys():
        if rek1 & rek2 == 0:
            pos_res2.append(result2[rek1]+result2[rek2])
print(max(pos_res2))
