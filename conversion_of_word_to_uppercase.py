import sys 
a=str(input("Enter the word you want to conver to upper case: "))
for i in str(a):
    if (ord(i)>=97 and ord(i)<=122 ):
        j=chr((ord(i)-32))
        print (j,end='')
    else:
        print("ERROR")
        sys.exit(0)
        