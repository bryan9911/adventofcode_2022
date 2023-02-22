import numpy as np
from operator import *
from util import read_input
lines = read_input()

def parse(l):
    k, v = l.split(': ')
    try:
        v = int(v)
    except:
        pass
    return k, v

operator_map = {'+':add, '-':sub, '*':mul, '/':floordiv}
reverse_operator_map = {'+':sub, '-':add, '*':floordiv, '/':mul}
cache = {}
def calc_monkeys(monkeys, name):
    if name in cache:
        return cache[name]
    if type(monkeys[name]) == str:
        lchild, opr, rchild = monkeys[name].split()
        lchild_value, lchild_has_humn = calc_monkeys(monkeys, lchild)
        rchild_value, rchild_has_humn = calc_monkeys(monkeys, rchild)
        has_humn = lchild_has_humn or rchild_has_humn
        cache[name] = (operator_map[opr](lchild_value, rchild_value), has_humn)
    else:
        has_humn = name == 'humn'
        cache[name] = (monkeys[name], has_humn)
        
    return cache[name]

def figure_humn(monkeys):
    lchild, _, rchild = monkeys['root'].split()
    lchild_value, lchild_has_humn = calc_monkeys(monkeys, lchild)
    rchild_value, _ = calc_monkeys(monkeys, rchild)

    if lchild_has_humn:
        return decide_humn_value(monkeys, lchild, rchild_value)
    else:
        return decide_humn_value(monkeys, rchild, lchild_value)

def decide_humn_value(monkeys, name, value):
    if name == 'humn':
        return value
    lchild, opr, rchild = monkeys[name].split()
    lchild_value, lchild_has_humn = calc_monkeys(monkeys, lchild)
    rchild_value, _ = calc_monkeys(monkeys, rchild)

    if lchild_has_humn:
        return decide_humn_value(monkeys, lchild, reverse_operator_map[opr](value, rchild_value))
    else:
        if opr == '-':
            value = -value
        return decide_humn_value(monkeys, rchild, reverse_operator_map[opr](value, lchild_value))

monkeys = {}
for l in lines:
    k, v =  parse(l)
    monkeys[k] = v

print(calc_monkeys(monkeys, 'root')[0])
print(figure_humn(monkeys))