class Tree:
    def __init__(self, size=0, seen=False, score=1):
        self.size = size
        self.seen = seen
        self.score = score


def part1(treegrid):
    for edge in range(4):
        for row in treegrid:
            tallesttreesize = row[0].size
            row[0].seen = True
            for treenum in range(len(row)):
                if row[treenum].size > tallesttreesize:
                    row[treenum].seen = True
                    tallesttreesize = row[treenum].size
        treegrid = list(zip(*treegrid[::-1])) #rotate the grid

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
                for othertreenum in range(treenum - 1, -1, -1):
                    score += 1
                    if row[treenum].size <= row[othertreenum].size:
                        break
                row[treenum].score *= score
        treegrid = list(zip(*treegrid[::-1])) 

    maxscore = 0
    for x in treegrid:
        for y in x:
            if y.score > maxscore:
                maxscore = y.score
    return maxscore

def get_data(inputfile):
    with open(inputfile) as datafile:
        lines = [i.removesuffix('\n') for i in datafile.readlines()]
        data = []
        for i in lines:
            data.append([Tree(int(x)) for x in i])
    return data

inputdata = get_data("Inputs/Day8.txt")
print("Part 1:", part1(inputdata))
print("Part 2:", part2(inputdata))
