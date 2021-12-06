def readFile(inputLocation):
    with open(inputLocation, 'r') as inputFile:
        lines = inputFile.readlines()

    for index, line in enumerate(lines):
        lines[index] = line.strip('\n')

    return lines


def processLines(lines):
    counts = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    gammaRate = 0

    for line in lines:
        for index, char in enumerate(line):
            if char == '1':
                counts[index] += 1

    for index, count in enumerate(counts):
        if count > len(lines)/2:
            gammaRate |= int('100000000000', 2) >> index

    epsilonRate = gammaRate ^ int('111111111111', 2)

    return gammaRate, epsilonRate


def removeLinesByBit(lines):
    o2 = lines.copy()
    co2 = lines.copy()

    for i in range(0, 12):
        if len(o2) > 1:
            o2Ones = countColumn(o2, i)

            if o2Ones >= len(o2)/2:
                o2 = filterColumn(o2, i, '1')
            else:
                o2 = filterColumn(o2, i, '0')

        if len(co2) > 1:
            co2Ones = countColumn(co2, i)
            if co2Ones >= len(co2)/2:
                co2 = filterColumn(co2, i, '0')
            else:
                co2 = filterColumn(co2, i, '1')
    return o2[0], co2[0]


def countColumn(lines, index):
    count = 0

    for line in lines:
        if line[index] == '1':
            count += 1

    return count


def filterColumn(lines, index, character):
    result = []

    for line in lines:
        if line[index] == character:
            result.append(line)

    return result


lines = readFile('input/day3.txt')
print(lines)
g, e = processLines(lines)
print(g * e)

o, c = removeLinesByBit(lines)
print(o, c, int(o, 2) * int(c, 2))
