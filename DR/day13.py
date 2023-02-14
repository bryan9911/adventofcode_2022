from util import read_input
lines = read_input()

def value2return(l:int, r:int):
    if l == r:
        return 0
    if l < r:
        return 1
    return -1

def compare(l, r):
    type_l = type(l)
    type_r = type(r)
    if type_l == int and type_r == int:
        return value2return(l, r)
    if type_l == int and type_r == list:
        return compare([l], r)
    if type_l == list and type_r == int:
        return compare(l, [r])
    
    long_side = value2return(len(l), len(r))
    for i in range(min(len(l), len(r))):
        c = compare(l[i], r[i])
        if c == 0:
            continue
        return c

    return long_side
    
# Part 1
def lineno2index(lineno):
    return lineno//3 + 1

part1 = 0
for i in range(0, len(lines), 3):
    if compare(eval(lines[i]), eval(lines[i+1])) == 1:
        part1 += lineno2index(i)
print(part1)

# Part 2
from functools import cmp_to_key

packets = []
for l in lines:
    if l:
        packets.append(eval(l))
packets.extend([[[2]], [[6]]])

packets.sort(key=cmp_to_key(compare), reverse=True)

part2 = 1
for i, p in enumerate(packets):
    if p == [[2]] or p == [[6]]:
        part2 *= i+1
print(part2)