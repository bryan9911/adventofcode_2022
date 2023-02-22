import numpy as np
from itertools import cycle
from util import read_input
lines = read_input()

numbers = list(map(int, lines))
it = cycle(numbers.copy())

for _ in range(len(numbers)):
    i = next(it)
    idx = numbers.index(i)
    numbers.remove(i)
    target_idx = (idx + i + len(numbers)) % len(numbers)
    print(idx, target_idx)
    numbers.insert(target_idx, i)

zero_idx = numbers.index(0)
print("part 1:", [numbers[(zero_idx + i)%len(numbers)] for i in range(1000,3001,1000)])