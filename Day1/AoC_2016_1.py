"""
Advent of Code 2016
Day 1

"""

class direction:
    def __init__(self):
        self.index = 0 
        self.direction = ['N','O','S','W']
        
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
distance_N=0  
distance_O=0
distance_S=0
distance_W=0
with open('Puzzel Input.txt') as f:
    stream = f.read()
    data = stream.split(",") 
        
    i=0   
    print('anfang')
    for element in data:
        data[i] = data[i].strip()
        i+=1
    for element in data:
        heading.changeDir(element[0])
        d=heading.getDir()
        print(element, end=':')
        print(d,end='  ')
        if d is 'N':
            distance_N += int(element[1:len(element)])
        elif d is 'S':
            distance_S  -= int(element[1:len(element)])            
        elif d is 'O':
            distance_O += int(element[1:len(element)])
        elif d is 'W':
            distance_W -= int(element[1:len(element)])
        else:
            pass
        print('Norden:'+str(distance_N), end=' ')
        print('Osten:' + str(distance_O),end=' ')
        print('Sueden:'+ str(distance_S),end=' ')
        print('Westen:' + str(distance_W),end=' ')
        print('Gesamtdistanz:'+str(distance_N + distance_O + distance_S + distance_W),end='\n')
    print('n-s:' + str(distance_N + distance_S))
    print('o-w:' + str(distance_O + distance_W)) 
    print(abs(distance_N + distance_S)+abs(distance_O + distance_W))       
   
    
