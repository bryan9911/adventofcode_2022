import numpy as np

Data = open('Day1.txt').readlines()
data = np.zeros(len(Data))
n = 0
for i in Data:
    data[n] = i.replace('\n', '0')
    n = n + 1

Calories = np.array(data, dtype=int)/10
Elf = np.zeros(len(Calories))
num = 0
for i in Calories:
    if i > 0:
        Elf[num] = Elf[num] + i
    elif i == 0:
        num = num + 1

max_elf = np.argmax(Elf)
print(Elf[max_elf])

flat = Elf.flatten()
flat.sort()
print(flat)
print(flat[-1]+flat[-2]+flat[-3])
