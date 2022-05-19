'''
print('----Program starts----')
try:
    x=int(input('Enter first number'))
    y=int(input('Enter second number'))

    div=x/y

    print('Output is ',div)

except ZeroDivisionError as msg:
    print('Cant divide by zero',msg)
except ValueError as msg:
    print('Eception has occured',msg)

    
print('----Program ends----')
'''
'''
print('---Program starts---')
try:
    def add(a,b):
        result=a+b
        print('Addition is ',result)
        
    add(10,'cjc')
except TypeError as msg:
    print('Type error has occured...',msg)
    
print('---Program ends---')
'''
