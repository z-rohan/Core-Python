'''
def outer(n):
    def inner(a):
        print('---Welcome---')
        n(a)
        print('---bye bye---')
    return inner 


@outer
def fun(a):
    print(f'Hello {a}')

fun('Surabhi')
'''
'''
def check(n):
    def inner(a,b):
        if b==0:
            print('you cant divide by zero')
        else:
            return n(a,b)
    return inner

@check
def div(a,b):
    return a/b

print(div(10,0))
'''
#without return statement
'''
def check(n):
    def inner(a,b):
        if b==0:
            print('you cant divide by zero')
        else:
            n(a,b)
    return inner

@check
def div(a,b):
    print(a/b)

div(10,5)
'''

'''
def discount(n):
    def inner(a):
        b=int(input('enter how much discount you want to give'))
        t=(1-b/100)*a
        return f'total discounted bill is {t}'
    return inner

@discount
def total(n):
    return f'total bill is {n}'

print(total(1000))
'''

#tried by myself(error)
'''
def discount(n):
    def inner(a):
        if a>500:
            print('disount is 5%')
            print(f'total bill is {0.95*a}')
        else:
            total(a)

    return inner

@discount
def total(n):
    print (f'total bill is {n}')

total(400)
'''











































