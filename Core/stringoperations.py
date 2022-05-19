s="python"
print(s.capitalize())#Python

print(s.upper())#PYTHON

s1="PUNE"
print(s1.lower())#pune

print(s1.center(50))#                       PUNE                       
print("Pune".center(20,'*'))#********Pune********

msg="Python is popular programming language"
print(msg.title())#Python Is Popular Programming Language

print(msg.count('p'))#3
print(msg.count('p',10,18))#2

print(msg.endswith('language'))#True    
print(msg.startswith('Python'))#True
print(msg.find('is'))#7 return index

msg1="pYtHoN python PYTHON Python"
print(msg1.swapcase())#PyThOn PYTHON python pYTHON

print(msg.split(' '))#['Python', 'is', 'popular', 'programming', 'language']

msg2="Python-Java-PHP/.net/React"
print(msg2.split('-'))#['Python', 'Java', 'PHP/.net/React']
print(msg2.split('/'))#['Python-Java-PHP', '.net', 'React']
print('-'*40)
lang=msg2.split('-')
print(lang)         #['Python', 'Java', 'PHP/.net/React']
print(lang[2].split('/'))#['PHP', '.net', 'React']

msg3=msg2.replace('-'," ")
msg4=msg3.replace('/'," ")

print(msg4.split(' '))#['Python', 'Java', 'PHP', '.net', 'React']
