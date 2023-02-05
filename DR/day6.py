from util import read_input
lines = read_input()

def part1_is_signal(str):
    return len(set(str)) == 4

def part2_is_signal(str):
    return len(set(str)) == 14

check = [0, 0]
# Part 1
for i in range(4, len(lines[0])):
    if not check[0] and part1_is_signal(lines[0][i-4:i]):
        print("part1:", i)
        check[0] = 1
    if not check[1] and part2_is_signal(lines[0][i-14:i]):
        print("part2:", i)
        check[1] = 1