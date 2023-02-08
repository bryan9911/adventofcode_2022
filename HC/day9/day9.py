import sys
import numpy as np

moves = open(sys.argv[1]).readlines()
tot_len = int(sys.argv[2])
tails = [np.array([0,0]) for _ in range(tot_len)]
tracker, tracker_last = [], []

def head_moves(direction,repeat,head,tail,i):
    global tot_len, tracker, tracker_last
    #d = [up_down,left_right]

    if direction == 'U':
        d = np.array([1,0])

    elif direction == 'D':
        d = np.array([-1,0])

    elif direction == 'L':
        d = np.array([0,-1])

    elif direction == 'R':
        d = np.array([0,1])

    
    # move only the first
    if i == 1:
        head += d

    tail = tail_moves(head,tail)

    tracking(tail,tracker)
    
    # if the last tail moved
    if i == tot_len-1 :
        tracking(tail,tracker_last)

    return head, tail

def tracking(tail,trackerr):
    tail_loc = tail
    trackerr.append(str(tail_loc.tolist()))

def tail_moves(head,tail):

    #diff_up_down, diff_left_right = head_loc - tail_loc
    dh, dw = head - tail

    if abs(dh) <= 1 and abs(dw) <= 1:
        move = [0,0]

    elif dh + dw >= 3:
        move = [1,1]

    elif dh + dw <= -3:
        move = [-1,-1]

    elif dh >= 2 and dw == 0:
        move = [1,0]

    elif dh <= -2 and dw == 0:
        move = [-1,0]

    elif dh == 0 and dw >= 2:
        move = [0,1]

    elif dh == 0 and dw <= -2:
        move = [0,-1]

    elif dh > 0:
        move = [1,-1]

    elif dh < 0:
        move = [-1,1]

    tail += np.array(move)

    return tail

for move in moves:
    direction,repeat = move.split()
    for _ in range(int(repeat)):
        for i in range(1,tot_len):

            tails[i-1], tails[i] = head_moves(direction,repeat,tails[i-1],tails[i],i)

print(len(set(tracker)))
print(len(set(tracker_last)))