import re


def decoder(sna: list):
    ret, size = 0, len(sna)
    for i in range(size):
        if sna[i] == '1':
            ret += 1 * pow(5, size-i-1)
        elif sna[i] == '2':
            ret += 2 * pow(5, size-i-1)
        elif sna[i] == '-':
            ret += -1 * pow(5, size-i-1)
        elif sna[i] == '=':
            ret += -2 * pow(5, size-i-1)
    return ret


def encoder(dec: int):
    ret, n = '', dec
    while n > 0:
        m, q = divmod(n, 5)
        if q == 3:
            ret += '='
            n = m + 1
        elif q == 4:
            ret += '-'
            n = m + 1
        else:
            ret += str(q)
            n = m
    return ret[::-1]


Lines = open('Day25.txt').readlines()
SNAFU, int_total = [re.findall(r'\d|-|=', line) for line in Lines], 0
for snaf in SNAFU:
    int_total += decoder(snaf)
print(int_total)
print(encoder(int_total))
