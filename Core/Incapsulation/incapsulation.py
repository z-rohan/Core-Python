'''
class student:
    rno=101
    _name="Rakesh"
    __marks=85

    def m1(self):
        print("M1-->student")
    def _m2(self):
        print("M2-->student")
    def __m3(self):
        print("m3-->student")

s=student()
print(s.rno)
print(s._name)
#print(s.__marks)  #error

s.m1()
s._m2()
#s.__m3()
'''
'''
class student:
    __rno=0
    __name=""
    __marks=0.0

    def __init__(self,r,n,m):
        self.__rno=r
        self.__name=n
        self.__marks=m

    def __str__(self):
        return f"Roll No:{self.__rno}, Name:{self.__name},Marks:{self.__marks}"

s=student(101,"Rakesh",98)
print(s)
'''
'''
class student:
    __rno=0
    __name=""
    __marks=0.0

    def setRno(self,r):
        self.__rno=r
    def setName(self,r):
        self.__name=r
    def setMarks(self,r):
        self.__marks=r
    def getRno(self):
        return self.__rno
    def getName(self):
        return self.__name
    def getMarks(self):
        return self.__marks

s=student()
s.setRno(101)
s.setName("Ravi")
s.setMarks(98)
print(s.getRno())
print(s.getName())
print(s.getMarks())
'''

#Name Mangling (Not a legal way)
#Syntex: print(objectname._classname__variablename)
            #objectname._classname__methodname()
'''
class parent:
    __a=10
    def m1(self):
        print("This is m1 method")
    def __m2(self):
        print("This is m2 private method")

p1=parent()
p1.m1()
print(p1._parent__a)
p1._parent__m2()
'''
'''
class parent:
    __a=10
    def m1(self):
        print("This is m1 method")
        self.__m2()
        print(self.__a)
    def __m2(self):
        print("This is m2 private method")

p1=parent()
p1.m1()
'''





























