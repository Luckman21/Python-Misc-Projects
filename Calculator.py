'''
Created on Mar 27, 2017

@author: Luqmaan
'''
''''
print "choose your operation"
print "Addition = 1"
print "Subtraction = 2"
print "Multiplication = 3"
print "Division = 4"
oper = input (":")

num1 = input ("Please enter your first number you would like to calculate: ")

num2 = input ("please enter your second number you would like to calculate: ")

if oper == 1:
    print num1 + num2

elif oper == 2:
    print num1 - num2    

elif oper == 3:
    print num1 * num2

elif oper == 4:
    print num1 / num2
    
else:
    print "operation choice invalid"
'''

while True:
    
    print "Input \"0\" to end"
    qst = input ("Enter your math equation: ")
    
    if qst == 0:
        break
    
    print float(qst)
    