from abc import ABC,abstractmethod

class abstract(ABC):
    @abstractmethod
    def m1(self):
        pass
        
    def m2(self):
        print("m2--> abstract class")

#ab=abstract() #type error
#ab.m2()

class child(abstract):

    def m1(self):
        print("To overwrite m1 of abstract and prevent child class from becoming abstract class")

ch=child()
ch.m1()
ch.m2()
#ab=abstract()
#ab.m3()


class RBI(ABC):
    @abstractmethod
    def interest_rate(self):
        pass

    def new_guidelines(self):
        print("New guidelines")

#rbi=RBI()
#print(rbi)
class IDFC(RBI):

    def interest_rate(self):
        print("interest rate for IDFC class is 6%")
    def home_loan(self):
        print("interest rate for homeloan is 9%")

class SBI(RBI):

    def interest_rate(self):
        print("Interest rate for SBI is 2.7%")
    def personal_loan(self):
        print("interest rate for personal loan is 11%")

idfc=IDFC()
idfc.interest_rate()
idfc.home_loan()

print()

sbi=SBI()
sbi.interest_rate()
sbi.personal_loan()



