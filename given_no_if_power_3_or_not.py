a = int(input("Enter a positive integer you want  factors for : "))
i = 3
while True:
     if(a%i==0):
        print(i)
        a=a//i
     if(a%i!=0):
        if (a!=1):
            print("it is not a power of 3")
        else:
            print("it is a power")
        break
     

#You can take log of the number and devide it with log 3 and check it its a integer or not 
#Another method could be you can take the largest power of 3 that a 64 bit can store and divide it by the input number to check if the remainder is zero
