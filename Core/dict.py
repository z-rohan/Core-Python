'''
d={5:"java",10:"python",15:"spring"}
print(d)

print(d[5])
print(d.get(10))# method to access values

d1=dict()

d1[5]="aaa"
d1[10]="bbb"
print(d1)


d={5:"java",10:"python",15:"spring"}
for key in d.keys():
    print(key)

for val in d.values():
    print(val)
    
for key,val in d.items():
    print(key)
    print(val)
    


d={5:"java",10:"python",15:"spring"}
del d[10]
print(d)

d[30]="html"
print(d)

#del d
#print(d)

d.clear()
print(d)


d={5:"java",10:"python",15:"spring"}
t=d.pop(10)     #return in tupple format
print(d)
print(t)


d={5:"java",10:"python",15:"spring"}
d.popitem()
print(d)
'''

class student():
    def __init__(self,r,n):
        self.rollno=r
        self.name=n

    def __str__(self):
        return "Roll number is {} and name is {}".format(self.rollno,self.name)

l1=[]    
s1=student(1,"xyz")
l1.append(s1)
s2=student(2,"pqr")
l1.append(s2)

l2=[]
s3=student(3,"abc")
l2.append(s3)
s4=student(4,"def")
l2.append(s4)

d={"MCA1":l1,"MCA2":l2}

for key,valuelist in d.items():
    print(key)
    for stu in valuelist:
        print(stu)




































