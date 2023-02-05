import sys, os
from collections import Counter

signal = open(sys.argv[1]).readline().replace('\n','')

length = int(sys.argv[2]) # 4? 14?

def is_duplicate(a):

    if len(a) == len(set(a)):
        return 1
    else:
        return 0

for i in range(0,len(signal)-(length-1)):
    marker = signal[i:i+length]

    if is_duplicate(marker):
        print(i+length)
        break
