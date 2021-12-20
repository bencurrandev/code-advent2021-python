"""
This finds winning bingo boards
Classes: None
Functions: None
"""
with open('input.txt', encoding='UTF-8') as inputfile:
    data = [str(datalen).strip() for datalen in inputfile.readlines()]

NUMBERS = []
for i in data[0].split(","):
    NUMBERS.append(int(i))

BOARDS = []
BOARD = []
for i in data[1::]:
    if i == '':
        if BOARD:
            BOARDS.append(BOARD)
            BOARD = []
    else:
        BOARDLINE = i.split()
        BOARD.append(BOARDLINE)

BOARDS.append(BOARD)

FOUND = []
for i in BOARDS:
    assert len(i)==5 and len(i[0])==5
    FOUND.append([[False for _ in range(5)] for _ in range(5)])

BINGOCARD = [False for _ in range(len(BOARDS))]

for num in NUMBERS:
    for board in range(len(BOARDS)):
        for row in range(5):
            for column in range(5):
                if int(BOARDS[board][row][column]) == num:
                    FOUND[board][row][column] = True
        BINGO = False
        for row in range(5):
            OK = True
            for column in range(5):
                if not FOUND[board][row][column]:
                    OK = False
            if OK:
                BINGO = True
        for column in range(5):
            OK = True
            for row in range(5):
                if not FOUND[board][row][column]:
                    OK = False
            if OK:
                BINGO = True
        if BINGO and not BINGOCARD[board]:
            BINGOCARD[board] = True
            nwin = len([j for j in range(len(BOARDS)) if BINGOCARD[j]])
            if nwin == 1 or nwin == len(BOARDS):
                UNMARKED = 0
                for row in range(5):
                    for column in range(5):
                        if not FOUND[board][row][column]:
                            UNMARKED += int(BOARDS[board][row][column])
                print(UNMARKED * num)

