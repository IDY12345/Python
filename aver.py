a= input("Enter the numbers if the list with a space")
b=a.split()
for i in range(len(b)):
     b[i] = int(b[i])
print("Sum = ", sum(b))
print("Max = ",max(b))
print("Min = ",min(b))
print("Total Numbers = ",len(b))
print("Avg = ", sum(b)/(len(b)))