with open('input.txt') as inputfile:
    data = [int(datalen) for datalen in inputfile.readlines()]

increase = 0
for firstval, nextval in zip(data, data[1:]):
    if nextval > firstval:
        increase += 1
print(increase)

slideinc = 0
slidelist = []
for firstval, secval, thirdval in zip(data, data[1:], data[2:]):
    slidelist.append(firstval + secval + thirdval)
for firstslide, nextslide in zip(slidelist, slidelist[1:]):
    if nextslide > firstslide:
        slideinc += 1
print(slideinc)
