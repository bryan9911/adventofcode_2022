import pandas as pd
import numpy as np

df = pd.read_csv('Day2.txt')
df['Opponent'] = df.Text.str.split(' ').str[0]
df['Result'] = df.Text.str.split(' ').str[1]

score1 = np.zeros(len(df['Text']))
s1 = 0
for i in df['Text']:
    if i == 'A Y' or i == 'B X' or i == 'C Z':
        score1[s1] = 1
    elif i == 'A Z' or i == 'B Y' or i == 'C X':
        score1[s1] = 2
    else:
        score1[s1] = 3
    s1 += 1

score2 = np.zeros(len(df['Result']))
s2 = 0
for j in df['Result']:
    if j == 'Z':
        score2[s2] = 6
    elif j == 'Y':
        score2[s2] = 3
    else:
        continue
    s2 += 1

print(np.sum(score1)+np.sum(score2))
'''
a= rock
b= paper
c = scissor

x= lose
y= draw
z= win
