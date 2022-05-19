# Traditional Approach

li=[1,2,3,4,5,6,7,8,9,10]

Evens=[]
for i in li:
    if i%2==0:
        Evens.append(i)
print(Evens)

di={}
for i in li:
    k=i
    v=i*i
    di[k]=v
print(di)

sqrs=[]
for i in li:
    s=i*i
    sqrs.append(s)
print(sqrs)

#comprehenssion
'''
Types:
    1.List comprehenssion
    2.Set comprehesnsion
    3.Dictionary comprehenssion
    4.Generator comprehenssion
[New_seq]=[expression for i in old_seq]
[New_seq]=[expression for i in old_seq if cond]
[New_seq]=[expression1 if cond else expression2 for i in old_seq] 

'''
evens=[i for i in li if i%2==0]
print(evens)

di={i:'Even' if i%2==0 else 'Odd' for i in li}
print(di)

di1={1:'a',2:'b',3:'c',4:'d',5:'e'}

dic={v:k for k,v in di1.items()}
print(dic)

s={1,2,3,4,5}
s1={i*i for i in s}
print(s1)
























