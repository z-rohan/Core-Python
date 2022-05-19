#syntax: fun_obj=lambda arg:expression

print((lambda a,b:a+b)(10,20))

print((lambda n,:n*n)(10))

#filter_obj=filter(function,seq)
#map_obj=map(funcion,seq)
#reduce_obj=reduce(funcion,seq)


marks=[10,20,30,40,50,60,70,80,90,100]
from functools import reduce

def failed_fun(m):
    if m<40:
        return m

#failed_list=list(filter(failed_fun, marks))
failed_list=list(filter(lambda m:m<40,marks))
print(failed_list)


def newmarks(m):
    return m+5

#new_marks=list(map(newmarks,marks))
new_marks=list(map(lambda m:m+5,marks))
print(new_marks)

def addmarks(a,b):
    return a+b

#total=reduce(addmarks,marks)
total=reduce(lambda a,b:a+b,marks)
print(total)


