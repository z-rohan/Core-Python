'''
print('---Program starts---')

try:
    result=20/0
    print('Division is :',result)

except ZeroDivisionError as e:
    print('Division error---',e)

except:
    print('Exception occured')

else:
    print('No exception occured')
finally: # executed in both senarios wheather a exception is happened or not
    print('----program ends----')
'''
#Exception propagation
    #here even though div is defined outside try but it will still be handled
    
'''
def div(a,b):
    result= a/b
    print('Division is :',result)

try:
    a=int(input('Enter first number'))
    b=int(input("Enter second number"))
    div(a,b)

except ZeroDivisionError as msg:
    print('division error exception occured')

'''
#Custome exception
'''
class VotingEligibility(BaseException):
    def __init__(self,msg):
        self.msg=msg
age=int(input('Enter your age :'))
if age<18:
    raise VotingEligibility('Not eligible to vote!!!')

else:
    print('Eligible to vote!!!')
'''  
#hadling custome exception
'''  
class VotingEligibility(BaseException):
    def __init__(self,msg):
        self.msg=msg
try:
    age=int(input('Enter your age :'))
    if age<18:
        raise VotingEligibility('Not eligible to vote!!!')

except VotingEligibility as e:
    print('Exception occured....',e)
else:
    print('Eligible to vote!!!')

print('---Program ends---')
'''
#changing the massage of error
'''
b=0
if b==0:
    raise ZeroDivisionError('Division can\'t be done')
else:
    print('Division is possible')
'''




