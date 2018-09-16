# list.py

import os
import sys

f = open("./list.txt", 'r')
s = f.readline()
p = "cp -f "
v = "test/*txt"
t = " /home/bmk/Py/test1"
print(p + v + t)
os.system(p + v + t)
f.close()
