import math as math 
a= int(input("enter the number you want factors for "))

for i  in range(1, (a+1) ):
     if a % i == 0:
         print(i)
