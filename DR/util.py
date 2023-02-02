import sys

def read_input():
    with open(f'{sys.argv[0].split(".")[0]}.input') as f:
        lines = f.readlines()
        for i in range(len(lines)):
            lines[i] = lines[i].strip()

    return lines