from util import read_input
lines = read_input()

def parse(s):
    return [int(x) for x in s.replace("move ", "").replace(" from ", ",").replace(" to ", ",").split(",")]

def part1_move(cnt, src, dst):
    src -= 1
    dst -= 1
    for _ in range(cnt):
        stack[dst].append(stack[src].pop())

def part2_move(cnt, src, dst):
    src -= 1
    dst -= 1
    stack[dst].extend(stack[src][-cnt:])
    stack[src] = stack[src][:-cnt]

from copy import deepcopy
stack = [[] for _ in range(9)]

# Create stack
for l in lines[:8]:
    for i in range(9):
        c = l[4*i + 1]
        if c != ' ':
            stack[i].append(c)
[x.reverse() for x in stack]

# Deepcopy for part 2
stack_bak = deepcopy(stack)

# Part 1
for l in lines[10:]:
    args = parse(l)
    part1_move(*args)

print(''.join([x[-1] for x in stack]))

# Part 2
stack = stack_bak # Recover stack
for l in lines[10:]:
    args = parse(l)
    part2_move(*args)

print(''.join([x[-1] for x in stack]))