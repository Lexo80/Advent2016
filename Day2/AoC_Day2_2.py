"""
Advent of code 2016 
Day 2 part 2
"""


class SecondKeypad():
    """manage keypad index for Advent of code day 2 part 2"""

    def __init__(self):
        self.x = 0
        self.y = 2
        self.keypad = (('_', '_', '1', '_', '_'),
                       ('_', '2', '3', '4', '_'),
                       ('5', '6', '7', '8', '9'),
                       ('_', 'A', 'B', 'C', '_'),
                       ('_', '_', 'D', '_', '_')
                       )

    def update(self, s):
        if str(s) == 'U':
            if self.keypad[self.y][self.x] in ('D', 'A', 'B', 'C', '6', '7', '8', '3'):
                self.y -= 1
        elif str(s) == 'D':
            if self.keypad[self.y][self.x] in ('1', '2', '3', '4', '6', '6', '7', '8', 'B'):
                self.y += 1
        elif str(s) == 'L':
            if self.keypad[self.y][self.x] in ('3', '4', '6', '7', '8', '9', 'B', 'C'):
                self.x -= 1
        elif str(s) == 'R':
            if self.keypad[self.y][self.x] in ('2', '3', '5', '6', '7', '8', 'A', 'B'):
                self.x += 1
        else:
            pass

    def getkey(self):
        return str(self.keypad[self.y][self.x])


with open('puzzel1.txt') as f:
    keys = [element.strip('\n') for element in f.readlines()]


this = SecondKeypad()
code = str('')
for key in keys:
    for element in key:
        this.update(element)
    code += str(this.getkey())
print(code)
