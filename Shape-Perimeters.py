'''
Created on May 8, 2018

@author: Luck
'''
polygon,length = [[1,1],[4,6],[7,0],[4,1],[0,0]],0
sides = 2 #The number of sides a polygon has after subtracting 3
shape = "polygon"

#SQUARE
'''
square = [[1,2],[2,2],[2,1],[1,1]]
polygon,sides,shape = square,1,"square"
'''
#TRIANGLE
'''
triangle = [[1,2],[2,1],[1,1]]
polygon,sides,shape = triangle,0,"triangle"
'''
#RECTANGLE
'''
rectangle = [[1,1],[1,4],[4,4],[4,1]]
polygon,sides,shape = rectangle,1,"rectangle"
'''
#HEXAGON
'''
hexagon = [[1,1],[2,0],[4,0],[5,1],[4,2],[2,2]]
polygon,sides,shape = hexagon,3,"hexagon"
'''
#OCTAGON
'''
octogon = [[1,1],[2,0],[4,0],[5,1],[5,2],[4,3],[2,3],[1,2]]
polygon,sides,shape = octagon,4,"octagon"
'''

z = sides

for i in range(0,3+z):
    if i < 2+z:
        length+=(((polygon[i+1][0]-polygon[i][0])**(2) + (polygon[i+1][1]-polygon[i][1])**(2))**(0.5))
        
    else:
        length+=((polygon[2+z][0]-polygon[0][0])**(2) + (polygon[2+z][1]-polygon[0][1])**(2))**(0.5)

print "\nTherefore, the perimeter of the "+shape+" is "+str(length)+" units."