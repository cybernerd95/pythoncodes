import sys 
a=str(input("Enter the word you want to conver to lower case: "))
for i in str(a):
    if (ord(i)>=65 and ord(i)<=90):
        j=chr((ord(i)+32))
        print (j,end='')
    else:
        print("ERROR")
        sys.exit(0)

        