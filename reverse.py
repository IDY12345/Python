print("Enter a number to be reversed")
n=int(input())
temp=n
reverse=0
while n>0:
    r=int(n%10)
    reverse=int(reverse*10+r)
    n=int(n/10)
print("The reversed number is",reverse)