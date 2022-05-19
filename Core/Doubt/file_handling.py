#file path: you have to give path in open command
#filepath:folderpath\filename.extension
#use \\ or / if unicode error appears

#creating new file 
'''
fh=open('chani.txt','x')#creating a text file
fh.close()
'''
#reading the file 
'''
fh=open('pqr.txt','r')
fh.read()
print('file read')
fh.close()
'''
#write in the file
'''
fh=open('chani.txt','w')
fh.write('Hello All')
print('data inserted')
fh.close()
'''
#append the file
'''
fh=open('chani.txt','a')
fh.write('\nBye bye ')
print('data inserted')
fh.close()
'''
#appending pnj file
'''
fh=open('C:\\Users\\11117\\Pictures\\Screenshots\\Screenshot (1).png','ab')
fh.write()
print('alteration done')
fh.close()
'''
#reading file seek, tell, readline, readlines
'''
fh=open('zchani.txt') #by default its read mode
#print(fh.read()) #read whole file 
#print(fh.readline())
print(fh.tell())
print(fh.seek(0))
print(fh.tell())
print(fh.readline())
#print(fh.readlines())
'''
#writelines
'''
fh=open('chani.txt','w')
l=['1','2','3','4']
print(fh.writelines(l))
fh.close()
'''
#without closing file
'''
with open('C:\\Users\\11117\\Desktop\\CJC\\Python\\Notes\\xyz1.txt') as fh:
    print(fh.read())
'''
#read images(binary file)
'''
fh=open('C:\\Users\\11117\\Desktop\\download.png','rb')
print(fh.read())
'''

