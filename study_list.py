#study_list.py

import string

a = [1, [2,3], [4,5,6]]
print(a[-2])

#1
a = ['Life', 'is', 'too', 'short', 'you', 'need', 'python']
print("%s %s"%(a[4], a[2]))

#2
a = ['Life', 'is', 'too', 'short']
print("%s"%" ".join(a))

#3
a = [1,2,3]
print("a length : %d"%len(a))

#4
a = [1,2,3]
b = a.append([4,5])
c = a.extend([4,5])
print("a append 4,5 : ")
print(b)
print("a extend 4,5 : ")
print(c)

