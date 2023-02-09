import numpy as np

Data = open('Day10.txt').readlines()
tot_cycle = 0
X = 1

for d in Data:
    temp = d.split()
    if temp[0] == 'addx':
        tot_cycle += 2
    else:
        tot_cycle += 1
Sig = np.zeros((tot_cycle, 3), dtype=int)

n = 0
for i in range(0, len(Data)):
    temp = Data[i].split()
    if temp[0] == 'addx':
        x_temp = int(temp[1])
        Sig[n] = [n, X, X]
        Sig[n+1] = [n+1, X,  X + x_temp]
        X += x_temp
        n += 2
    else:
        Sig[n] = [n, X, X]
        n += 1

sig_sum = 0
for j in [20, 60, 100, 140, 180, 220]:
    sig_sum += j*Sig[j-1, 1]
print(sig_sum)
    
CRT = np.zeros(tot_cycle, dtype=str)
for k in range(0, len(CRT)):
    if (Sig[k, 1] - 1) <= Sig[k, 0] % 40 <= (Sig[k, 1] + 1):
        CRT[k] = '#'
    else:
        CRT[k] = '.'
    print(CRT[k], end='')
    if (k % 40) == 39:
        print('')
