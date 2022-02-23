#!/usr/bin/env python3
import sys, pyperclip

filepath="dane.txt"
f=open(filepath,"r")


PASSWORDS={'email':'F7minlBDDuvMJuxESSKHFhTxFtjVB6',
	   'netflix':'VmALvQyKAxiVH5G8v01if1MLZF3st',
	   'face':'kotek12345',
	   'jsos':'emacarane990'}

for line in f:
	x=line.strip('\n').split(':')
	PASSWORDS[x[0]]=x[1]
f.close()

if len(sys.argv) < 2:
	print('Uzycie: python pw.py [konto] - brakuje argumentu')
	sys.exit()

account=sys.argv[1]

if account in PASSWORDS:
	pyperclip.copy(PASSWORDS[account])
	print('Hasło do konta ' + account + ' zostało skopiowane do schowka.')
else:
	print('Nie istnieje konto o nazwie ' + account + '.')
	print('Chcesz dodac nowe haslo do tego konta?: (tak lub nie)')
	answer=input()
	if answer.isalpha() == True:
		if answer.lower() == 'tak':
			newAccount=sys.argv[1]
			print('Podaj haslo dla nowego konta: ')
			newPassword=input()
			PASSWORDS.setdefault(newAccount,newPassword)
			f=open(filepath,"w")
			PASSWORDS={k + ':' + v + "\n" for k,v in PASSWORDS.items()}
			f.writelines(PASSWORDS)
			f.close()
			print('Zaktaulizowano baze hasel')
		else:
			print('Konczymy dzialanie programu')
			sys.exit()
	else:
		print('Podano bledne dane.')
		sys.exit()
