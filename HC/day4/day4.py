import sys

read = open(sys.argv[-1]).readlines()
count = 0

count_2 = 0

for line in read:

    line = line.replace('\n','')
    first_pair, second_pair = line.split(',')

    section_1, section_2 = first_pair.split('-')
    section_3, section_4 = second_pair.split('-')

    #이걸 안하면 2번에서 에러남; 왜?
    section_1, section_2, section_3, section_4 = int(section_1), int(section_2), int(section_3), int(section_4)

    if (section_1 == section_3) or (section_2 == section_4):
        count+=1
    
    elif section_1 > section_3:
        if section_2 < section_4:
            count+=1

    elif section_1 < section_3:
        if section_2 > section_4:
            count+=1

    if section_1 in range(section_3,section_4+1) or section_2 in range(section_3,section_4+1) or section_3 in range(section_1,section_2+1) or section_4 in range(section_1,section_2+1):
        count_2+=1

print(count)
print(count_2)
