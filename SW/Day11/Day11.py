import numpy as np

count = np.zeros(8, dtype=int)
MI = [[84, 66, 62, 69, 88, 91, 91],
      [98, 50, 76, 99],
      [72, 56, 94],
      [55, 88, 90, 77, 60, 67],
      [69, 72, 63, 60, 72, 52, 63, 78],
      [89, 73],
      [78, 68, 98, 88, 66],
      [70]]
MO = [[2, 4, 7],
      [7, 3, 6],
      [13, 4, 0],
      [3, 6, 5],
      [19, 1, 7],
      [17, 2, 0],
      [11, 2, 5],
      [5, 1, 3]]
factor = 1
for m in MO:
    factor *= m[0]


def monkey(num: int):
    old = MI[num].pop(0)
    new = cal(old, num) // 3
    if (new % MO[num][0]) == 0:
        MI[MO[num][1]].insert(-1, new)
    else:
        MI[MO[num][2]].insert(-1, new)
    count[num] += 1


def monkey2(num: int):
    old = MI[num].pop(0)
    new = cal(old, num)
    if new > factor:
        new = new % factor
    if (new % MO[num][0]) == 0:
        MI[MO[num][1]].insert(-1, new)
    else:
        MI[MO[num][2]].insert(-1, new)
    count[num] += 1


def cal(numin, n):
    if n == 0:
        return numin * 11
    elif n == 1:
        return numin * numin
    elif n == 2:
        return numin + 1
    elif n == 3:
        return numin + 2
    elif n == 4:
        return numin * 13
    elif n == 5:
        return numin + 5
    elif n == 6:
        return numin + 6
    elif n == 7:
        return numin + 7


for _ in range(0, 10000):
    for i in range(0, len(MI)):
        for j in range(0, len(MI[i])):
            monkey2(i)
res = sorted(count)
print(res[-1]*res[-2])
