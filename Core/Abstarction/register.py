from abc import ABC,abstractmethod

#indirect subclass

class A(ABC):
    @abstractmethod
    def m1(self):
        pass

    @abstractmethod
    def m2(self):
        pass

    def m3(self):
        print("This is m3 method of A")

class B:
    def m1(self):
        print("this is m1 method of B")

    #def m2(self):
        #print("This is m2 method of B")

A.register(B)
print(issubclass(B,A))
b=B()
b.m1()


#name magling
'''
class test:
    __a=10

    def m1(self):
        print("This is m1 method")
    def __m2(self):
        print("This is m2 method")

t1=test()
print(t1._test__a)
t1._test__m2()
'''

#use of super in abstraction
'''
class A(ABC):
    @abstractmethod
    def m1(self):
        print("this is m1 method of A class")

    @abstractmethod
    def m2(self):
        print("this is m2 method of A class")

    def m3(self):
        print("this is m3 method of A class")

class B(A):
    def m1(self):
        print("This is m1 method of B class")
        super().m1()
    def m2(self):
        print("this is m2 method of B class")
        
b1=B()
b1.m1()
b1.m2()
'''
# comman interface
'''
class connection(ABC):
    @abstractmethod
    def commit(self):
        pass

    @abstractmethod
    def rollback(self):
        pass

class oracle(connection):
    def commit(self):
        print("Commit----oracle class")

    def rollback(self):
        print("rollback----oracle class")

class mysql(connection):
    def commit(self):
        print("Commit----mysql class")

    def rollback(self):
        print("rollback----mysql class")


o=oracle()
s=mysql()

def comman_interface(obj):
    obj.commit()
    obj.rollback()

comman_interface(o)
comman_interface(s)
'''
