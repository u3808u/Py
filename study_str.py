#study_str.py
import string
#1
print('"jump to python"solve this problem')
#2
print("Life is too short,\nYou need Python");
#3
print('''
Life is too short
You need Python
''')
#4
a = "python"
print("python to upper : %30s"%a.upper())
a = ''
#5
b = "Life is too short, you need python"
print("short index : %d"%b.index("short"))
b = ''
#6
c = "a:b:c:d"
print("a:b:c:d to %s"%c.replace(':','#'))
c = ''
#7
d = "a:b:c:d"
d = d.split(":")
print ("#".join(d))
e = ''
d = ''
#8
f = "881120-1068234"
print(f[7])
f = ''
#9
g = "1980M1120"
tmp = g[4]
g = g[:4] + g[5:]
g = tmp + g
print(g)
