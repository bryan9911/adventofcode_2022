from collections import Counter

data = open('Day6.txt').readlines()
Signal = data[0]
Sig_set = [None]*(len(Signal)-3)
for i in range(0, len(Sig_set)):
    Sig_set[i] = Signal[i:i+4]
    temp = Counter(Sig_set[i])
    temp2 = 0
    for char, count in temp.items():
        if count > 1:
            temp2 = 1
    if temp2 == 0:
        print(i+4)
