print("Enter a string")
str=input()
str1=""
str=str.upper()
len=len(str)
for i in range(0,len):
    ch=str[i]
    str1=ch+str1
if(str==str1):
    print("Palindrome String")
else :
    print("Not a Palindrome String")
