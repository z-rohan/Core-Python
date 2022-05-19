#main thread
'''
from threading import current_thread

print('----Program Starts----',current_thread().name)

def evens():
    for i in range(0,10,2):
        print(i)
def odds():
    for i in range(1,10,2):
         print(i)
evens()
odds()

print('----Program Ends----',current_thread().name)# this is throwing a warning
'''

#creating threads
'''
from threading import current_thread,Thread

def evens():
    for i in range(0,10,2):
        print(i,current_thread().name)
def odds():
    for i in range(1,10,2):
         print(i,current_thread().name)

t1=Thread(target=evens)
t2=Thread(target=odds)
t1.start()
t2.start()
'''

#with parameters
'''
from threading import current_thread,Thread

def evens(start,end,step):
    for i in range(start,end,step):
        print(i,current_thread().name)
def odds(start,end,step):
    for i in range(start,end,step):
         print(i,current_thread().name)
         
print('---Program start---',current_thread().name)
t1=Thread(target=evens,args=(0,10,2),name='Evens ')
t2=Thread(target=odds,args=(1,10,2),name='Odds')
t1.start()
t2.start()
print('---Program ends---',current_thread().name)
'''
#Lock

from threading import current_thread,Thread,Lock
lock=Lock()
print('----Program starts----',current_thread().name)
def evens(start,end,step):
    lock.acquire()
    for i in range(start,end,step):
        print(i,current_thread().name)
    lock.release()
def odds(start,end,step):
    lock.acquire()
    for i in range(start,end,step):
         print(i,current_thread().name)
    lock.release()
t1=Thread(target=evens,args=(0,10,2),name='Evens ')
t2=Thread(target=odds,args=(1,10,2),name='Odds')
t1.start()
t2.start()

print('----Program ends----',current_thread().name)

