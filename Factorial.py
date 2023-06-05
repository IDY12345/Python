print("Enter a Number to find a factorial")
n=int(input())
fact=1
for i in range(0,n):
    fact=fact*i
print("The factorial is : ",fact)