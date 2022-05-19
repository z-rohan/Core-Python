'''
class parent:
    x=10

class another(parent):
    y=20

class child1(another):
    pass

class child2(child1):
    pass

another_obj=another()
parent_obj=parent()
ch1=child1()
ch2=child2()

print(isinstance(another_obj,another))
print(isinstance(another_obj,parent))
print(isinstance(parent_obj,another))
print(isinstance(parent_obj,parent))
print(isinstance(ch2,child2))
print(isinstance(ch2,child1))
print(isinstance(ch2,object))

print("-"*20)

print(issubclass(another,parent))
print(issubclass(parent,another))
print(issubclass(parent,object))
print(issubclass(another,object))
'''
'''
class parent:
    def m1(self):
        print("m1-->parent")

class child:
    def m2(self):
        print("m2-->child")
        parent.m1(self)#will work irrespective of inheritance 

ch=child()
ch.m2()

class child2(parent):
    def m3(self):
        print("m3-->child2")
        super().m1() # inheritance is requiered

ch2=child2()
ch2.m3()
'''


#person-name,age,gender
#student-name,age,gender,rn,marks
#teacher-name,age,gender,exp,salary

'''
class person:
    def __init__(self,n,a,g):
        self.name=n
        self.age=a
        self.gender=g

    def __str__(self):
        return f"Name:{self.name},Age:{self.age},Gender:{self.gender}"

class student(person):
    def __init__(self,n,a,g,r,m):
        super().__init__(n,a,g)
        self.rollno=r
        self.marks=m

    def __str__(self):
        print(super().__str__(),end=',')
        return f"Roll No:{self.rollno},Marks:{self.marks}"


s=student("ajay",32,"male",101,95.66)
print(s)
'''






























































