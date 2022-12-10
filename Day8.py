class Tree:
    def __init__(self, size = 0, seen = False, score = 1):
        self.size = size
        self.seen = seen
        self.score = score

with open("Inputs/Day8.txt") as datafile:
    lines = [i.removesuffix('\n') for i in datafile.readlines()]
    inputdata = []
    for i in lines:
        inputdata.append([Tree(int(x)) for x in i])

def part1(treegrid):
    for edge in range(4):
        for rownum in range(len(treegrid)):
            tallesttreesize = treegrid[rownum][0].size
            treegrid[rownum][0].seen = True
            for treenum in range(len(treegrid[rownum])):
                if treegrid[rownum][treenum].size > tallesttreesize:
                    treegrid[rownum][treenum].seen = True
                    tallesttreesize = treegrid[rownum][treenum].size
        treegrid = list(zip(*treegrid[::-1]))

    edgevisibletrees = 0
    for i in treegrid:
        for j in i:
            if j.seen:
                edgevisibletrees += 1
    return edgevisibletrees

def part2(treegrid):
    for edge in range(4):
        for row in treegrid:
            for treenum in range(len(row)):
                score = 0
                for othertreenum in range(treenum-1, -1, -1):
                    if row[treenum].size > row[othertreenum].size:
                        score += 1
                    else:
                        score += 1
                        break
                row[treenum].score *= score
        treegrid = list(zip(*treegrid[::-1]))

    maxscore = 0
    for x in treegrid:
        for y in x:
            if y.score > maxscore:
                maxscore = y.score
    return maxscore

print("Part 1:", part1(inputdata))
print("Part 2:", part2(inputdata))
