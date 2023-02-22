import numpy as np
from itertools import cycle
from util import read_input
lines = read_input()

key = 811589153

numbers_raw = [(i, int(l)) for i, l in enumerate(lines)]
def solve(part=1):
    round = 10 if part==2 else 1
    key = 811589153 if part==2 else 1
    numbers = [(i, v*key) for i, v in numbers_raw]

    it = cycle(numbers.copy())
    for i, v in numbers:
        if v == 0:
            zero_idx = i

    for _ in range(round * len(numbers)):
        i = next(it)
        idx = numbers.index(i)
        numbers.remove(i)
        target_idx = (idx + i[1] + len(numbers)) % len(numbers)
        numbers.insert(target_idx, i)

    zero_idx = numbers.index((zero_idx, 0))
    return sum(numbers[(zero_idx + i)%len(numbers)][1] for i in range(1000,3001,1000))

print("part 1:", solve())
print("part 2:", solve(2))
