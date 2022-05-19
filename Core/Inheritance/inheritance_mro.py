'''
class calculator:
    def add(self,a,b):
        return a+b

    def sub(self,a,b):
        return a-b

    def mul(self,a,b):
        return a*b

    def div(self,a,b):
        return a/b

class advcalculator(calculator):
    def avg(self,a,b):
        total=super().add(a,b)
        return super().div(total,2)

a=advcalculator()
print(a.avg(10,20))
'''
"""
class A:
    pass
class B(A):
    pass
class C(A):
    pass
class D(B,C):
    pass

print(D.mro()) #method resolution order
"""
