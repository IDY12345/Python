from math import sqrt as i
print("Enter a Number")
n=int(input())
print("Square Root of the number",n,":",i(n))
print("Square of number ",n,":",n*n)
print("Cube of number",n,": ",n**3)
count=0
for i in range(1,n+1):
      if n%i==0:
          print("The Prime Factors are : ",i)
          count=count+1
if count==2:
    print("It is a Prime Number")
else:
    print("It is not a Prime Number")
fact=1
for i in range (1,n+1):
    fact=fact*i
print("Factorial of the ",n,"is :",fact)