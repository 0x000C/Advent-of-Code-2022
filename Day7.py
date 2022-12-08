nodelist = []


class Node:
    def __init__(self, parent, name, children, size, directory):
        self.name = name
        self.children = children
        self.size = size
        self.parent = parent
        self.directory = directory
        nodelist.append(self)

    def get_size(self):
        if len(self.children) == 0:
            return self.size
        sum = 0
        for i in self.children:
            sum += i.get_size()
        self.size = sum
        return sum

    def find_child(self, name):
        for i in self.children:
            if i.name == name:
                return i
        return None

    def add_child(self, child):
        self.children.append(child)

    def get_parent(self):
        return self.parent


with open("Inputs/Day7.txt") as datafile:
    inputdata = [i.removesuffix('\n').split(" ") for i in datafile.readlines()]

currentnode = Node(None, '/', [], 0, True)

for i in inputdata[0]:
    if i == "/":
        inputdata = inputdata[1:]

for i in inputdata:
    if i[0] == "$":
        if i[1] == "cd":
            if i[2] == "..":
                if currentnode.name == "/":
                    pass
                else:
                    currentnode = currentnode.get_parent()
            else:
                currentnode = currentnode.find_child(i[2])
        elif i[1] == "ls":
            pass
    elif i[0] == "dir":
        newnode = Node(currentnode, i[1], [], 0, True)
        currentnode.add_child(newnode)
    else:
        newnode = Node(currentnode, i[1], [], int(i[0]), False)
        currentnode.add_child(newnode)

[node.get_size() for node in nodelist]
nodelist = sorted(nodelist, key=lambda node: node.size)

spaceneeded = disk_space_used = 30000000 - (70000000 - nodelist[-1].size)

for i in range(len(nodelist)):
    if nodelist[i].size > spaceneeded and nodelist[i].directory:
        part2node = nodelist[i]
        break

print("Part 1:", sum([node.size for node in nodelist if 0 <
      node.size < 100000 and node.directory]))
print("Part 2:", part2node.size)
