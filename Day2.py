def read_data():
    with open("Inputs/Day2.txt", "r") as inputfile:
        messy_data = inputfile.readlines()
        tuplelist = []
        for i in range(len(messy_data)):
            tuplelist.append((messy_data[i][0], messy_data[i][2]))
        return tuplelist


def generate_test_data():
    testdata = []
    for i in ['A', 'B', 'C']:
        for j in ['X', 'Y', 'Z']:
            testdata.append((i, j))
    return testdata


def calculate_part1_score(a, b):
    lose, draw, win = 0, 3, 6
    outcome, hand = 0, ord(b) - 87
    match a:
        case 'A':
            match b:
                case 'X': outcome = draw
                case 'Y': outcome = win
                case 'Z': outcome = lose
        case 'B':  # paper
            match b:
                case 'X': outcome = lose
                case 'Y': outcome = draw
                case 'Z': outcome = win
        case 'C':  # scissors
            match b:
                case 'X': outcome = win
                case 'Y': outcome = lose
                case 'Z': outcome = draw
    return outcome + hand


def calculate_part2_score(a, b):
    lose, draw, win = 0, 3, 6
    rock, paper, scissors = 1, 2, 3

    outcome = 0
    match b:
        case 'X': outcome = lose
        case 'Y': outcome = draw
        case 'Z': outcome = win

    hand = 0
    match a:
        case 'A':  # rock
            match b:
                case 'X': hand = scissors
                case 'Y': hand = rock
                case 'Z': hand = paper
        case 'B':  # paper
            match b:
                case 'X': hand = rock
                case 'Y': hand = paper
                case 'Z': hand = scissors
        case 'C':  # scissors
            match b:
                case 'X': hand = paper
                case 'Y': hand = scissors
                case 'Z': hand = rock
    return hand + outcome


data = read_data()
part1score, part2score = 0, 0

for i in data:
    part1score += calculate_part1_score(i[0], i[1])
    part2score += calculate_part2_score(i[0], i[1])

print("Part 1:", part1score)
print("Part 2:", part2score)
