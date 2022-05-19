from threading import current_thread, Lock, Thread
#class inherited from THread class with run overwritten

'''
class evens(Thread):
    def run(self):
        for i in range(0,11,2):
            print(i)
e=evens()
e.start()           #calls run method
'''

#without run method
'''
class odd(Thread):
    def m1(self):
        for i in range(1,11,2):
            print(i)
o=odd()
t1=Thread(target=o.m1())
t1.start()
'''

#synchronising
'''
l=Lock()
def fun(msg):
    l.acquire()
    print('[')
    print(msg)
    print(']')
    l.release()
t1=Thread(target=fun,args=('Python',))# as its tupple with 1 element so , is required
t2=Thread(target=fun,args=('Java',))
t2.start()
t1.start()
'''
#what will be the output if only acquire is used without release

# even and odd in single class
'''
l=Lock()

class numbers(Thread):
    def __init__(self,startt,end,step):
        Thread.__init__(self)
        self.startt=startt
        self.end=end
        self.step=step

    def run(self):
        l.acquire()
        for i in range(self.startt,self.end,self.step):
            print(i,current_thread().name)
        l.release()

n1=numbers(0,10,2)
n2=numbers(1,11,2)
n1.setName('EVENS')
n2.setName('ODDS')
n1.start()
n2.start()
'''

#Alphabets in capital and small in reverse order
'''
l=Lock()
class alpha(Thread):
    def __init__(self,startt,end,step):
        Thread.__init__(self)
        self.startt=startt
        self.end=end
        self.step=step

    def run(self):
        l.acquire()
        for i in range(self.startt,self.end,self.step):
            print(chr(i),current_thread().name)
        l.release()

cap=alpha(65,91,1)
small_reverse=alpha(122,96,-1)
cap.name='CAPITAL'
small_reverse.name='SMALL'
cap.start()
small_reverse.start()
'''























