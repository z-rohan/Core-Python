s="Python is very very easy"
print(s)
li=s.split()
print(li)

li.append("Language")
print(li)

s=""
for i in li:
    s+=i
    s+=" "
print(s)

li.insert(2,"a")
print(li)

no=[1,3,2,4,7,5,6,7,8,7,9]
print(no)

no.remove(7)
print(no)

no.pop()
print(no)

no.pop(3)
print(no)

no.reverse()
print(no)

