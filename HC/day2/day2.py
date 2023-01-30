import os, sys

def part_1():
    translate = {'A':'rock','X':'rock',
                 'B':'paper','Y':'paper',
                 'C':'scissors','Z':'scissors'}

    score_0 = {'rock':1,'paper':2,'scissors':3}
    score_2 = {'win':6,'draw':3,'lose':0}

    games = open('day2.txt').readlines()

    def do_game(aa,bb):
        
        aa = translate[aa]
        bb = translate[bb]

        result = (score_0[aa]-score_0[bb])
        if result == 0:
            return 'draw', score_2['draw']+score_0[bb]

        elif result == 1 or result == -2:
            return 'lose', score_2['lose']+score_0[bb]

        elif result == -1 or result == 2:
            return 'win', score_2['win']+score_0[bb]

    result = 0

    for game in games:
        aa, bb = game.replace('\n','').split()
        print(translate[aa],translate[bb],do_game(aa,bb))
        result += do_game(aa,bb)[1]

    print(result)

def part_2():
    translate = {'A':'rock','X':'lose',
                 'B':'paper','Y':'draw',
                 'C':'scissors','Z':'win'}

    score_0 = {'rock':1,'paper':2,'scissors':3}
    score_2 = {'win':6,'draw':3,'lose':0}

    games = open('day2.txt').readlines()

    def guess(aa,bb):

        aa = translate[aa]
        bb = translate[bb]

        if bb == 'draw':

            guess = aa

        elif bb == 'win':

            if aa == 'rock':

                guess = 'paper'

            elif aa == 'paper':

                guess = 'scissors'

            else:
                guess = 'rock'

        else:

            if aa == 'rock':

                guess = 'scissors'

            elif aa == 'paper':

                guess = 'rock'

            else:
                guess = 'paper'

        return score_0[guess]+score_2[bb]
    
    result=0

    for game in games:
        aa, bb = game.replace('\n','').split()
        result += guess(aa,bb)

    print(result)
if __name__ == '__main__':
    part_2()