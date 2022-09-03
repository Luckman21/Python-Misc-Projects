'''
Created on Apr 18, 2017

@author: Luqmaan
'''
import time
from random import randint

print "Welcome to Hotel Dusk!\n"
time.sleep(1)
name = raw_input("Please enter your full name here: ")

space  = name.find(" ")
space +=1 
name1 = name[space:]

time.sleep(1)
print "\nHello, "+name1+".\n"
time.sleep(1)
cash = input ("What is the price of your hotel room per night?: ")
time.sleep(1)
print
day = input ("How many nights will you be staying?: ")
time.sleep(1)
print 
print "Now, before you enter your discount amount, make sure there are no percent signs.\n"
time.sleep(1)
print "Example: 10% -> 10\n"
time.sleep(1)
dis = input ("Please enter your discount amount now: ")
time.sleep(1)
print

total = (day*cash - dis*0.01)*1.13
save = (day*cash)* dis*0.01
print "\nYour total amount with your discount and tax is: "+str(total)
time.sleep(1)
print "\nYou have saved: "+str(save)+"\n"
time.sleep(1)

room = randint (0,340)

if room == 215:
    print "\nYour room number is 215.  That's a special room!  It's name is Wish."

else:
    print "\nYour room number is "+str(room)

time.sleep(1)
print "\nHave a nice day, "+name+"!"
