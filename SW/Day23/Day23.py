import re
from collections import deque, Counter


def direction(elf: tuple, direc: str):
    dirs = {'N': [(-1, 0), (-1, 1), (-1, -1)], 'S': [(1, 0), (1, 1), (1, -1)],
            'W': [(0, -1), (-1, -1), (1, -1)], 'E': [(0, 1), (-1, 1), (1, 1)]}
    return [(elf[0]+check[0], elf[1]+check[1]) for check in dirs[direc]]


def all_dir(elf: tuple):
    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
    return [(elf[0]+di[0], elf[1]+di[1]) for di in dirs]


def move_elves(elves: list):
    dir_order, rounds, all_move = deque(['N', 'S', 'W', 'E']), 0, False
    while all_move is False:
        all_move = True
        next_move, elf_set = [None]*len(elves), set(elves)
        for i, elf in enumerate(elves):
            if all(al not in elf_set for al in all_dir(elf)):
                continue
            else:
                all_move = False
                for dirs in dir_order:
                    looks = direction(elf, dirs)
                    if all(look not in elf_set for look in looks):
                        next_move[i] = (looks[0][0], looks[0][1])
                        break
        count = Counter(next_move)
        for i, new_elf in enumerate(next_move):
            if count[new_elf] == 1:
                elves[i] = new_elf
        dir_order.rotate(-1)
        rounds += 1
        if rounds == 10:
            x_elf, y_elf = [p[0] for p in elves], [p[1] for p in elves]
            print((max(x_elf) - min(x_elf) + 1) * (max(y_elf) - min(y_elf) + 1) - len(elves))
    return rounds


Lines = open('Day23.txt').readlines()
grid = [re.findall(r'[.#]', line) for line in Lines]
Elves = [(i, j) for i in range(len(grid)) for j in range(len(grid[0])) if grid[i][j] == '#']
print(move_elves(Elves))
