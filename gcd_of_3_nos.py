import numpy as np
a= int(input("enter the number: "))
b= int(input("enter the number: "))
c= int(input("enter the number: "))
l=[]
if (a<b):
  if(a<c):
        for i in range (2,a+1):
         if a % i== 0 and b % i ==0 and c % i ==0:
            l.append(i)
        print (max(l))
  else: 
        for i in range (2,c+1):
            if a % i== 0 and b % i ==0 and c % i ==0:
             l.append(i)
        print (max(l))
else:
   if(b<c):
        for i in range (2,b+1):
         if a % i== 0 and b % i ==0 and c % i ==0:
             l.append(i)
        print (max(l))
   else:
        for i in range (2,c+1):
         if a % i== 0 and b % i ==0 and c % i ==0:
             l.append(i)
        print (max(l))
           



# Or the other method can be you get GCD of 1st number and 2nd number and  then take GCD of the obtained GCD and the 3rd number