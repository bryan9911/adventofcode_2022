import sys, os

signal = open(sys.argv[1]).readline().replace('\n','')

length = int(sys.argv[2]) # 4? 14?

for i in range(0,len(signal)-(length-1)):
    marker = signal[i:i+length]

    if len(marker) == len(set(marker)):
        print(i+length)
        break
