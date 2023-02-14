from itertools import zip_longest as zl


def compare(a, b):
    comp = zl(a, b, fillvalue=None)
    status = 'q'
    for co in comp:
        left, right = co
        if type(left) == list and type(right) == list:
            status = compare(left, right)
        elif type(left) == int and type(right) == int:
            if a < b:
                status = 'r'
            elif a > b:
                status = 'n'
        elif left is None:
            status = 'r'
        elif right is None:
            status = 'n'
        elif type(left) == int and type(right) == list:
            status = compare(make_list(left), right)
        elif type(left) == list and type(right) == int:
            status = compare(left, make_list(right))
        if status != 'q':
            return status


def make_list(ma):
    if type(ma) == int:
        return [ma]


def find_2and6(inspect: list):
    ind_2, ind_6 = 1, 2
    two, six = [[2]], [[6]]
    for item in inspect:
        det2 = compare(item, two)
        det6 = compare(item, six)
        if det2 == 'r':
            ind_2 += 1
        if det6 == 'r':
            ind_6 += 1
    return [ind_2, ind_6]


Lines = open('Day13.txt').readlines()
Lines = list(map(lambda s: s.strip(), Lines))
Packet = []
for ii in range(len(Lines)):
    if (ii % 3) == 0:
        l1 = eval(Lines[ii])
    elif (ii % 3) == 1:
        l2 = eval(Lines[ii])
        Packet.append([l1, l2, 'q'])

tot1 = 0
initial = []
for p in range(len(Packet)):
    Packet[p][2] = compare(Packet[p][0], Packet[p][1])
    initial.extend([Packet[p][0], Packet[p][1]])
    if Packet[p][2] == 'r':
        tot1 += (p+1)
print(tot1)
res = find_2and6(initial)
print(res[0]*res[1])
