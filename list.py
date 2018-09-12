# list.py

import os
import sys

f = open("./list.txt", 'r')
s = f.readline()
print("under " + s + "--------------------\n", end='')
for s in f:
    print("=================================================================")
    print("under " + s + "--------------------\n", end='')
    com = s
    s = "ls " + com
    os.system(s)
f.close()
