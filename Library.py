import time
print ("enter your name")

name=input()

print ("enter your roll no")

rollno=input ()

a=['A', 'B', 'C']
print ("enter your book name") 
choice=input()


a=time.ctime() 
print("time: ",time.ctime())

if choice=='A':

    print ("A book is available")

    print ("author: aaa")

elif choice=='B':

     print ("B book is available")

     print ("author: bbb")

elif choice=='C':

    print("C book is available")

    print("author: ccc")
else :
    print ("no book available")
b=time.ctime()
delta=b-a