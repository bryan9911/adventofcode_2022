

def fill_grid(instruction: list, xlim: list, ylim: list):
    new = [['.' for _ in range(xlim[1]-xlim[0]+3)] for __ in range(ylim[1]+3)]
    mx = xlim[0]-1
    for inst in instruction:
        prev = inst[0]
        for ins in inst:
            new[ins[1]][ins[0]-mx] = '#'
            if ins[0] == prev[0] and ins[1] > prev[1]:
                for n in range(ins[1]-prev[1]):
                    new[prev[1]+n][ins[0]-mx] = '#'
            elif ins[0] == prev[0] and ins[1] < prev[1]:
                for n in range(prev[1]-ins[1]):
                    new[prev[1]-n][ins[0]-mx] = '#'
            elif ins[0] > prev[0] and ins[1] == prev[1]:
                for n in range(ins[0]-prev[0]):
                    new[ins[1]][prev[0]+n-mx] = '#'
            if ins[0] < prev[0] and ins[1] == prev[1]:
                for n in range(prev[0]-ins[0]):
                    new[ins[1]][prev[0]-n-mx] = '#'
            prev = ins
    new[0][500-mx] = '+'
    if xlim[1] > 600:
        for b in range(len(new[0])):
            new[ylim[1]+2][b] = '#'
    return new


def sand(source: list):
    count = 0
    stop = False
    start = source
    while not stop:
        check = check_below(start, count, stop)
        count, stop = check
    return count


def check_below(ori: list, num: int, what):
    down = [ori[0]+1, ori[1]]
    if down[0] < maxy+2:
        if grid[down[0]][down[1]] == '.':
            res = check_below(down, num, what)
        else:
            left = [ori[0]+1, ori[1]-1]
            if grid[left[0]][left[1]] == '.':
                res = check_below(left, num, what)
            else:
                right = [ori[0]+1, ori[1]+1]
                if grid[right[0]][right[1]] == '.':
                    res = check_below(right, num, what)
                else:
                    if grid[ori[0]][ori[1]] == '+':
                        num += 1
                        what = True
                    else:
                        grid[ori[0]][ori[1]] = 'o'
                        num += 1
                    res = [num, what]
    else:
        what = True
        res = [num, what]
    return res


Lines = open('Day14.txt').readlines()
Lines = list(map(lambda s: s.strip(), Lines))
rock = []
maxx, minx, maxy = 0, 1000, 0
for line in Lines:
    temp = line.split(' -> ')
    add = []
    for te in temp:
        x, y = te.split(',')
        if int(x) > maxx:
            maxx = int(x)
        if int(x) < minx:
            minx = int(x)
        if int(y) > maxy:
            maxy = int(y)
        add.append([int(x), int(y)])
    rock.append(add)

grid = fill_grid(rock, [500-(maxy+2), 500+(maxy+2)], [0, maxy])

sand_source = [0, 500-minx+1]
sand_source2 = [0, maxy+3]
sand_count = sand(sand_source2)

for k in range(len(grid)):
    for ll in range(len(grid[k])):
        print(grid[k][ll], end='')
    print('')
print(sand_count)
