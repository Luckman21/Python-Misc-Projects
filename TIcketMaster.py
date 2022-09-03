'''
Created on May 2, 2017

@author: Luqmaan
'''
import time

print "Welcome to \"Ticketmaster.com\"!\n"
time.sleep(1)                  
age = input ("How old are you? (Enter your age): ")         #age, stu, sci and imax are all variables.  Making 1 = yes and 2 = no makes it 
time.sleep(1)
stu = input ("\nAre you a student?\n\n1 - Yes\n2 - No\n: ") #easier to use for if elif and else and creates to possible answers, whereas using 
time.sleep(1)
sci = input ("\nAre you going to the Science Center?\n\n1 - Yes\n2 - No\n: ")#string takes longer and people could mean different things like ya or oui
time.sleep(1)
imax = input ("\nAre you going to the IMAX Theater?\n\n1 - Yes\n2 - No\n: ")#instead of yes.  The time.sleep(x) is to give time in between questions and makes output print look better and easier to read.
time.sleep(1)
print

if stu == 1: #student comes up first to check if student because student offers a bigger discount than general adult ticket
    
    if age >= 3 and age <= 12: #child comes up because child rates are lower and some children are in school and would qualify as students.
        
        if sci == 1 and imax == 1:
            print "Because you are a child, your rate is the same as the student discount."
            time.sleep(1)
            print "Because you are going to both the Science Center and IMAX Theater, you qualify for the special discount combo."
            time.sleep(1)
            print "Your total price is $22 (saved $3!)."
            
        elif sci == 1:
            print "Because you are a child, your rate is the same as the student discount."
            time.sleep(1)
            print "Your total price is $16."
            
        elif imax == 1:
            print "Because you are a child, your rate is the same as the student discount."
            time.sleep(1)
            print "Your total price is $9."
            
        else:
            print "Are you even going here???"
        
    elif age > 12: #They are not young enough to fall under child rates, but still a student so they get better rates than general admission
        
        if sci == 1 and imax == 1:
            print "Because you are a student, you get a special discount which is lower than general rates."
            time.sleep(1)
            print "Because you are going to both the Science Center and IMAX Theater, you qualify for the special discount combo."
            time.sleep(1)
            print "Your total price is $22 (saved $3!)."
            
        elif sci == 1:
            print "Because you are a student, you get a special discount which is lower than general rates."
            time.sleep(1)
            print "Your total price is $16."
            
        elif imax == 1:
            print "Because you are a student, you get a special discount which is lower than general rates."
            time.sleep(1)
            print "Your total price is $9."
        
        else:
            print "Are you even going here???"
        
    else: #Just in case they go to preschool and they count that as school
        print "Because you are an infant, you are FREE!"
        
elif age <= 2:
    print "Because you are an infant, you are FREE!"
    
elif age >= 18 and age <= 64:
    
    if sci == 1 and imax == 1:
        print "Because you are an adult and are not in any specialized class, you have to pay general rates."
        time.sleep(1)
        print "Because you are going to both the Science Center and IMAX Theater, you qualify for the special discount combo."
        time.sleep(1)
        print "Your total price is $28 (saved $7!)."
            
    elif sci == 1:
        print "Because you are an adult and are not in any specialized class, you have to pay general rates."
        time.sleep(1)
        print "Your total price is $22."
        
    elif imax == 1:
        print "Because you are an adult and are not in any specialized class, you have to pay general rates."
        time.sleep(1)
        print "Your total price is $13."
    
    else:
        print "Are you even going here???"

elif age > 64:
    
    if sci == 1 and imax == 1:
        print "Because you are a senior, you pay lower than general rates."
        time.sleep(1)
        print "Because you are going to both the Science Center and IMAX Theater, you qualify for the special discount combo."
        time.sleep(1)
        print "Your total price is $22 (saved $3!)."
        
    elif sci == 1:
        print "Because you are a senior, you pay lower than general rates."
        time.sleep(1)
        print "Your total price is $16."
        
    elif imax == 1:
        print "Because you are a senior, you pay lower than general rates."
        time.sleep(1)
        print "Your total price is $9."
    
    else:
        print "Are you even going here???"

elif age >= 13 and age <= 17:
    
    if sci == 1 and imax == 1:
        print "Because you are a youth you pay lower than general rates."
        time.sleep(1)
        print "Because you are going to both the Science Center and IMAX Theater, you qualify for the special discount combo."
        time.sleep(1)
        print "Your total price is $22 (saved $3!)."
        
    elif sci == 1:
        print "Because you are a youth you pay lower than general rates."
        time.sleep(1)
        print "Your total price is $16."
        
    elif imax == 1:
        print "Because you are a youth you pay lower than general rates."
        time.sleep(1)
        print "Your total price is $9."
    
    else:
        print "Are you even going here???"
    
elif age >= 3 and age <= 12: 
    
    if sci == 1 and imax == 1:
        print "Because you are a child, your rate is the same as the student discount."
        time.sleep(1)
        print "Because you are going to both the Science Center and IMAX Theater, you qualify for the special discount combo."
        time.sleep(1)
        print "Your total price is $22 (saved $3!)."
        
    elif sci == 1:
        print "Because you are a child, your rate is the same as the student discount."
        time.sleep(1)
        print "Your total price is $16."
        
    elif imax == 1:
        print "Because you are a child, your rate is the same as the student discount."
        time.sleep(1)
        print "Your total price is $9."
        
    else:
        print "Are you even going here???"
        

else:
    print "HOW OLD ARE YOU???  "+str(age)+" is not even an actual age..."
     
time.sleep(1)   
print "Have a good day!"
        