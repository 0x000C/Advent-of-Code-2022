def read_data(textfile):
    inputlines = []
    tuplelist = []
    with open(textfile, "r") as infile:
        inputlines = infile.readlines()
    for i in inputlines:
        i = i.removesuffix('\n').split(",")
        i = i[0].split("-") + i[1].split("-")
        for j in range(len(i)):
            i[j] = int(i[j])
        tuplelist.append(((i[0], i[1]), (i[2], i[3])))
    return tuplelist


def calculate_part1_score(inputlist):
    score = 0
    for i in inputlist:
        if i[0][0] <= i[1][0] and i[0][1] >= i[1][1]:
            score += 1
        elif i[1][0] <= i[0][0] and i[1][1] >= i[0][1]:
            score += 1
    return score


def calculate_part2_score(inputlist):
    score = 0
    for i in inputlist:
        min_a = i[0][0]
        max_a = i[0][1]
        min_b = i[1][0]
        max_b = i[1][1]
        if min_a <= min_b <= max_a:
            score += 1
        elif min_a <= max_b <= max_a:
            score += 1
        elif min_b <= min_a <= max_b:
            score += 1
        elif min_b <= max_a <= max_b:
            score += 1
    return score


inputfile = "Inputs/Day4.txt"
data = read_data(inputfile)
part1score = calculate_part1_score(data)
part2score = calculate_part2_score(data)

print("Part 1:", part1score)
print("Part 2:", part2score)
