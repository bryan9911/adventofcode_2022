import re


def cube_turning(maps: list):
    f_len = 50
    x_len, y_len = int(len(maps) / f_len), int(len(maps[0]) / f_len)
    blocks = [(i, j) for i in range(x_len) for j in range(y_len) if maps[i*f_len][j*f_len] != ' ']
    block_id = {block: ind+1 for ind, block in enumerate(blocks)}
    rotation = {(1, 2): (4, 0), (1, 3): (6, 0), (2, 0): (5, 2), (2, 1): (3, 2), (2, 3): (6, 3),
                (3, 0): (2, 3), (3, 2): (4, 1), (4, 2): (1, 0), (4, 3): (3, 0), (5, 0): (2, 2),
                (5, 1): (6, 2), (6, 0): (5, 3), (6, 1): (2, 1), (6, 2): (1, 1)}
    inv_block_id = {v: k for k, v in block_id.items()}
    return block_id, inv_block_id, rotation, f_len


def navigation(maps: list, directions: list, part: int):
    if part == 2:
        block_id, inv_id, rot, f_len = cube_turning(maps)
    num_row, num_col, d_type = len(maps), len(maps[0]), [[0, 1], [1, 0], [0, -1], [-1, 0]]
    cur, facing = [0, maps[0].index('.')], 0
    for direc in directions:
        if direc == 'R':
            facing = (facing + 1) % 4
        elif direc == 'L':
            facing = (facing - 1) % 4
        else:
            for _ in range(int(direc)):
                temp = [(cur[0] + d_type[facing][0]) % num_row, (cur[1] + d_type[facing][1]) % num_col]
                if maps[temp[0]][temp[1]] == '.':
                    cur = temp
                elif maps[temp[0]][temp[1]] == '#':
                    break
                else:
                    if part == 1:
                        while maps[temp[0]][temp[1]] == ' ':
                            temp = [(temp[0] + d_type[facing][0]) % num_row, (temp[1] + d_type[facing][1]) % num_col]
                        if maps[temp[0]][temp[1]] == '.':
                            cur = temp
                        elif maps[temp[0]][temp[1]] == '#':
                            break
                    elif part == 2:
                        rel_cur, cur_block_id = (cur[0] % f_len, cur[1] % f_len), (cur[0] // f_len, cur[1] // f_len)
                        (new_block_id, new_facing) = rot[block_id[cur_block_id], facing]
                        new_block = inv_id[new_block_id]
                        rel_new = ((f_len - rel_cur[0] - 1, rel_cur[1]) if abs(new_facing-facing) % 2 == 0
                                   else (rel_cur[1], rel_cur[0]))
                        temp2 = [rel_new[0]+new_block[0]*f_len, rel_new[1]+new_block[1]*f_len]
                        if maps[temp2[0]][temp2[1]] == '.':
                            cur, facing = temp2, new_facing
                        elif maps[temp2[0]][temp2[1]] == '#':
                            break
    return (cur[0] + 1) * 1000 + (cur[1] + 1) * 4 + facing


Lines = open('Day22.txt').readlines()
last_line = Lines.pop(-1)
del Lines[-1]
board = [re.findall(r'[ .#]', line) for line in Lines]
max_len = max(len(boa) for boa in board)
for boa in board:
    boa.extend(' '*(max_len-len(boa)))
direction = re.findall(r'\d+|\w', last_line)

print(navigation(board, direction, 1))
print(navigation(board, direction, 2))
