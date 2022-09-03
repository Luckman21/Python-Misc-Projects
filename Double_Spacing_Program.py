'''
Created on May 26, 2017

@author: Luqmaan
'''
total = 0
first = 0
last = 250

text = raw_input ("Paste your text here: ")
print

while total < len(text):
    print text[first:last]
    print 
    first = last
    
    if last+250 > len(text):
        num = len(text)-first
        last+=num+1
        print text[first:last]
        print
        break 
    
    else:
        last+=250
    
    