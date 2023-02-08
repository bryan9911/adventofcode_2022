class Node:
    def __init__(self, type, size, name, parent):
        self.type = type
        self.size = size
        self.name = name
        self.parent = parent
        self.children = []


data = open('Day7.txt').readlines()

root = Node('dir', 0, '/', None)
cur_dir = root
for i in data[1:]:
    check = i.split()
    if check[0] == '$' and check[1] == 'cd':
        if check[2] != '..':
            child = Node('dir', 0, check[2], cur_dir)
            cur_dir.children.append(child)
            cur_dir = child
        elif check[2] == '..':
            cur_dir = cur_dir.parent
    elif check[0] == '$' and check[1] == 'ls':
        continue
    elif check[0] == 'dir':
        continue
    else:
        size = int(check[0])
        name = check[1]
        child = Node('file', size, name, cur_dir)
        cur_dir.children.append(child)

total = 0
thres = []


def walk(node: Node):
    global total, thres
    if node.type == 'file':
        return node.size
    if node.type == 'dir':
        sub_total = sum([walk(x) for x in node.children])
        thres.append(sub_total)
        if sub_total <= 100000:
            total += sub_total
    return sub_total


tot = walk(root)
print(total)
threshold = tot - 40000000

temp = tot
for n in thres:
    if n > threshold:
        del_node = n
        if del_node < temp:
            temp = del_node

print(temp)
