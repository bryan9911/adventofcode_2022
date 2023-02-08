from collections import Counter
import numpy as np

Data = open('Day3.txt').readlines()
Data = list(map(lambda s: s.strip(), Data))
Temp = np.empty(len(Data), dtype=int)
Final = np.zeros(len(Data))
n = 0

for i in Data:
    temp1 = Counter(i[0:len(i)//2])
    temp2 = Counter(i[len(i)//2:])
    for char1, count1 in temp1.items():
        for char2, count2 in temp2.items():
            if char1 == char2:
                Temp[n] = ord(char1)
    n += 1

m = 0
for j in Temp:
    if 96 < j < 123:
        Final[m] = j - 96
    elif 64 < j < 91:
        Final[m] = j - 38
    m += 1

Temp2 = np.zeros(len(Data)//3)
Final2 = np.zeros(len(Data)//3)
q = 0
for n in range(0, len(Data)-1, 3):
    t1 = Counter(Data[n])
    t2 = Counter(Data[n+1])
    t3 = Counter(Data[n+2])
    for char1, count1 in t1.items():
        for char2, count2 in t2.items():
            for char3, count3 in t3.items():
                if char1 == char2 == char3:
                    Temp2[q] = ord(char1)
    q = q + 1

m = 0
for j in Temp2:
    if 96 < j < 123:
        Final2[m] = j - 96
    elif 64 < j < 91:
        Final2[m] = j - 38
    m += 1

print(np.sum(Final2))
