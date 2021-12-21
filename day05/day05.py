"""
This finds winning bingo boards
Classes: None
Functions: None
"""

from collections import defaultdict

with open('input.txt', encoding='UTF-8') as inputfile:
    data = [str(datalen).strip() for datalen in inputfile.readlines()]
