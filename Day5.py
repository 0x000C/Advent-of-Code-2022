def read_data(textfile):
    with open(textfile, "r") as infile:
        outputdata = infile.readlines()
    outputdata = [i.removesuffix('\n') for i in outputdata]
    return outputdata


def create_table(inputdata):  # Looking back, holy smokes what was I thinking.
    inputdata = [i.split("[") for i in inputdata if "[" in i]
    for i in range(len(inputdata)):
        inputdata[i].remove('')  # remove empty string elements
        # make each element equal to first character of each element
        inputdata[i] = [inputdata[i][x][0] for x in range(len(inputdata[i]))]
    outputtable = []
    for i in range(len(inputdata[0])):
        outputtable.append([])  # create an output list of appropriate size
    for i in range(len(inputdata)):  # remove zeroes and transpose
        for j in range(len(inputdata[i])):
            if inputdata[i][j] != "0":
                outputtable[j].append(inputdata[i][j])
    for i in range(len(outputtable)):
        outputtable[i] = ''.join(outputtable[i])  # unsplit lists
    return outputtable


def create_moves(inputdata):
    outputdata = [i.split(' ') for i in inputdata if "move" in i]
    for i in range(len(outputdata)):
        outputdata[i] = [int(j) for j in outputdata[i] if j.isdigit()]
        outputdata[i] = [j - 1 for j in outputdata[i]]
    return outputdata


def execute_part1_move(inputtable, inputmove):
    moveqty = inputmove[0] + 1
    fromcolumn = inputtable[inputmove[1]]
    tocolumn = inputtable[inputmove[2]]

    for i in range(moveqty):
        tocolumn = fromcolumn[0] + tocolumn
        fromcolumn = fromcolumn[1:]

    inputtable[inputmove[1]] = fromcolumn
    inputtable[inputmove[2]] = tocolumn
    return inputtable


def execute_part2_move(inputtable, inputmove):
    moveqty = inputmove[0] + 1
    fromcolumn = inputtable[inputmove[1]]
    tocolumn = inputtable[inputmove[2]]

    tocolumn = fromcolumn[0:moveqty] + tocolumn
    fromcolumn = fromcolumn[moveqty:]

    inputtable[inputmove[1]] = fromcolumn
    inputtable[inputmove[2]] = tocolumn
    return inputtable


inputfile = "Inputs/Day5.txt"
data = read_data(inputfile)
datatable1 = create_table(data)
datatable2 = datatable1.copy()
moves = create_moves(data)

for move in moves:
    datatable1 = execute_part1_move(datatable1, move)
    datatable2 = execute_part2_move(datatable2, move)

tops1, tops2 = '', ''
for i in datatable1:
    tops1 += i[0]
for i in datatable2:
    tops2 += i[0]

print("Part 1:", tops1)
print("Part 2:", tops2)
