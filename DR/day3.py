from util import read_input
lines = read_input()

# Part 1
import string
from functools import reduce
from operator import ior, iand
pool = string.ascii_lowercase + string.ascii_uppercase
def chr2priority(chr):
    return 1 + pool.find(chr)

def mask_includes_chr(mask, chr):
    return mask|(1 << chr2priority(chr)) == mask

dups = []
for l in lines:
    cnt = [0] * 53
    mid = len(l) // 2

    left_mask = reduce(ior, [(1 << chr2priority(i)) for i in l[:mid]])
    right_mask = 0
    for i in l[mid:]:
        if mask_includes_chr(left_mask, i) and not mask_includes_chr(right_mask, i):
            dups.append(i)
        right_mask |= (1 << chr2priority(i))

print(sum(chr2priority(i) for i in dups))

# Part 2
from math import log2 as mask2priority

dups = []
for i in range(0, len(lines), 3):
    rucksacks = lines[i:i+3]
    masks = []
    for r in rucksacks:
        masks.append(reduce(ior, [(1 << chr2priority(i)) for i in r]))

    dups.append(mask2priority(reduce(iand, masks)))

print(sum(dups))