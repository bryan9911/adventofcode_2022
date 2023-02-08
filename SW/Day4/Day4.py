import pandas as pd
import numpy as np

Data = pd.read_csv('Day4.txt', sep=',')
df = pd.DataFrame()

df['Pair1 start'] = Data.Pair1.str.split('-').str[0]
df['Pair1 end'] = Data.Pair1.str.split('-').str[1]
df['Pair2 start'] = Data.Pair2.str.split('-').str[0]
df['Pair2 end'] = Data.Pair2.str.split('-').str[1]
df = df.to_numpy(dtype=int)

count = np.zeros(len(df))
for n in range(0, len(df), 1):
    if df[n, 1] < df[n, 2]:
        count[n] = 1
    elif df[n, 3] < df[n, 0]:
        count[n] = 1

print(len(df)-np.sum(count))
