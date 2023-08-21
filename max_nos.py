#import numpy as np
a= int (input("Enter a "))
b= int (input("Enter b "))
c= int (input("Enter c "))

max_no = a

if(b>max_no):
     max_no =b

if(c>max_no):
     max_no = c

print("max number is ", max_no)
