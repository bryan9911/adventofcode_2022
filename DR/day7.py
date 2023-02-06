from __future__ import annotations
import bisect
from util import read_input
lines = read_input()

# Covers files/directories
class Node:
    def __init__(self, type:str, name:str, size:int, parent:Node):
        self.type = type
        self.name = name
        self.size = size
        self.child = []
        self.parent = parent

    def add_child(self, child:Node):
        self.child.append(child)
    
    def get_child(self, name:str):
        for c in self.child:
            if c.type == 'dir' and c.name == name:
                return c
        return None

part1 = 0
part2_candidates = []
def sum_subdir_fsize(node:Node):
    # Returns the size of node
    global part1, part2_candidates
    if node.type == 'file':
        return node.size

    ret = sum(sum_subdir_fsize(c) for c in node.child)
    part2_candidates.append(ret)
    if ret <= 100000:
        part1 += ret
    return ret

# Create Filesystem from input
root = Node('dir', '/', 0, None)
cur = root
for l in lines[1:]:
    if l.startswith('$'):
        if 'cd' in l:
            parsed = l.split()
            if parsed[-1] == '..':
                cur = cur.parent
            else:
                cur = cur.get_child(parsed[-1])
    
    else:
        parsed = l.split()
        ftype = 'dir' if l.startswith('dir') else 'file'
        size = 0 if l.startswith('dir') else int(parsed[0])
        name = parsed[-1]
        cur.add_child(Node(ftype, name, size, cur))

# Part 1
tot = sum_subdir_fsize(root)
print(part1)

# Part 2
threshold = tot - 40000000
part2_candidates.sort()
print(part2_candidates[bisect.bisect_right(part2_candidates, threshold)])
