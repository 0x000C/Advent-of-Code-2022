def read_data(textfile):
    with open(textfile) as infile:
        return infile.read()

def is_unique(inputstring):
    for i in range(len(inputstring)):
        for j in range(i+1,len(inputstring)):
            print(inputstring[i],inputstring[j])
            if inputstring[i] == inputstring[j]:
                return False
    return True

data = read_data("Inputs/Day6Small.txt")

cursor = data[0:4]

for i in range(4,len(data)):
    if is_unique(cursor):
        
