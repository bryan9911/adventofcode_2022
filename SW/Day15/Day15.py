import re


def check_position(se: list, be: list, row: int):
    m_distance = abs(se[0]-be[0]) + abs(se[1]-be[1])
    if (se[1] - m_distance) <= row <= (se[1] + m_distance):
        temp = abs(se[1]-row)
        count.append([se[0]-(m_distance-temp), se[0]+(m_distance-temp)])


def add_position(cou: list):
    nc = sorted(cou, key=lambda row: (row[0], row[1]))
    result = []
    for n in nc:
        temp = False
        if len(result) == 0:
            result.append(n)
        else:
            for ii in range(len(result)):
                if result[ii][0] <= n[0] <= result[ii][1]:
                    if n[1] > result[ii][1]:
                        result[ii][1] = n[1]
                else:
                    temp = True
            if temp is True:
                result.append(n)
    for res in result:
        if res[0] < 0:
            res[0] = 0
        if res[1] > 4000000:
            res[1] = 4000000
    return result


sensor, beacon = [], []
Lines = open('Day15.txt').readlines()
Lines = list(map(lambda s: s.strip(), Lines))
for line in Lines:
    li = re.split(r'[ ,=:]', line)
    sensor.append([int(li[3]), int(li[6])])
    beacon.append([int(li[13]), int(li[16])])

tot = []
for j in range(0, 4000001):
    count = []
    for tw in range(len(sensor)):
        check_position(sensor[tw], beacon[tw], j)
    pos = add_position(count)
    if len(pos) > 1:
        tot.append([j, pos])

ans = tot[0][0] + (tot[0][1][0][1]+1)*4000000
print(ans)
