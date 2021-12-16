import math

def readFile(inputLocation):
    with open(inputLocation, 'r') as inputFile:
        inputLines = inputFile.readlines()

    return inputLines[0].strip()


def convertToBits(hex):
    binary = ""
    for character in hex:
        value = int(character, 16)
        binary += format(value, '04b')
    return binary


def identifyVersion(packet):
    version = int(packet[0:3], 2)
    return version


def identifyType(packet):
    type = int(packet[3:6], 2)
    return type


def identifyValue(packet, start):
    first = packet[start]
    number = packet[start+1:start+5]
    count = 1
    while first != '0':
        index = start + count * 5
        first = packet[index]
        number += packet[index+1:index+5]
        count += 1
    end = count * 5 + start
    return int(number, 2), end


def processPacket(packet):
    version = identifyVersion(packet)
    versions = [version]

    type = identifyType(packet)
    types = [type]

    values = []
    if type == 4:
        value, valueEnd = identifyValue(packet, 6)
        values.append(value)

    else:
        lengthType = packet[6]
        if lengthType == '0':
            last = 22
            bitLength = int(packet[7:22], 2)
            while last - 22 < bitLength:
                subVersion, subTypes, currentValues, valueEnd = processPacket(packet[last:])
                versions.extend(subVersion)
                types.extend(subTypes)
                values.extend(currentValues)
                last = last + valueEnd
            valueEnd = last
        else:
            subPackets = int(packet[7:18], 2)
            count = 0
            last = 18
            while count < subPackets:
                subVersion, subTypes, currentValues, valueEnd = processPacket(packet[last:])
                versions.extend(subVersion)
                types.extend(subTypes)
                values.extend(currentValues)
                last = last + valueEnd
                count += 1
            valueEnd = last

    if type == 0:
        values = [sum(values)]
    elif type == 1:
        values.append(1)
        values = [math.prod(values)]
    elif type == 2:
        values = [min(values)]
    elif type == 3:
        values = [max(values)]
    elif type == 5:
        values = [1 if values[0] > values[1] else 0]
    elif type == 6:
        values = [1 if values[0] < values[1] else 0]
    elif type == 7:
        values = [1 if values[0] == values[1] else 0]

    return versions, types, values, valueEnd


line = readFile('input/day16.txt')
bits = convertToBits(line)
versions, types, values, end = processPacket(bits)
print(versions)
print(types)
print(values)

