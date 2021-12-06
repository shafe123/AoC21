def readFile(inputLocation):
    with open(inputLocation, 'r') as inputFile:
        lines = inputFile.readlines()

    for index, line in enumerate(lines):
        lines[index] = int(line)

    return lines


def processLinesByOne(lines):
    count = 0
    for index, line in enumerate(lines):
        if index == len(lines) - 1:
            break
        if line < lines[index + 1]:
            count += 1

    return count


def processLinesByWindow(lines, windowSize):
    count = 0
    sums = []
    currentSum = sum(lines[0:windowSize])
    sums.append(currentSum)

    for index in range(windowSize, len(lines)):
        currentSum -= lines[index-windowSize]
        currentSum += lines[index]
        sums.append(currentSum)

    with open('input/day1window.txt', 'w') as outputFile:
        outputFile.write('\n'.join((str(element) for element in sums)))

    count = processLinesByOne(sums)

    return count


if __name__ == "__main__":
    lines = readFile('input/day1.txt')
    print(processLinesByOne(lines))
    print(processLinesByWindow(lines, 3))
