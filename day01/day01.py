"""
This checks for increases in depth readings
Classes: None
Functions: None
"""
with open('input.txt', encoding='UTF-8') as inputfile:
    data = [int(datalen) for datalen in inputfile.readlines()]

INCREASE = 0
for firstval, nextval in zip(data, data[1:]):
    if nextval > firstval:
        INCREASE += 1
print(INCREASE)

SLIDEINC = 0
slidelist = []
for firstval, secval, thirdval in zip(data, data[1:], data[2:]):
    slidelist.append(firstval + secval + thirdval)
for firstslide, nextslide in zip(slidelist, slidelist[1:]):
    if nextslide > firstslide:
        SLIDEINC += 1
print(SLIDEINC)
