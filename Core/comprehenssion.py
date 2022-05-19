oldLi=[1,2,3,4,5,6,7,8,9,10]

sqLi=[i*i for i in oldLi]
print(sqLi)

sqSet={i*i for i in oldLi}
print(sqSet)

sqDict={i:i*i for i in oldLi}
print(sqDict)

eoLi=['Even' if i%2==0 else 'Odd' for i in oldLi]
print(eoLi)

evenLi=[i for i in oldLi if i%2==0]
print(evenLi)

eoDict={i:'Even' if i%2==0 else 'Odd' for i in oldLi}
print(eoDict)


sqset=set()
for i in oldLi:
    sqset.add(i*i)

print(sqset)














