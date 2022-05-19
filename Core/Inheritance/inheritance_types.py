
#single inheritance
'''
class parent:
    x=5

class child(parent):
    x=10

ch=child()
print(ch.x)
'''
#IMP
#Multiple inheritance
'''
class parent1:
    x=10

class parent2:
    y=20
    x=100

class child(parent1,parent2):
    z=30

ch=child()
print(ch.x)
print(ch.y)
'''


#Multilevel Inheritance
'''
class A:
    x=5
class B(A):
    x=10
class C(B):
    pass
class D(C):
    pass
d=D()
print(d.x)
'''

#Hierarchial inheritance
'''
class parent:
    a=2
class child1(parent):
    b=3
class child2(parent):
    c=4

ch1=child1()
ch2=child2()

print(ch1.a)
print(ch1.b)
#print(ch1.c)
print(ch2.a)
#print(ch2.b)
print(ch2.c)
'''

