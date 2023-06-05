def replace_dot(file1):
    file2=open("d:\\Replacedot.txt","w") 
    text=file1.readline()
    while text:

        word=text.split() #creating a list of words word
        word=[w.replace('.', ',') for w in word]#searching dot from each word and replacing it by comma text=''.join(word)#creating a sentence again from list of words
        text=''.join(word)
        text +='\n'
        file2.write(text) #writing the content to the file text 
        text=file1.readline()#reading file line by line in a loop
    file1.close() 
    file2.close()

def to_lower_case(file1):
    file2=open("d:\\lowercase.txt","w")
    text=file1.readline()
    while text:
         word=text.split()
         word =[w.lower()for w in word]#converting each word to lower case
         text=''.join(word)
         text +='\n'
         file2.write(text) 
         text=file1.readline()
    file1.close() 
    file2.close()
def to_upper_case(file1):
    file2=open("d:\\uppercase.txt","w")
    text=file1.readline()
    while text:
        word=text.split() 
        word=[w.upper() for w in word]
        text=''.join(word)
        text += '\n'
        file2.write(text)
        text=file1.readline()
    file1.close()
    file2.close()

file1=open("d:\\Original.txt","r")
replace_dot(file1)
print("The dots are replaced by commas in the file")

file1=open("d:\\Original.txt","r")
to_lower_case(file1)
print("The upper case letters are converted to lower case")

file1=open("d:\\Original.txt","r")
to_upper_case(file1)
print("The lower case letters are converted to upper case")