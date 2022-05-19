s={1,2,3,4,5,6,7,8,9,2,2,2,'fd',False,90.8}
print(s)
s.add(10)
print(s)
s.remove(3)
print(s)
s.discard(5)
print(s)
s.pop()
print(s)


s1={10,20,30,40,50}
s2={40,50,60,70,80,90,100}

print(s1|s2)
print(s1.union(s2))
print(s1&s2)
print(s2.intersection(s1))
print(s1-s2)
print(s2-s1)
