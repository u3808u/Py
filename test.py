#test.py

a = [1,2,3]

b = [1,2,3]

if (a is b):
    print(True)
else:
    print('a id :',id(a)) 
    print('b id :',id(b))
