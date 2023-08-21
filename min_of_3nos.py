#import numpy as np
a= int (input("Enter a "))
b= int (input("Enter b "))
c= int (input("Enter c "))
if (a<b):
  if(a<c):
      print("max number", a)
  else: 
      print("max number is ", c )
else:
   if(b<c):
          print("max number is:   ", b)
   else:
          print("max number is ",c)