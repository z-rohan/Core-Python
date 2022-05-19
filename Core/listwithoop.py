class student:
    sid=0
    sname=""

    def __init__(self,sid,sname):
        self.sid=sid
        self.sname=sname

    def __str__(self):
        return "Student ID:-{}\n"\
               "student name:-{}\n".format(self.sid,self.sname)


s=student(101,"Rohan")
s1=student(102,"Khushal")

l1=[s,s1]
#print(id(s1))
for stu in l1:
    print(stu)
    #print(id(stu))

