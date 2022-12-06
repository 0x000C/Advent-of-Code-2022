def read_data(textfile):
    with open(textfile) as infile:
        return infile.read()


def is_unique(inputstr):
    for i in range(len(inputstr)):
        for j in range(i + 1, len(inputstr)):
            if inputstr[i] == inputstr[j]:
                return False
    return True


def find_unique_location(inputstr, uniquesize):
    for i in range(len(data)):
        if i + uniquesize < len(inputstr):
            cursor = inputstr[i:i + uniquesize]
        else:
            return -1
        if is_unique(cursor):
            return i + uniquesize


data = read_data("Inputs/Day6.txt")

print("Part 1:", find_unique_location(data, 4))
print("Part 2:", find_unique_location(data, 14))
