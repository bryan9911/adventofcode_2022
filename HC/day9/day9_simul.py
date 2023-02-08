import sys
import numpy as np

moves = open('test.txt').readlines()
head_loc = np.array([0,0])
tail_loc = np.array([0,0])
tracker = []
max_height, min_height = 0, 0
max_width, min_width = 0, 0

def head_moves(movement):
    direction,repeat = movement
    global head_loc, d
    #d = [up_down,left_right]

    if direction == 'U':
        d = np.array([1,0])

    elif direction == 'D':
        d = np.array([-1,0])

    elif direction == 'L':
        d = np.array([0,-1])

    elif direction == 'R':
        d = np.array([0,1])

    for _ in range(int(repeat)):
        head_loc += d
        tail_moves()
        Marauders_map()
        tracking()

def tail_moves():
    global head_loc, tail_loc, d

    diff_up_down, diff_left_right = head_loc - tail_loc
    move = [0,0]
    if (diff_up_down > 1 and diff_left_right == 1) or (diff_up_down == 1 and diff_left_right > 1):
        move = [1,1]

    elif (diff_up_down < -1 and diff_left_right == -1) or (diff_up_down == -1 and diff_left_right < -1):
        move = [-1,-1]

    elif (diff_up_down > 1 and diff_left_right == -1) or (diff_up_down == 1 and diff_left_right < -1):
        move = [1,-1]

    elif (diff_up_down < -1 and diff_left_right == 1) or (diff_up_down == -1 and diff_left_right > 1):
        move = [-1,1]

    elif diff_up_down > 1:
        move = [1,0]

    elif diff_up_down < -1:
        move = [-1,0]

    elif diff_left_right > 1:
        move = [0,1]

    elif diff_left_right < -1:
        move = [0,-1]

    tail_loc += move

def Marauders_map():
    global head_loc, tail_loc, tracker

    for i in range(5,-1,-1):
        for j in range(6):
            dot = [i,j]
            #print(dot,head_loc,tail_loc)
            if dot == head_loc.tolist():
                print('H',end='')
                pass
            elif dot == tail_loc.tolist():
                print('T',end='')
                tracker.append(str(dot))
            elif dot == [0,0]:
                pass
                print('s',end='')
            else:
                pass
                print('.',end='')
        print()
    print()

def Marauders_map_tracker():
    global head_loc, tail_loc, tracker
    answer_1 = 0
    for i in range(5,-1,-1):
        for j in range(6):
            dot = str([i,j])
            #print(dot,head_loc,tail_loc)
            if dot in tracker:
                answer_1 += 1
                print('#',end='')
            else:
                pass
                print('.',end='')
        print()
    #print(answer_1)

def tracking():
    global head_loc, tail_loc, tracker
    tracker.append(str(tail_loc.tolist()))

def main_test():
    for move in moves:
        print(f'== {move.rstrip()} ==\n')
        head_moves(move.split())

    print('== answer_1 ==')
    Marauders_map_tracker()
    print(len(set(tracker)))

def main_1():
    for move in moves:
        head_moves(move.split())

    print('answer_1: ',len(set(tracker)))

main_test()
