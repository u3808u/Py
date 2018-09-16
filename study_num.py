#study_num.py

a = 80
b = 75
c = 55

d = (a + b + c)/3
print("average : ", d)

a = 17 // 3
print("17 // 3 : ", a)

a = 17 % 3
print("17 % 3 : ", a)

a = 17
if a%2 == 1:
    print("a = odd")
else:
    print("a = even")

while 1:
	name = "suji"
	i = input("what is your name? : ")
	if i == name:
		print("hello,"  + name)
		break;
	else:
		print("it is not your name!")
		continue;
print("bye!")
