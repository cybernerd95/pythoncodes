import math as math
a= int(input("enter the number to which you want to sum the digits of"))


b=0

for n in str(a):
    b = b + int(n)

print(b)