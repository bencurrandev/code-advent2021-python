"""
This checks for power consumption
Classes: None
Functions: None
"""
with open('input.txt', encoding='UTF-8') as inputfile:
    data = [str(datalen) for datalen in inputfile.readlines()]

BITS = 12
GAMMABIN = ""
EPSILONBIN = ""
for k in range(BITS):
    BINCOUNT = 0
    for binbit in data:
        BINCOUNT += int(binbit[k])
    result = round(BINCOUNT/len(data))
    GAMMABIN += str(result)
    EPSILONBIN += str(1-result)
GAMMA = int(GAMMABIN, 2)
EPSILON = int(EPSILONBIN, 2)
POWER = GAMMA * EPSILON
print(POWER)
