from multipledispatch import dispatch
# dispatch is only use in case of overloading 

#overriding
'''
class parent:
    def add(self,a,b):
        print("add--->parent")
        print(a+b)

class child(parent):
    def add(self,a,b,c=0):
        print("add--->child")
        print(a+b+c)

ch=child()
ch.add(10,20)
p=parent()
p.add(10,30)
ch.add(10,20,30)
'''


#Overloading

'''
class calculator:
    @dispatch(int,int)
    def add(self,a,b):
        print('add with 2 int called')
        print(a+b)

    @dispatch(int,int,int)
    def add(self,a,b,c):
        print('add with 3 int called')
        print(a+b+c)

    @dispatch(str,str)
    def add(self,a,b):
        print("Add with 2 strings")
        print(a+b)


c=calculator()
c.add(10,20)
c.add(10,20,30)
c.add("CJC","Pune")
'''

'''
def add(a,b,c=0):
    tot=a+b+c
    print(tot)

add(10,20)
add(10,20,30)
'''

