import sys, os

class Directory:
    def __init__(self, my_name):
        self.size = 0
        self.name = my_name
        self.directory = []

    def add_file(self, class_file):
        self.directory.append(class_file)
        self.size += class_file.size

    #def add_child_dir_size(self, class_dir):
    #    self.directory.append(class_dir.directory)

class File:
    def __init__(self, my_name, my_size):
        self.name = my_name
        self.size = int(my_size)

lines = open(sys.argv[1]).readlines()

iamat = []
tracking = []
current_files = []

for line in lines:
    try:
        current_dir = iamat[-1]
    except:
        pass
    characters = line.split()
    if characters[1] == 'cd':

        try:
            for file in current_files:
                for directory in iamat:
                    try:
                        directory.add_file(file)
                    except:
                        pass
            current_files=[]
        except:
            pass

        if characters[2] == '..':
            #iamat[-2].add_child_dir_size(current_dir) 에휴 씼팔앂쌀
            iamat.pop()
        else:
            current_dir=Directory(characters[2])
            iamat.append(current_dir)
            tracking.append(current_dir)

    elif characters[1] == 'ls':
        pass

    elif characters[0] == 'dir':
        pass

    else:
        file = File(characters[1],characters[0])
        current_files.append(file)

tot = 0

answer_1 = 0
for Dir in tracking:
    print(Dir.name, Dir.size)
    if Dir.size <= 100000:
        answer_1 += Dir.size

tot = tracking[0].size

print(f'\nanswer_1={answer_1}')

answer_2 = []
for Dir in tracking:
    if 70000000 - tot + Dir.size >= 30000000:
        answer_2.append(Dir.size)

answer_2.sort()
print(f'answer_2={answer_2[0]}')