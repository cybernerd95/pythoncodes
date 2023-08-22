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