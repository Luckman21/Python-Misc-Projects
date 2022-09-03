'''
Created on Apr 24, 2017

@author: Luqmaan
'''
from random import randint
import time

print "For Best game experience, make sure your compiler is this high:"
print "|\n"*10
time.sleep(1)
start = raw_input ("Press \"ENTER\" key to START!")
print "\n"*30
time.sleep(1)
print "\nWelcome to Luigi's Mansion!\nIt's a mia, Luigi!\n"
name2 = raw_input ("What is your name?: ")
name1 = name2.count(" ")
g = 1

if name1 >= 1:
    name = name2[0:name2.find(" ")]
    
else:
    name = name2
    
if name.upper() == "MARIO":
    name = "bro"
    
elif name.upper() == "LUIGI":
    name = "doppleganger "+name2

print "Welcome to my mansion, "+name+"!"

highscore = 0

while g == 1:

    time.sleep(1)
    print "Ready to play, Luigi Slots?"
    time.sleep(1)
    print "\n3..."
    time.sleep(1)
    print "2..."
    time.sleep(1)
    print "1..."
    time.sleep(1)
    print "START!"
    print "-"*40
    
    money = 200.0
    score = 0
    a = 1
    
    
    while money > 0:
        
        b = 1
        
        numb1 = randint (1,7)
        numb2 = randint (1,7)
        numb3 = randint (1,7)
        
        time.sleep(1)
        
        while True:
            stop = raw_input ("Press \'ENTER\' key to stop the slots from moving!\n(To gamble, enter the amount you want to gamble and press \"ENTER\")")
            if stop == '':
                gamble = 20
                break
            elif float(stop) > 0:   
                gamble = float(stop)
                break
            else:
                continue
                
        print"\n\n(", numb1 , ")(" , numb2 , ")(" , numb3 , ")\n\n"
                
        if numb1 == numb2 or numb1 == numb3:
            if numb1 == numb2 == numb3:
                print "\nMAMA MIA, "+name.upper()+"!  All 3 numbers are the same!!!\n"
                money+=(gamble*10)
                score+=1
                
                
            elif numb1 == numb2:
                print "\nNice one!  2 numbers are the same!\n"
                money+=(gamble*3)
                score+=1
                
            elif numb1 == numb3:
                print "\nWow, "+name+"!  2 end numbers are the same!\n"
                money+=(gamble*numb1)
                score+=1
            
        elif numb2 == numb3:
            print "\nNice one!  2 numbers are the same!\n"
            money+= (gamble*3)
            score+=1
                
        else:
            print "\nSorry, no numbers are the same...\n"
            money-=gamble
            
        print "Money: "+str(money)
        print "Score: "+str(score)
        print
            
    if score > highscore:
        highscore = score
        hs = "Mama Mia!  A new high score!"
        
    else:
        highscore = highscore
        hs = "Good game!"
    
    print "-"*40
    time.sleep(1)
    print "GAME OVER"
    time.sleep(1)
    print
    print "Score: "+str(score)
    print "High Score: "+str(highscore)
    print hs
    print "\nPLAY AGAIN?\n\n1 - Yes\n2 - No"
    g = input (": ")
    
    time.sleep(1)
    
    if g == 2:
        print "\nBetter luck next time, "+name+"!\n"
        
    else:
        print "\nThat's what Luigi want's to hear, "+name+"!\n"

    time.sleep(1)

        