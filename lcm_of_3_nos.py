import numpy as np
a= int(input("enter the number: "))
b= int(input("enter the number: "))
c= int(input("enter the number: "))

if (a>b):
  if(a>c):
      d=a
      while True:
        if d % b == 0 and d  % c == 0 and d % a == 0:
            print(d)
            break
        d =d + 1
  else:
      d=c
      while True:
        if d % a == 0 and d  % b == 0 and d % c == 0:
            print(d)
            break
        d =d + 1
else:
   if(b>c):
      d=b
      while True:
        if d % a == 0 and d  % c == 0 and d % b == 0:
            print(d)
            break
        d =d + 1
   else:
      d=c
      while True: 
        if d % a == 0 and d % b == 0 and d % c== 0:
            print(d)
            break
        d = d +1



# Or the other method can be you get LCM of 1st number and 2nd number and  then take LCM of the obtained LCM and the 3rd number


