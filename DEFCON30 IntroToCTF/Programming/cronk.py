import time
import sys, os 

c=open('cronk2.txt', 'r')
flag=c.read()

for x in flag:
    os.system('clear')
    print(x, end="\r")
    time.sleep(5)
	
c.close()	
