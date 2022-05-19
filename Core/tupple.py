class student:
    def __init__(self,r,n):
        self.rollno=r
        self.name=n

    def __str__(self):
        return "Roll number:-{} and Name:-{}".format(self.rollno,self.name)

s1=student(1,"xyz")
s2=student(2,"pqr")

t=(s1,s2)

for stu in t:
    print(stu)


t1=(1,2,3)
t2=("a","b","c")

list1=[t1,t2]

for i in list1:
    for j in i:
        print(j)

t3=(1,2,3,"a","b",4)
print(len(t3))
#print(min(t3)) # error
#print(max(t3)) #error
print(min(t2))
print(max(t2))
print(sum(t1))
#print(sum(t2)) #error

t4=(10,20,30,10,40,50,10,50,30)
print(t4.count(10))
print(t4.index(10))
t5=sorted(t4)
print(t5)
t6=sorted(t5,reverse=True)
print(t6)

t7=t1+t2
print(t7)
t8=t1*2
print(t8)









