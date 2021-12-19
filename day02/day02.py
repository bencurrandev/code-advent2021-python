"""
This checks for sub location after movement instructions
Classes: None
Functions: None
"""
with open('input.txt', encoding='UTF-8') as inputfile:
    data = [str(datalen) for datalen in inputfile.readlines()]

X = 0
Y = 0
A = 0 # Part2

for movement in data:
    thismove = movement.split(" ")
    if thismove[0] == "forward":
        X += int(thismove[1])
        Y += A * int(thismove[1]) # Part2
    elif thismove[0] == "down":
        # Part1 Y += int(thismove[1])
        A += int(thismove[1])
    elif thismove[0] == "up":
        # Part1 Y -= int(thismove[1])
        A -= int(thismove[1])

print(X*Y)
