from util import read_input
lines = read_input()

def distance(p1, p2):
    return abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])

points = []
for l in lines:
    for s in ['Sensor at x=', 'y=', ' closest beacon is at x=']:
        l = l.replace(s, '')
    points.append([list(map(int, s.split(', '))) for s in l.split(':')])

given_y = 2000000
no_beacon_ranges = []
min_x = 1000000000
max_x = -1000000000

for y in range(0, 4000000):
    no_beacon_ranges = []
    if y % 10000 == 0:
        print("debug", y)
    for s, b in points:
        d = distance(s, b)
        min_x = min(min_x, s[0], b[0])
        max_x = max(max_x, s[0], b[0])
        delta_x = d - abs(y - s[1])
        if delta_x < 0:
            continue
        no_beacon_ranges.append([s[0] - delta_x, s[0] + delta_x])

    no_beacon_ranges.sort()
    while True:
        has_intercept = False
        for i in range(1, len(no_beacon_ranges)):
            if no_beacon_ranges[i][0] <= no_beacon_ranges[i-1][1]:
                has_intercept = True
                no_beacon_ranges = no_beacon_ranges[:i-1] + \
                                [[no_beacon_ranges[i-1][0], max(no_beacon_ranges[i-1][1], no_beacon_ranges[i][1])]] + \
                                no_beacon_ranges[i+1:]
                break
        
        if not has_intercept:
            break

    has_possible_beacon_position = True
    for s, e in no_beacon_ranges:
        if s <= 0 and 4000000 <= e:
            has_possible_beacon_position = False
            break
    if has_possible_beacon_position:
        print("part2")
        print(no_beacon_ranges)
        print(y)

    if y == given_y:
        print(no_beacon_ranges)
        part1 = 0
        for src, dst in no_beacon_ranges:
            beacon_points = set()
            for s, b in points:
                if b[1] == given_y and src <= b[0] <= dst:
                    beacon_points.add(tuple(b))
            part1 += dst - src + 1 - len(beacon_points)

        print("part1:", part1)