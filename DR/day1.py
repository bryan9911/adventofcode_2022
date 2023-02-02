from util import read_input
lines = read_input()

calories = []
sum_c = 0
for l in lines:
    l = l.strip()
    if l:
        sum_c += int(l)
    else:
        calories.append(sum_c)
        sum_c = 0

calories.sort(reverse=True)
print(calories[0], sum(calories[:3]))