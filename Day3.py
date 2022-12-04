def read_data():
    with open("Inputs/Day3.txt", "r") as inputfile:
        messy_data = inputfile.readlines()
        tuplelist = []
        for i in messy_data:
            i = i.removesuffix('\n')
            x = int(len(i) / 2)
            tuplelist.append((i[0:x], i[x:]))
        return tuplelist


# ord(A) = 65, ord(Z) = 122, ord(a) = 97, ord(z)=122
def get_character_priority(x):
    if x.islower():
        return (ord(x) - 96)
    else:
        return (ord(x) - 38)


def find_same_character_part1(x):
    for i in x[0]:
        for j in x[1]:
            if i == j:
                return i
    print("No same character found.")
    return


def find_same_character_part2(x):
    charlist = ''
    for i in x[0]:
        for j in x[1]:
            if i == j and i not in charlist:
                charlist += i
    for i in x[2]:
        for j in charlist:
            if i == j:
                return i
    print("No same character found.")
    return


data = read_data()
part1sum, part2sum = 0, 0
#part2sum > 2273

for i in data:
    part1sum += get_character_priority(find_same_character_part1(i))

for i in range(0, len(data), 3):
    z = [data[i][0] + data[i][1],
         data[i + 1][0] + data[i + 1][1],
         data[i + 2][0] + data[i + 2][1]]
    part2sum += get_character_priority(find_same_character_part2(z))

print("Part 1:", part1sum)
print("Part 2:", part2sum)
