import sys
import numpy as np

moves = open(sys.argv[1]).readlines()
tot_len = int(sys.argv[2])
tails = [np.array([0,0]) for _ in range(tot_len)]
tracker, tracker_last = [], []

def head_moves(direction,repeat,head,tail,i):
    global d, tot_len, tracker, tracker_last
    #d = [up_down,left_right]

    head_loc = head
    tail_loc = tail

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
        tail_loc = tail_moves(head_loc,tail_loc)

        tracking(tail_loc,tracker)
        
        # if the last tail moved
        if i == tot_len-1 :
            tracking(tail_loc,tracker_last)

def tracking(tail,trackerr):
    tail_loc = tail
    trackerr.append(str(tail_loc.tolist()))

def tail_moves(head,tail):

    head_loc = head
    tail_loc = tail

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

    return tail_loc

for move in moves:
    for i in range(1,tot_len):

        head = tails[i-1]
        tail = tails[i]
        direction,repeat = move.split()

        head_moves(direction,repeat,head,tail,i)

print(len(set(tracker)))
print(len(set(tracker_last)))