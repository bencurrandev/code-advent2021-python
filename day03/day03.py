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

O2 = data
CO2 = data
for k in range(BITS):
    if len(O2) > 1:
        O2A = len([x for x in O2 if x[k]=='0'])
        O2B = len([x for x in O2 if x[k]=='1'])
        if O2B >= O2A:
            O2 = [x for x in O2 if x[k]=='1']
        else:
            O2 = [x for x in O2 if x[k]=='0']
    if len(CO2) > 1:
        CO2A = len([x for x in CO2 if x[k]=='0'])
        CO2B = len([x for x in CO2 if x[k]=='1'])
        if CO2B >= CO2A:
            CO2 = [x for x in CO2 if x[k]=='0']
        else:
            CO2 = [x for x in CO2 if x[k]=='1']
OXYGEN = int(O2[0].strip(),2)
CARBDIOX = int(CO2[0].strip(),2)
LIFE = OXYGEN * CARBDIOX
print(LIFE)
