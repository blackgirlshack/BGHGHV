from easygui import *

g = open('reveal.txt', 'r')
flag = g.read()


msg = "Do you want to continue to reveal the flag?"
title = "Please Confirm"

if ccbox(msg, title):     # show a Continue/Cancel dialog
    msgbox("The flag is: ") # add the missing part 
else:  # user chose Cancel
    exit()

g.close()