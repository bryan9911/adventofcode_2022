import sys

forest = []

trees = open(sys.argv[1]).readlines()

for Tree in trees:
    grid = []
    Tree=Tree.rstrip()
    for tree in Tree:
        grid.append(tree)

    forest.append(grid)

answer_1 = 0
# 세로 x 가로 = i x j
for i in range(len(forest)):
    for j in range(len(forest[i])):

        left = range(0,j)
        right = range(j+1,len(forest))
        up = range(0,i)
        down = range(i+1,len(forest))

        if (i==0 or i==len(forest)-1 or j==0 or j==len(forest)-1):
            answer_1 += 1
            #print('type 1:',i,j)
        else:
            still_look = False
            for ii in up:
                if forest[ii][j] >= forest[i][j]:
                    still_look = True
                    break

            if still_look:
                for ii in down:
                    if forest[ii][j] >= forest[i][j]:
                        still_look = True
                        break
                    else:
                        still_look = False

            if still_look:
                for jj in left:
                    if forest[i][jj] >= forest[i][j]:
                        still_look = True
                        break
                    else:
                        still_look = False

            if still_look:
                for jj in right:
                    if forest[i][jj] >= forest[i][j]:
                        still_look = True
                        break
                    else:
                        still_look = False      

            if not still_look:
                answer_1 += 1

print(answer_1)

answer_2s=[]

for i in range(len(forest)):
    for j in range(len(forest[i])):
        l, r, u, d = 1,1,1,1

        left = range(j-1,-1,-1)
        right = range(j+1,len(forest))
        up = range(i-1,-1,-1)
        down = range(i+1,len(forest))

        if False:
            print('oh sex!')
        else:
            for ii in up:
                if forest[ii][j] >= forest[i][j]:
                    u=i-ii
                    break
                else:
                    u=i

            for ii in down:
                if forest[ii][j] >= forest[i][j]:
                    d=ii-i
                    break
                else:
                    d=len(forest)-i-1

            for jj in left:
                if forest[i][jj] >= forest[i][j]:
                    l=j-jj
                    break
                else:
                    l=j

            for jj in right:
                if forest[i][jj] >= forest[i][j]:
                    r=jj-j
                    break
                else:
                    r=len(forest)-j-1

        #if l==0:
        #    l=1
        #if r==0:
        #    r=1
        #if u==0:
        #    u=1
        #if d==0:
        #    d=1
        answer_2s.append(l*r*u*d)

answer_2s.sort()

print(answer_2s[-1])