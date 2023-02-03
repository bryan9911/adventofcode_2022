import sys, re

stack_0 = ['D','T','W','N','L']
stack_1 = ['H','P','C']
stack_2 = ['J','M','G','D','N','H','P','W']
stack_3 = ['L','Q','T','N','S','W','LC']
stack_4 = ['N','C','H','P']
stack_5 = ['B','Q','W','M','D','N','H','T']
stack_6 = ['L','S','G','J','R','B','M']
stack_7 = ['T','R','B','V','G','W','N','Z']
stack_8 = ['L','P','N','D','G','W']

stacks = [stack_0,
          stack_1,
          stack_2,
          stack_3,
          stack_4,
          stack_5,
          stack_6,
          stack_7,
          stack_8]

moves = open('day5.txt').readlines()

def part_1():
    for move in moves:
        crate, stack_from, stack_to = re.findall(r'\d+', move)
        crate, stack_from, stack_to = int(crate), int(stack_from)-1, int(stack_to)-1

        stack_from = stacks[stack_from]
        stack_to = stacks[stack_to]

        for _ in range(crate):
            move_me = stack_from.pop(0)
            stack_to.insert(0, move_me)

    for stack in stacks:
        print(stack[0],end='')

def part2():
    for move in moves:
        crate, stack_from, stack_to = re.findall(r'\d+', move)
        crate, stack_from, stack_to = int(crate), int(stack_from)-1, int(stack_to)-1

        stack_from = stacks[stack_from]
        stack_to = stacks[stack_to]

        move_me = stack_from[:crate]

        for _ in range(crate):
            stack_from.pop(0)

        stack_to[0:0] = move_me

    for stack in stacks:
        print(stack[0],end='')

part2()