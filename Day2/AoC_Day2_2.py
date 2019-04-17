"""
Advent of code 2016 
Day 2 part 1
"""
from collections import namedtuple


class Index():
    """manage keypad index for Advent of code day 2 part 1"""

    def __init__(self):
        self.iH = 1
        self.iV = 1

    def update(self, s):
        if str(s).upper() == 'U':
            self.iV -= 1
            if self.iV <= 0:
                self.iV = 0
        elif str(s).upper() == 'D':
            self.iV += 1
            if self.iV >= 2:
                self.iV = 2
        elif str(s).upper() == 'R':
            self.iH += 1
            if self.iH >= 2:
                self.iH = 2
        elif str(s).upper() == 'L':
            self.iH -= 1
            if self.iH <= 0:
                self.iH = 0
        else:
            pass

    def getindexes(self):
        return (self.iV, self.iH)


with open('puzzel1.txt') as f:
    keys = [element.strip('\n') for element in f.readlines()]

keypad = tuple(tuple(spalte + 3 * zeile for spalte in range(1, 4))
               for zeile in range(3))


index = Index()
code = str('')
Point = namedtuple('Point', ['zeile', 'spalte'])
for key in keys:
    for element in key:
        index.update(element)
    k = Point(index.getindexes()[0], index.getindexes()[1])
    taste = keypad[k.zeile][k.spalte]
    code += str(taste)

x = ((1),
    (2, 3, 4),
    (5, 6, 7, 8, 9),
    ('A', 'B', 'C'),
    ('D'))

print(x)