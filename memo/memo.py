# -*- coding: utf-8 -*-
# ~/Py/memo/memo.py

import sys
import os
import shutil

while True: 
	print("<This is notepad>")
	print("1. start")
	print("2. exit")
	choice = input("choice : ")
	if choice == '1':
		while True:
			memo = input('input text(if you want exit, input "exit") : ')
			if memo == 'exit':
				break;
			f = open('./notepad.txt', 'a')
			f.write(memo + '\n')
			f.close()
			f = open('./notepad.txt', 'r')
			text = f.read()
			print(text)
			for a in f:
				text = f.read()
				print(text)
			f.close()	
	elif choice == '2':
		shutil.move('./notepad.txt', './notepad.prev.txt')
		print('notepad.txt -> notepad.prev.txt')
		f = open('./notepad.prev.txt')
		text = f.read()
		print(text)
		for a in f:
			text = f.read()
			print(text)
		f.close()
		break
	else:
		break
