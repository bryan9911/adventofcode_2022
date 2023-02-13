from util import read_input
lines = read_input()

signal_cycle = list(range(20,230, 40))
cur_cycle = 1
X = 1
part1 = 0

def run_cycle():
    render_CRT()
    cur_cycle += 1

def render_CRT():
    print('#' if X-1 <= (cur_cycle-1)%40 <= X+1 else '.', end='')
    if cur_cycle % 40 == 0:
        print('')

for l in lines:
    if signal_cycle and signal_cycle[0] - 1 <= cur_cycle <= signal_cycle[0]:
        part1 += signal_cycle[0] * X
        signal_cycle.pop(0)
    if l.startswith("noop"):
        run_cycle()
        continue

    run_cycle()
    run_cycle()
    X += int(l.split()[-1])

print(part1)