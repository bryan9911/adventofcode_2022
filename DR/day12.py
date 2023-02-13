from util import read_input
height_map = read_input()

def find_S():
    for i, l in enumerate(height_map):
        if 'S' in l:
            return i, l.find('S')
    return None, None

def height_difference(x1, y1, x2, y2):
    height_remap = {'S': 'a', 'E': 'z'}
    h1 = height_remap[height_map[x1][y1]] if height_map[x1][y1] in height_remap else height_map[x1][y1]
    h2 = height_remap[height_map[x2][y2]] if height_map[x2][y2] in height_remap else height_map[x2][y2]
    return ord(h2) - ord(h1)

def is_valid_coord(x, y):
    return 0 <= x < len(height_map) and 0 <= y < len(height_map[0])

def find_minimum_steps(points):
    q = [(x, y, 0) for x, y in points]
    visit.add((x, y) for x, y in points)
    dirs = [[0,1], [1,0], [0,-1], [-1,0]]
    while q:
        cur_x, cur_y, cur_step = q.pop(0)
        if height_map[cur_x][cur_y] == 'E':
            return cur_step
        for d in dirs:
            if not is_valid_coord(cur_x+d[0], cur_y+d[1]):
                continue
            if (cur_x+d[0], cur_y+d[1]) not in visit and height_difference(cur_x, cur_y, cur_x+d[0], cur_y+d[1]) < 2:
                visit.add((cur_x+d[0], cur_y+d[1]))
                q.append((cur_x+d[0], cur_y+d[1], cur_step + 1))

# Part 1
visit = set()
print(find_minimum_steps([find_S()]))

# Part 2
visit = set()
print(find_minimum_steps([(x, y) for x in range(len(height_map)) for y in range(len(height_map[x])) if height_map[x][y] == 'a'] + [find_S()]))