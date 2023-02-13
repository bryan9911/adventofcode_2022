import sys
import numpy as np

fucking_monkeys = open(sys.argv[1]).readlines()


def generate_very_first_starting_items_lists(fucking_monkeys, starting_items, LCMs):

    for line in range(0,len(fucking_monkeys),7):
        num = int(fucking_monkeys[line].replace(':','').split()[-1])
        starting_items[num] = fucking_monkeys[line+1].replace('Starting items: ','').strip().split(', ')
        test_val = int(fucking_monkeys[line+3].split()[-1])
        LCMs.append(test_val)

    lcm = np.lcm.reduce(LCMs)

    return fucking_monkeys, starting_items, lcm

class Monkeys():

    def __init__(self, num:int, operation:list, test_val:int, true:int, false:int):

        self.num = num
        self.operation = operation
        self.test_val = test_val
        self.throw_true = true
        self.throw_false = false

    def operate_test_throw(self, item, starting_items, lcm):

        def operate(item, lcm):

            if self.operation[1] != 'old':
                if self.operation[0] == '*':
                    item *= int(self.operation[1])
                else:
                    item += int(self.operation[1])
            else: #ㅎㅎ 귀차낭
                item *= item

            #item = int(item/3) # 3 for part1, Nan for part2

            return item % lcm

        def pass_test(item):

            return item % self.test_val == 0

        def throw(throw_to, item, starting_items): #조심

            throw_to_items = starting_items[throw_to]
            throw_to_items.extend([item])

            return starting_items

        item = operate(item, lcm)

        if pass_test(item):
            starting_items = throw(self.throw_true,item,starting_items)
        else:
            starting_items = throw(self.throw_false,item,starting_items)

    def update_activity(self, monkey_activities):

        monkey_activities[self.num]+=1

        return monkey_activities

starting_items = [list() for _ in range((len(fucking_monkeys)+1)//7)]
monkey_activities = [0 for _ in range((len(fucking_monkeys)+1)//7)]
monkeys = []
LCMs = []

fucking_monkeys, starting_items, lcm = generate_very_first_starting_items_lists(fucking_monkeys, starting_items, LCMs)

print('very start at:',starting_items)

def define_monkeys():

    global fucking_monkeys, starting_items, monkeys

    for line in range(0,len(fucking_monkeys),7):
        num = int(fucking_monkeys[line].replace(':','').split()[-1])
        items = starting_items[num]
        operation = fucking_monkeys[line+2].replace('Operation: new = old','').split()
        test_val = int(fucking_monkeys[line+3].split()[-1])
        true = int(fucking_monkeys[line+4].split()[-1])
        false = int(fucking_monkeys[line+5].split()[-1])

        cur_monkey = Monkeys(num, operation, test_val, true, false)
        monkeys.append(cur_monkey)

def run_monkeys():

    global monkey_activities, starting_items, monkeys
    for i, monkey in enumerate(monkeys):
        items = starting_items[i]
        for item in items:
            monkey.operate_test_throw(int(item), starting_items, lcm)
            monkey_activities = monkey.update_activity(monkey_activities)
        starting_items[i] = [] #조심

define_monkeys()

for _ in range(10000):
    run_monkeys()
    
monkey_activities.sort()
print(monkey_activities[-1]*monkey_activities[-2])