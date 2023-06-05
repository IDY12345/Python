print("Enter The Marks in Physics")
phy = int(input())
print("Enter The Marks in Chemistry")
chem=int(input())
print("Enter The Marks in Mathematics")
math=int(input())
print("Enter The Marks in Computer")
com=int(input())
print("Enter The Marks in English")
eng=int(input())
marks=[phy,chem,math,com,eng]
avg=sum(marks)/(len(marks))*100
if avg>=75:
    print("Distinction")
elif avg>=60 :
    print("First Class")
elif avg>=50 :  
    print("Second Class")
elif avg>=40 :
    print("Pass Class")
else :
    print("Fail")        