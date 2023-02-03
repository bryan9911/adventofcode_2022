import sys, re

stack_0 = ['N','Z']
stack_1 = ['D','C','M']
stack_2 = ['P']

stacks = [stack_0,
          stack_1,
          stack_2]

moves = open('test.txt').readlines()
'''
for move in moves:
    crate, stack_from, stack_to = re.findall(r'\d+', move)
    crate, stack_from, stack_to = int(crate), int(stack_from)-1, int(stack_to)-1

    stack_from = stacks[stack_from]
    stack_to = stacks[stack_to]

    for _ in range(crate):
        move_me = stack_from.pop(0)
        stack_to.insert(0, move_me)

        print(stack_0,stack_1,stack_2)

for stack in stacks:
    print(stack[0],end='')

'''
for move in moves:
    crate, stack_from, stack_to = re.findall(r'\d+', move)
    crate, stack_from, stack_to = int(crate), int(stack_from)-1, int(stack_to)-1

    stack_from = stacks[stack_from]
    stack_to = stacks[stack_to]

    move_me = stack_from[:crate]

    for _ in range(crate):
        stack_from.pop(0)

    stack_to[0:0] = move_me

    print(stacks)

for stack in stacks:
    print(stack[0],end='')