def readFile(inputLocation):
    with open(inputLocation, 'r') as inputFile:
        lines = inputFile.readlines()

    for index, line in enumerate(lines):
        lines[index] = line.split(' ')
        lines[index][1] = int(lines[index][1])

    return lines


def processLines(lines):
    horizontal = 0
    vertical = 0

    for entry in lines:
        if entry[0] == 'forward':
            horizontal += entry[1]
        elif entry[0] == 'up':
            vertical -= entry[1]
        elif entry[0] == 'down':
            vertical += entry[1]

    return horizontal, vertical


def processLinesWithAim(lines):
    horizontal = 0
    vertical = 0
    aim = 0

    for entry in lines:
        if entry[0] == 'forward':
            horizontal += entry[1]
            vertical += entry[1] * aim
        elif entry[0] == 'up':
            aim -= entry[1]
        elif entry[0] == 'down':
            aim += entry[1]

    return horizontal, vertical


lines = readFile('input/day02.txt')
print(lines)
h, v = processLinesWithAim(lines)

print(h, v, h*v)
