import pandas as pd

Stack = [['W', 'D', 'G', 'B', 'H', 'R', 'V'],
         ['J', 'N', 'G', 'C', 'R', 'F'],
         ['L', 'S', 'F', 'H', 'D', 'N', 'J'],
         ['J', 'D', 'S', 'V'],
         ['S', 'H', 'D', 'R', 'G', 'W', 'N', 'V'],
         ['P', 'G', 'H', 'C', 'M'],
         ['F', 'J', 'B', 'G', 'L', 'Z', 'H', 'C'],
         ['S', 'J', 'R'],
         ['L', 'G', 'S', 'R', 'B', 'N', 'V', 'M']]

Data = pd.read_csv('Day5_2.txt', dtype=str)
df = Data['Moves'].str[5:]
df1 = df.str.split(' from ').str[0]
temp = df.str.split(' from ').str[1]
df2 = temp.str.split(' to ').str[0]
df3 = temp.str.split(' to ').str[1]

move = df1.astype('int64')
st_origin = df2.astype('int64')
st_destin = df3.astype('int64')


def move1():
    for i in range(0, len(move)):
        n = move[i]
        ori = Stack[st_origin[i] - 1]
        des = Stack[st_destin[i] - 1]
        for _ in range(n):
            crate = ori.pop(-1)
            des.append(crate)

    for k in Stack:
        print(k[-1])


def move2():
    for i in range(0, len(move)):
        n = move[i]
        ori = Stack[st_origin[i] - 1]
        des = Stack[st_destin[i] - 1]
        crate = ori[-n:]
        des.extend(crate)
        del ori[-n:]

    for k in Stack:
        print(k[-1])


move2()
