'''
bal=5000

def deposit(amt):
	global bal
	bal=bal+amt

def withdrawal(amt):
	global bal
	bal=bal-amt

def bal_check():
	print("----balance----",bal)

'''

bal=5000

def deposit(amt,bal):
	bal=bal+amt
	return bal

def withdrawal(amt,bal):
	bal=bal-amt
	return bal

def bal_check(bal):
	print("----balance----",bal)