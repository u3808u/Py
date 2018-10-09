#main.py

from Manager import manager
from Consumer import consumer
import string

login = 0

def main():
	while True:
		print("<BMK Library Login>")
		print("1. Manager")
		print("2. Consumer")
		print("3. Make account")
		print("4. Remove account")
		print("5. Exit")
		menu = raw_input("Select number : ")
		if menu == 1:
		    account = raw_input("Input your ID : ")
		    passwd = raw_input("Input your PW : ")
		    mf = open("./Manager/login.txt", 'r')
		    content_id = mf.read()
			if not content_id:
				print("No manager account exist. Make account.\n")
				continue
			content_pw = mf.read()
			if account == content_id and passwd == content_pw:
				mf.close()
				login = 1
				man = manager_obj()
		    else:
				for i in mf:
					content_id = mf.read()
				    content_pw = mf.read()
					if account == content_id and passwd == content_pw:
						mf.close()
						login = 1
						man = manager_obj()
					break
		elif menu == 2:
			account = raw_input("Input your ID : ")
		    passwd = raw_input("Input your PW : ")
		    cf = open("./Consumer/login.txt", 'r')
			content_id = mf.read()
		    if not content_id:
				print("No consumer account exist. Make account.\n")
				continue
			content_pw = cf.read()
		    if account == content_id and passwd == content_pw:
				cf.close()
				login = 1
				con = consumer_obj()
		    else:
				for j in mf:
					content_id = cf.read()
				    content_pw = cf.read()
				    if account == content_id and passwd == content_pw:
						cf.close()
						login = 1
						con = consumer_obj()
						break
		elif menu == 3:
		    while True:
			print("< Make your account >")
			print("1. Manager")
			print("2. Consumer")
			print("3. exit")
			choice = raw_input("Select number : ")
			if choice == 1:
			    account = raw_input("Input new manager account ID : ")
			    passwd = raw_input("Input new manager account PW : ")
			    mf = open("./Manager/login.txt", 'a')
			    mf.write(account)
			    mf.write(passwd)
			    mf.close()
			    print("New manager acccount is created.\n")
			    continue
			elif choice == 2:
			    account = raw_input("Input new consumer account ID : ")
			    passwd = raw_input("Input new consumer account PW : ")
			    cf = open("./Consumer/login.txt", 'a')
			    cf.write(account)
			    cf.write(passwd)
			    cf.close()
			    print("New Consumer account is created.\n")
			    continue
			elif choice == 3:
			    print("Stop creating account\n")
			    break
			else:
			    print("Wrong number input.\n")
			    continue
		elif menu == 4:
		    while True:
				print("< Remove your account >")
				print("1. Manager")
				print("2. Consumer")
				print("3. exit")
				choice = raw_input("Select number : ")
				if choice == 1:
				    account = raw_input("Input account ID you wanna remove : ")
				    passwd = raw_input("Input account PW you wanna remove : ")
				    mf  = open("./Manager/login.txt", 'r+')
				    content_id = mf.read()
				    content_pw = mf.read()
				    if account == content_id and passwd == content_pw:
						content_id = content_id.replace(account,"",1)
						content_pw = content_pw.replace(passwd,"",1)
						print("Removing manager account succeed.\n")
						break
					for k in mf:
						content_id = mf.read()
						content_pw = mf.read()
						if account == content_id and passwd == content_pw:
						    content_id = content_id.replace(account,"",1)
						    content_pw = content_pw.replace(passwd,"",1)
						    print("Removing manager account succeed.\n")
						    break
						else:
						    continue
				elif choice == 2:
				    account = raw_input("Input account ID you wanna remove : ")
				    passwd = raw_input("Input account PW you wanna remove : ")
				    cf = open("./Consumer/login.txt", 'r+')
				    content_id = cf.read()
				    content_pw = cf.read()
				    if account == content_id and passwd == content_pw:
						content_id = content_id.replace(account,"",1)
						content_pw = content_pw.replace(passwd,"",1)
						print("Removing consumer account succeed.\n")
						break
				    for l in cf:
						content_id = cf.read()
						content_pw = cf.read()
						if account == content_id and passwd == content_pw:
						    content_id = content_id.replace(account,"",1)
						    content_pw = content_pw.replace(passwd,"",1)
						    print("Removing consumer account succeed.\n")
						    break
						else:
						    continue
				elif choice == 3:
				    print("Stop removing account.\n")
				    break
				else:
				    print("Wrong number input. Try again.\n")
				    continue	    
		elif menu == 5:
			print("Library management exit.")
		    break
		else:
		    print("Wrong number input. Try again.\n")
		    continue
	return

main()
