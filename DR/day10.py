from util import read_input
lines = read_input()

signal_turns = list(range(20,230, 40))
cur_turn = 1
X = 1
part1 = 0

def render_CRT():
    print('#' if X-1 <= (cur_turn-1)%40 <= X+1 else '.', end='')
    if cur_turn % 40 == 0:
        print('')

for l in lines:
    if signal_turns and signal_turns[0] - 1 <= cur_turn <= signal_turns[0]:
        part1 += signal_turns[0] * X
        signal_turns.pop(0)
    if l.startswith("noop"):
        render_CRT()
        cur_turn += 1
        continue

    render_CRT()
    cur_turn += 1
    render_CRT()
    cur_turn += 1
    X += int(l.split()[-1])

print(part1)