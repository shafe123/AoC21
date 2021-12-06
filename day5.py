def readFile(inputLocation):
    with open(inputLocation, 'r') as inputFile:
        lines = inputFile.readlines()

    for index, line in enumerate(lines):
        lines[index] = line.strip('\n')

    return lines