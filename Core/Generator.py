'''
def seq():
    print('Generator starts----------')
    for i in range(0,100):
        yield i
    print('Generator Ends------------')

gen=seq()

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print("---------FOR-------------")

for j in gen:
    print(j)
'''
'''
def fun1():
    print('Generator starts---------------')
    yield 10
    print('In middle of Generator')
    yield 20
    print('Gerator ends---------------')

gen=fun1()

print(gen.__next__())
print(next(gen))
#print(next(gen)) # this will execute generator ends print command but error will be genrated

for i in gen:
    print(i) # this will execute geneartor  ends print commmand without error
'''
'''
def odd():
    print('Generator starts----------')
    for i in range(1,101):
        if i%2!=0:
            yield i
    print('Generator ends-------------')

for i in odd():
    print(i)
print('-------------------------------')
for i in odd():# here gen can be excuted repeatedly 
    print(i)

gen=odd()

for i in gen:
    print(i)
print('-------------------------------')
for i in gen:#here gen cant be executed 
    print(i)
'''
'''
def even():
    for i in range(0,100):
        if i%2==0:
            yield i
for i in even():
    print(i)
'''
