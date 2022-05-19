'''
class SEQ:
    def __init__(self,s,e):
        self.start=s
        self.end=e

    def __iter__(self):
        print("this is iter method")
        return self     #returns iterator object

    def __next__(self):
        print("This is next method")
        n=self.start
        self.start+=1
        if self.start<=self.end:
            return n
        raise StopIteration("Sequence Exausted")

s=SEQ(0,100)

for i in s:
    print(i)
'''

''' 
class EVEN:
    def __init__(self,s,e):
        self.start=s
        self.end=e

    def __iter__(self):
        return self

    def __next__(self):
        n=self.start
        self.start+=2
        if self.start<=self.end:
            return n
        raise StopIteration("Even Numbers ended")

e=EVEN(0,10)

for i in e:
    print(i)
'''
'''
class EVEN:
    def __init__(self,s,e):
        self.start=s
        self.end=e

    def __iter__(self):
        return self

    def __next__(self):
        n=self.start
        if self.start<=self.end:
            if self.start%2==0:
                self.start+=2
                return n
            else:
                self.start+=1
                return n+1
        else: 
            raise StopIteration("Even Numbers ended")
        

e=EVEN(1,10)

for i in e:
    print(i)
'''
