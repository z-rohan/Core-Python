'''
class A:
    def m1(self):
        print(self.x)

a1=A()
a1.x=100
a2=A()
a2.x=200

a1.m1()
a2.m1()


class A:
    def m1(self):
        print("m1----",id(self))

a=A()
a1=A()
print(id(a))
print(id(a1))

a.m1()
a1.m1()


class student:
    def display(self):
        print("Roll no:-", self.rollno)
        print("Name:-",self.name)

s=student()
s.rollno=101
s.name="aaa"

s1=student()
s1.rollno=102
s1.name="bbb"

s.display()
s1.display()


class student:
    def display(self):
        return "Roll No:-{} and name:-{}".format(self.rollno, self.name)

s=student()
s.rollno=101
s.name="aaa"

s1=student()
s1.rollno=102
s1.name="bbb"

print(s.display())
print(s1.display())
'''

class student:
    def __str__(self):
        return "Roll No:-{} and name:-{}".format(self.rollno, self.name)

s=student()
s.rollno=101
s.name="aaa"

s1=student()
s1.rollno=102
s1.name="bbb"

print(s)
print(s1)

































