import os, sys

calories = open('day1.txt').readlines()
elves, tmp = [], 0

for calory in calories:
    try:
        tmp += int(calory.replace('\n',''))

    except:
        elves.append(int(tmp))
        tmp = 0

elves.sort(reverse=True)

print(elves)

print(f'min calory = {min(elves)}')
print(f'max calory = {max(elves)}')

tmp = 0
for i in range(3):
    tmp += elves[i]

print(f'top three = {tmp}')