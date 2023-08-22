a = int(input("Enter a positive integer you want  factors for : "))
i = 2                      #D
while True:
    while(a>1):            #R
     if(a%i==0):
        print(i)
        a=a//i
     if(a==1  or a%i!=0):  #D
        i=i+1
        break




