"""
Advent of Code 2016
Day 1
part 1

"""


class direction:
    def __init__(self):
        self.index = 0
        self.direction = ['N', 'O', 'S', 'W']

    def changeDir(self, d):
        if str(d) is 'R':
            self.index += 1
        elif str(d) is 'L':
            self.index -= 1
        else:
            pass
        self.index %= 4

    def getDir(self):
        return(self.direction[self.index])


heading = direction()
distance_N = 0
distance_O = 0
distance_S = 0
distance_W = 0
with open('Puzzel Input.txt') as f:
    stream = f.read()
    data = stream.split(",")
    i = 0
    data = [e.strip() for e in data]
    for element in data:
        turn, l = element[0], element[1:]
        heading.changeDir(turn)
        d = heading.getDir()
        if d is 'N':
            distance_N += int(l)
        elif d is 'S':
            distance_S -= int(l)
        elif d is 'O':
            distance_O += int(l)
        elif d is 'W':
            distance_W -= int(l)
        else:
            pass

    print(abs(distance_N + distance_S) + abs(distance_O + distance_W))
