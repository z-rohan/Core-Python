
mh=['Pune','Nagpur','Mumbai']
jh=['Ranchi','Lohardaga']
India=[mh,jh]

for x in India:
    for city in x:
        print(city)
l=[4,3,5,6,2,1]
l.sort(reverse=True)
print(l)

#sorting objects
'''
class student:
    def __init__(self,rollno,name):
        self.rollno=rollno
        self.name=name
    def __str__(self):
        return "Roll Number:-{} and Name:-{}".format(self.rollno,self.name)

s1=student(101,"Rohan")
s2=student(103,"Zade")
s3=student(102,"Khushal")

l=[s1,s2,s3]

def r_no(obj):
    return obj.rollno

def name(obj):
    return obj.name

for stu in l:
    print(stu)
print("----"*20)
l.sort(key=r_no)
for stu in l:
    print(stu)
'''
#sorting objects with attrgetter
'''
from operator import attrgetter
class student:
    def __init__(self,rollno,name):
        self.rollno=rollno
        self.name=name
    def __str__(self):
        return "Roll Number:-{} and Name:-{}".format(self.rollno,self.name)

s1=student(101,"Rohan")
s2=student(103,"Zade")
s3=student(102,"Khushal")

l=[s1,s2,s3]

for stu in l:
    print(stu)
print("----"*20)
l.sort(key=attrgetter('rollno'))
for stu in l:
    print(stu)
'''
#sorting objects with lambda function

'''
class student:
    def __init__(self,rollno,name):
        self.rollno=rollno
        self.name=name
    def __str__(self):
        return "Roll Number:-{} and Name:-{}".format(self.rollno,self.name)

s1=student(101,"Rohan")
s2=student(103,"Zade")
s3=student(102,"Khushal")

l=[s1,s2,s3]

for stu in l:
    print(stu)
print("----"*20)
l.sort(key=lambda x:x.rollno)
for stu in l:
    print(stu)
'''






















