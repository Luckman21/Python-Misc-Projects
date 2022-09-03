'''
Created on Feb 20, 2018

@author: Luqmaan
'''
import time 

print "ADD DECIMALS TO THE END OF THE NUMBER (Ex: 7 = 7.0)"
time.sleep(3)

while True:
    print "\nEnter the coordinates for point A"
    time.sleep(1)
    x1 = input ("X coordinate: ")
    y1 = input ("Y coordinate: ")
    
    print "\nEnter the coordinates for point B"
    time.sleep(1)
    x2 = input ("X coordinate: ")
    y2 = input ("Y coordinate: ")

    slope = "%.2f" %((y2-y1)/(x2-x1))
    
    print "The slope of the line with the coordinates of ("+str(x1)+", "+str(y1)+") and ("+str(x2)+", "+str(y2)+") is:\nm = "+str(slope)
    time.sleep(1)