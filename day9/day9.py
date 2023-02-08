import sys

instructions = open(sys.argv[1]).readlines()
cycles = 0
signal_sum = 0
register_X = 1
draw = []

def update_then_check_cycles():
    global signal_sum, cycles, register_X
    cycles += 1
    #print('cycles: ',cycles)
    #print('register_X: ',register_X)
    #ask 동렬쿤: global 쓰는게 더 멋있나?

    check_values_if = [20,60,100,140,180,220]

    for value in check_values_if:
        if cycles == value:
            signal_strength = register_X * value
            signal_sum += signal_strength

def update_sprite_then_draw():
    global sprite, cycles, register_X, draw
    
    draw_at = (cycles-1) % 40

    sprite = [register_X-1,register_X,register_X+1]

    if draw_at in sprite:
        draw.append('#')
    else:
        draw.append('.')


for instruction in instructions:
    instruction = instruction.split()

    if instruction[0] == 'noop':
        update_then_check_cycles()
        update_sprite_then_draw()

    elif instruction[0] == 'addx':
        #phase 1
        update_then_check_cycles()
        update_sprite_then_draw()

        #phase 2
        update_then_check_cycles()
        update_sprite_then_draw()
        register_X += int(instruction[1])



print(signal_sum)

for i in range(len(draw)):
    if i % 40 == 0:
        print()
    print(draw[i],end='')