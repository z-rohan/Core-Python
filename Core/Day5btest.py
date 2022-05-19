from Day5bcalculator import *

print("----select-----\n"\
	"1.Addition\n"\
	"2.Substraction\n"\
	"3.Multiplication\n"\
	"4.Division\n"\
	"5.Exit")

while True:
	x=int(input("Enter 1st number"))
	y=int(input("Enter 2nd number"))
	ch=int(input("Enter choice"))

	if ch==1:
		addition(x,y) 

	elif ch==2:
		substraction(x,y)

	elif ch==3:
		multiplication(x,y)

	elif ch==4:
		division(x,y)

	elif ch==5:
		break

	else: 
		print("wrong choice")
        	   	
