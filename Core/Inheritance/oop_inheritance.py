'''
class person:
    name=''
    age=0
    gender=''                           

    def setName(self,n):
        self.name=n
    def setAge(self,a):
        self.age=a
    def setGender(self,g):
        self.gender=g

    def getName(self):
        return self.name
    def getAge(self):
        return self.age
    def getGender(self):
        return self.gender

class student(person):
    rollno=0
    marks=0.0
    
    def setRollno(self,r):
        self.rollno=r
    def getRollno(self):
        return self.rollno

    def setMarks(self,r):
        self.marks=r
    def getMarks(self):
        return self.marks

s=student()

s.setName('Raj')
s.setAge(30)
s.setGender('M')
s.setRollno(101)
s.setMarks(97)

print(s.getName())
print(s.getAge())
print(s.getGender())
print(s.getRollno())
print(s.getMarks())
'''
'''
class parent:
    money=1000
    def m1(self):
        print("m1-parent")

class child(parent):
    flat='3BHK'
    def m2(self):
        print("m2-child")


p=parent()
c=child()

print(p.money)
c.money=2000
print(c.money)
print(p.money)

c.m1()
c.m2()
'''
