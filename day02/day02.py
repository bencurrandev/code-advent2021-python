"""
This checks for sub location after movement instructions
Classes: None
Functions: None
"""
with open('input.txt', encoding='UTF-8') as inputfile:
    data = [str(datalen) for datalen in inputfile.readlines()]

X = 0
Y = 0

for movement in data:
    thismove = movement.split(" ")
    if thismove[0] == "forward":
        X += int(thismove[1])
    elif thismove[0] == "down":
        Y += int(thismove[1])
    elif thismove[0] == "up":
        Y -= int(thismove[1])

print(X*Y)
