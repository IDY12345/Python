import time
class Lib():
    def display1(self):
        
        print("1.Display The Books in Library")
        print("2.Lend a Book")
        print("3.Add a Book")
        print("4.Return The Book")
        
    def display(self,name,Roll):
        name=name
        Roll=Roll
        r=Lib()
        print("Book Names are:")
        print("1.History")
        print("2.geography")
        print("3.Mathematics")
        print("4.Science")
        print("Enter c to continue and q to quit")
        choice=input()
        if choice=='c':
            r.display2(name,Roll)
        elif choice=='q':
            print("Session has Ended")
        else :
            r.display()
    def lend(self,l,History,Geography,Maths,Science,name,Roll):
        name=name
        Roll=Roll
        r=Lib()
        if l==1:
            print("History Book is Lended to ",name)
            a=time.ctime()
            print("Time:",a)
            History=History-1            
            Fo=open("Library.txt","wt")
            Fo.write("\n History:")
            Fo.write(str(History))
            Fo.write("\n Geography:")
            Fo.write(str(Geography))
            Fo.write("\n Mathematics:")
            Fo.write(str(Maths))
            Fo.write("\n Science:")
            Fo.write(str(Science))
            Fo.close()
            Ro=open("Library2.txt","a")
            Ro.write(name)
            Ro.write("   ")
            Ro.write(str(Roll))
            Ro.write("   History")
            Ro.write("   ")
            Ro.write(a)
            Ro.close()
            print("Enter c to continue and q to quit")
            choice=input()
            if choice=='c':
               r.display2(name,Roll)
            elif choice=='q':
                 print("Session has Ended")
            else :
                r.display()
        elif l==2:
            print("Geography Book is Lended to ",name)
            a=time.ctime()
            print("Time:",a)
            Geography=Geography-1
            Fo=open("Library.txt","wt")
            Fo.write("\n History:")
            Fo.write(str(History))
            Fo.write("\n Geography:")
            Fo.write(str(Geography))
            Fo.write("\n Mathematics:")
            Fo.write(str(Maths))
            Fo.write("\n Science:")
            Fo.write(str(Science))
            Fo.close()
            Ro=open("Library2.txt","a")
            Ro.write(name)
            Ro.write("   ")
            Ro.write(str(Roll))
            Ro.write("   Geography")
            Ro.write("   ")
            Ro.write(a)
            Ro.close()
            print("Enter c to continue and q to quit")
            choice=input()
            if choice=='c':
               r.display2(name,Roll)
            elif choice=='q':
                 print("Session has Ended")
            else :
                r.display()
        elif l==3:
            print("Mathematics Book is Lended to ",name)
            a=time.ctime()
            print("Time:",a)
            Maths=Maths-1
            Fo=open("Library.txt","wt")
            Fo.write("\n History:")
            Fo.write(str(History))
            Fo.write("\n Geography:")
            Fo.write(str(Geography))
            Fo.write("\n Mathematics:")
            Fo.write(str(Maths))
            Fo.write("\n Science:")
            Fo.write(str(Science))
            Fo.close()
            Ro=open("Library2.txt","a")
            Ro.write(name)
            Ro.write("   ")
            Ro.write(str(Roll))
            Ro.write("   Maths")
            Ro.write("   ")
            Ro.write(a)
            Ro.close()
            print("Enter c to continue and q to quit")
            choice=input()
            if choice=='c':
               r.display2(name,Roll)
            elif choice=='q':
                 print("Session has Ended")
            else :
                r.display()
        elif l==4:
            print("Science Book has been Lended to ",name)
            a=time.ctime()
            print("Time:",a)
            Science=Science-1
            Fo=open("Library.txt","wt")
            Fo.write("\n History:")
            Fo.write(str(History))
            Fo.write("\n Geography:")
            Fo.write(str(Geography))
            Fo.write("\n Mathematics:")
            Fo.write(str(Maths))
            Fo.write("\n Science:")
            Fo.write(str(Science))
            Fo.close()
            Ro=open("Library2.txt","a")
            Ro.write(name)
            Ro.write("   ")
            Ro.write(str(Roll))
            Ro.write("   Science")
            Ro.write("   ")
            Ro.write(a)
            Ro.close()
            print("Enter c to continue and q to quit")
            choice=input()
            if choice=='c':
               r.display2(name,Roll)
            elif choice=='q':
                 print("Session has Ended")
            else :
                r.display()
        else:
            print("Invalid Entry")
            r.lend(l,History,Geography,Maths,Science,name,Roll)
   
            
    def display2(self,name,Roll):
        name=name
        Roll=Roll
        ob=Lib()
        ob.display1()        
        print("Enter Your Choice")
        choice=int(input())
        if choice==1:
           ob.display(name,Roll)
        elif choice==2:             
             print("Enter The Number of booK u want")
             l=int(input())  
             ob.lend(l,History,Geography,Maths,Science,name,Roll)
        elif choice==3:
            print("Enter The Book U Want to add")
            l=int(input())
            ob.lend(l,History,Geography,Maths,Science,name,Roll)
        elif choice==4:
            print("The Book Has been Returned by",name)

History=20
Geography=30
Maths=25
Science=30
print("Enter Your Name")
name=input()
print("Enter Your Roll No")
Roll=int(input())
ob=Lib()
ob.display2(name,Roll)    