import re
import sympy as sy


def find_value(monkey: dict, size: dict, operation: dict, cur: str):
    if size[cur] is None:
        child = monkey[cur]
        return monkey_calculate(find_value(monkey, size, operation, child[0]), operation[cur],
                                find_value(monkey, size, operation, child[1]))
    else:
        return size[cur]


def monkey_calculate(child1, ops: str, child2):
    ret = 0
    if ops == '+':
        ret = child1 + child2
    elif ops == '-':
        ret = child1 - child2
    elif ops == '*':
        ret = child1 * child2
    elif ops == '/':
        ret = child1 / child2
    elif ops == '=':
        ret = sy.Eq(child1, child2)
    return ret


Lines = open('Day21.txt').readlines()
Lines = [line.replace(':', '') for line in Lines]

monkeys, value, ops = {}, {}, {}
for line in Lines:
    temp = line.split()
    if bool(re.search(r'\d+', line)):
        monkeys[temp[0]], value[temp[0]], ops[temp[0]] = None, int(temp[1]), None
    else:
        monkeys[temp[0]], value[temp[0]], ops[temp[0]] = [temp[1], temp[3]], None, temp[2]
print(find_value(monkeys, value, ops, 'root'))  # part1
ops['root'], value['humn'] = '=', sy.symbols('X')  # part2
eq = find_value(monkeys, value, ops, 'root')
print(sy.solve(eq))

# Another solution for part2: iteration
ops['root'], me, new_me = '-', value['humn'], 3429411055000
error = abs(find_value(monkeys, value, ops, 'root'))
value['humn'] = new_me
new_error = abs(find_value(monkeys, value, ops, 'root'))
while new_error > 1:
    try:
        delta = round((new_me - me) / (new_error - error))
    except ZeroDivisionError:
        delta = -1 if new_error > error else 1
    value['humn'] = new_me + delta
    me = new_me
    error = new_error
    new_me += delta
    new_error = abs(find_value(monkeys, value, ops, 'root'))
print(value['humn'])

