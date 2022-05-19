
#Operator overloading
'''
class book:
    def __init__(self,p):
        self.pages=p

    def __str__(self):
        return f"Number of pages={self.pages}"

    def __add__(self,other):
        pages=self.pages+other.pages
        return book(pages)

b1=book(200)
b2=book(300)
b3=book(500)

print(b1+b2)
print((b1+b2)+b3)
print(b1+b2+b3)
'''
#Duck typing
'''
class MySQL:
    def commit(self):
        print("MySQL database is commited")

    def rollback(self):
        print("MySQL database is rollbacked")

class oracle:
    def commit(self):
        print("Oracle database is commited")

    def rollback(self):
        print("Oracle database is rollbacked")

def common_interface(obj):
    obj.rollback()
    obj.commit()
    
m=MySQL()
o=oracle()

comman_interface(o)
'''

