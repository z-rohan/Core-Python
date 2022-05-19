class student:
    rn=0
    name=""
    marks=0.0

    def fun(self):
        print("Hello from fun",self)

    def add(self,a,b):
        print("Hello from add",a+b)

s1=student()
s2=student()

s1.rn=1
s1.name='abcd'
s1.marks=100
s2.rn=2
s2.name='xyz'
s2.marks=10

s1.fun()
s2.add(10,20)
s2.fun()
