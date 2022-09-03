'''
Created on May 30, 2017

@author: Luqmaan
'''
from random import randint
import time

mark = []
mark1 = []
marks = []
total = 0

time.sleep(1)
print "Welcome to the \"Average Calculator\"!\n" #Introduction

for x in range (1,4): #numbers 1,4 because the for loop will count up to 4 not include 4
    
    while True:
        
        time.sleep(1)
        y = input ("Enter a mark between 1 and 100: ")
        
        if y >= 1 and y <= 100:
            mark.append(y) #Adds the mark if within range to the list and breaks the loop to count as mark
            break

        else:
            time.sleep(1)
            print "\nInvalid input.  ",y," is not within range 0-100.\n"#Tells the user that their input is incorrect and doesn't count as a mark
            
            
for x in range (1,4): #numbers 1,4 because the for loop will count up to 4 not include 4
    
    z = randint(1,100) #This will generate our random marks
    mark1.append(z)#This adds the randomly generated marks to the other list

for x in range (0,3):
    marks.append(mark[x]) #Adding marks from the first list into the other list
    marks.append(mark1[x]) #Adding marks from the second list into the other list
print 
print marks #prints the list
marks.reverse() #reverses the list
print marks

for x in marks: #Counts the total by adding up all the marks
    total+=x
    
time.sleep(1)
print "\nYour average this semester, with the marks given and entered:"
print marks
print "\nYour average is : "+str(float(total)/len(marks)) #Counts the average by dividing the total by the number of marks in the list

time.sleep(1)
if float(total)/len(marks) >= 50: #Checks to see whether the average is above or below 50
    
    print "\nYou are passing! :D"
    
else:
    print "\nYou are failing :/"

    
    
    
    
    
    
    