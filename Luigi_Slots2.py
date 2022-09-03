'''
Created on May 1, 2017

@author: Luqmaan
'''
a = 0
x,y,z = 0, 5, 7

import time

while True:
    
    while a < 10:
        a+=1
        
        time.sleep(0.05)
        x+=1
        y+=1
        z+=1 
        print x,y,z
        