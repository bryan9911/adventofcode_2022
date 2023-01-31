import sys
with open(f'{sys.argv[0].split(".")[0]}.input') as f:
    lines = f.readlines()

def chr2int(chr):
    chr = ord(chr)
    if ord('A') <= chr <= ord('C'):
        return chr - ord('A') + 1
    return chr - ord('X') + 1

def outcome(p1, p2):
    a = chr2int(p1)
    b = chr2int(p2)

    if a == b: return 3
    if (a==3 and b==1) or a+1==b: return 6
    return 0

def chr2outcome(chr):
    return (ord(chr) - ord('X')) * 3

def myplay(x, y):
    outcome = chr2outcome(y)
    if outcome == 3: return chr2int(x)
    if outcome == 6: return (chr2int(x) % 3 + 1)
    return (chr2int(x) - 1) if (chr2int(x) - 1) else 3

res1 = 0
res2 = 0
for l in lines:
    x, y = l.strip().split()

    res1 += outcome(x, y) + chr2int(y)
    res2 += chr2outcome(y) + myplay(x, y)

print(res1, res2)