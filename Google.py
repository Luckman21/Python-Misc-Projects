'''
Created on May 6, 2017

@author: Luqmaan
'''
import webbrowser
import time

print "-"*30+"\n"
print "          GOOGLE.PY\n"
print "-"*30+"\n"
time.sleep(1)

while True:

    print "\nDo you want to enter a url or search something?\n\n1 - URL\n2 - Search"
    choose = raw_input (": ")
    
    if choose == "2":
            
        while True:
            
            print "\nTo quit, type \"google.py\".\n"
            time.sleep(0.5)
            url = raw_input ("Search something: ")
            
            if url.upper() == "GOOGLE.PY":
                break
            
            else:
                if url.count(" ") >= 1:
                    url = url.replace(" ","+")
                else:
                    True
                webbrowser.open_new_tab("https://www.google.ca/#q="+url)

    elif choose == "1":
            
        while True:
            
            print "\nTo quit, type \"google.py\".\n"
            time.sleep(0.5)
            url = raw_input ("Enter your URL here: ")
            
            if url.upper() == "GOOGLE.PY":
                break
            
            else:
                webbrowser.open_new_tab(url)

        
    elif choose == "":
        print "\nInvalid input.\n"
        
    else:
        print "\nInvalid input.\n"
