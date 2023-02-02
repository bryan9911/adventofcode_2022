from util import read_input
lines = read_input()

def parse(s):
    return [int(x) for x in s.split('-')]

def contains(a, b):
    if b[0] < a[0]:
        return contains(b, a)

    if a[0] == b[0]:
        return True
    return b[1] <= a[1]

def overlaps(a, b):
    if b[0] < a[0]:
        return overlaps(b, a)

    if a[0] == b[0]:
        return True
    return b[0] <= a[1]
part1 = 0
part2 = 0
for l in lines:
    part1 += contains(*(parse(x) for x in l.split(',')))
    part2 += overlaps(*(parse(x) for x in l.split(',')))

print(part1, part2)