from re import I


print("Enter a number")
n=int(input())
fact=1
for i in range (1,n+1):
     fact=fact*i
print("Factorial is : ",fact)