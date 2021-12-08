def readFile(inputLocation):
    with open(inputLocation, 'r') as inputFile:
        inputLines = inputFile.readlines()

    left = []
    right = []
    for line in inputLines:
        sides = line.split(' | ')
        left.append(sides[0].split())
        right.append(sides[1].split())

    return left, right


def countWordLength(segmentList):
    countByLength = {}
    for i in range(8):
        countByLength[i] = 0

    for line in segmentList:
        for word in line:
            countByLength[len(word)] += 1

    return countByLength


segmentMap = {
    'a': int('1000000', 2),
    'b': int('0100000', 2),
    'c': int('0010000', 2),
    'd': int('0001000', 2),
    'e': int('0000100', 2),
    'f': int('0000010', 2),
    'g': int('0000001', 2)
}


def countSetBits(num):
    binary = bin(num)
    setBits = [ones for ones in binary[2:] if ones == '1']
    return len(setBits)


def wordToBitmap(word):
    byte = int('0', 2)
    for letter in word:
        byte |= segmentMap[letter]
    return byte


def deduceMapping(leftSide):
    leftSide.sort(key=len)

    # do some bit-mapping shenanigans
    one = wordToBitmap(leftSide[0])
    seven = wordToBitmap(leftSide[1])
    four = wordToBitmap(leftSide[2])
    eight = wordToBitmap(leftSide[9])

    abcdf = (seven | four)
    for i in range(6, 9):
        currentWord = wordToBitmap(leftSide[i])
        if countSetBits(currentWord ^ abcdf) == 1:
            nine = currentWord
        elif countSetBits(currentWord & one) == 2:
            zero = currentWord
        else:
            six = currentWord

    for i in range(3, 6):
        currentWord = wordToBitmap(leftSide[i])
        if countSetBits(currentWord ^ six) == 1:
            five = wordToBitmap(leftSide[i])
        elif countSetBits(currentWord ^ nine) == 1:
            three = wordToBitmap(leftSide[i])
        else:
            two = wordToBitmap(leftSide[i])

    return zero, one, two, three, four, five, six, seven, eight, nine


def processLines(left, right):
    rightSum = 0
    for row in range(len(left)):
        mapping = deduceMapping(left[row])

        power = 4
        for entry in right[row]:
            currentWord = wordToBitmap(entry)
            for val in range(10):
                if currentWord == mapping[val]:
                    print(val, end="")
                    rightSum += val * pow(10, power)
            power -= 1
        print()
    return rightSum


leftLines, rightLines = readFile('input/day8.txt')
outputSum = processLines(leftLines, rightLines)
print(outputSum)
