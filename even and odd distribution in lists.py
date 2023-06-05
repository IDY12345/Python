lst = []
even =[]
odd = []
n = int(input("Enter number of elements : "))
for i in range(0, n):
    ele = int(input())
 
    lst.append(ele) 

for i in range(0,n):
    if lst[i]%2==0 :
        even.append(lst[i])
    else :
        odd.append(lst[i])
print(even)
print(odd)