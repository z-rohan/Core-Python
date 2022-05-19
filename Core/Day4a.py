'''
x=10
def m1():
	print(x)
m1()
'''

'''
x=10
def m1():
	x=x+2   #UnboundLocalError: local variable 'x' referenced before assignment
	print(x)
m1()
'''

'''
x=10
def m1():
	global x
	x=x+2
	print(x)
m1()
'''


x=10
print(x)
def m1():
	x=20
	print(x)
	print(globals()['x'])
m1()

