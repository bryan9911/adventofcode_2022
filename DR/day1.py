import sys
with open(f'{sys.argv[0].split(".")[0]}.input') as f:
    lines = f.readlines()

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