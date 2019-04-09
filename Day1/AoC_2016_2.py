class Heading(object):
    """docstring for direction"""
    heading = ['N', 'O', 'S', 'W']
    visitedPoints = []
    x, y = 0, 0
    index = 0
    checked = False


    def __init__(self):
        self.index = 0

    def processInputString(self, string_in):
        turn, d = string_in[0], string_in[1:]
        self.changeDirection(turn)
        self.checkPoints(d)

    def changeDirection(self, t):
        if t == 'R':
            self.index += 1
        elif t == 'L':
            self.index -= 1
        self.index %= 4
        # print(self.heading[self.index])

    def checkPoints(self, dist):
        lookingTo = self.heading[self.index]
        if lookingTo == 'N':
            for step in range(int(dist)):
                location = (self.x, self.y + (step + 1))
                self.visited(location)
        elif lookingTo == 'O':
            for step in range(int(dist)):
                location = (self.x + (step + 1), self.y)
                self.visited(location)
        elif lookingTo == 'S':
            for step in range(int(dist)):
                location = (self.x, self.y - (step + 1))
                self.visited(location)
        elif lookingTo == 'W':
            for step in range(int(dist)):
                location = (self.x - (step + 1), self.y)
                self.visited(location)
        self.x = location[0]
        self.y = location[1]

    def visited(self, pnt):
        if pnt in self.visitedPoints and self.checked == False:
            print('Der erste schon besuchte Punkt ist: ' +
                  str(abs(pnt[0]) + abs(pnt[1])))
            self.checked = True
        self.visitedPoints.append(pnt)


heading = Heading()
with open("Puzzel Input 2.txt") as f:
    data = f.read()
    myDataList = [e.strip() for e in data.split(',')]
    for element in myDataList:
        heading.processInputString(element)
