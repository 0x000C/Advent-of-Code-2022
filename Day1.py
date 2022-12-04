# Get input
with open("Inputs/Day1.txt", "r") as inputfile:
    inputdata = inputfile.readlines()

elfcalories = [0]   # Create list with placeholder for the first elf
for i in range(len(inputdata)):
    inputdata[i] = inputdata[i].removesuffix("\n")  # Remove junk from input
    if inputdata[i]:    # If the current input element is a number, add it to the last elf element
        elfcalories[-1] += int(inputdata[i])
    else:   # If the current input element is empty, create a new elf element
        elfcalories.append(0)
elfcalories.sort(reverse=True)

print("Part 1, top 1 most calories:", elfcalories[0])
print("Part 2, top 3 most calories:", sum(elfcalories[:3]))
