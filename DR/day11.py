from functools import reduce
from math import lcm
from copy import deepcopy
from util import read_input
lines = read_input()

monkeys = []

def parse_args(input_lines):
    items = list(map(int, input_lines[1][18:].split(", ")))

    operation_type, operation_value = input_lines[2][23:].split()
    if operation_value == "old":
        operation = lambda x: x * x
    elif operation_type == "+":
        operation = lambda x: x + int(operation_value)
    else:
        operation = lambda x: x * int(operation_value)

    test_value = int(input_lines[3].split()[-1])
    test = lambda x: (x % test_value) == 0

    throw_on_true = int(input_lines[4].split()[-1])
    throw_on_false = int(input_lines[5].split()[-1])

    return items, operation, test, test_value, throw_on_true, throw_on_false

class Monkey:
    def __init__(self, items, operation, test, test_value, throw_on_true, throw_on_false):
        self.items = items
        self.operation = operation
        self.test = test
        self.test_value = test_value
        self.throw_on_true = throw_on_true
        self.throw_on_false = throw_on_false
        self.inspect_cnt = 0

    def add_item(self, value):
        self.items.append(value)

    def throw(self, target, value):
        monkeys[target].add_item(value)

    def inspect(self, part):
        for i in self.items:
            worry_level = self.operation(i)
            if part == 1:
                worry_level //= 3
            # Modular by lcm of all test_values for value management
            worry_level %= item_mod
            self.throw(self.throw_on_true if self.test(worry_level) else self.throw_on_false, worry_level)

        self.inspect_cnt += len(self.items)
        self.items = []

for i in range(0, len(lines), 7):
    monkeys.append(Monkey(*parse_args(lines[i:i+7])))

# Copy for Part 2
monkeys_raw = deepcopy(monkeys)
item_mod = reduce(lcm, [m.test_value for m in monkeys])

# Part 1
for _ in range(20):
    for m in monkeys:
        m.inspect(1)

sorted_inspect_cnts = sorted([m.inspect_cnt for m in monkeys], reverse=True)
print(sorted_inspect_cnts[0] * sorted_inspect_cnts[1])

# Part 2
monkeys = monkeys_raw
for _ in range(10000):
    for m in monkeys:
        m.inspect(2)

sorted_inspect_cnts = sorted([m.inspect_cnt for m in monkeys], reverse=True)
print(sorted_inspect_cnts[0] * sorted_inspect_cnts[1])