import numpy as np
a= int(input("Enter the number whose digits you want reversed: "))
rev_no = 0
while(a>=1):
  digit = a%10
  rev_no = rev_no*10+ digit
  a= int(a/10)


print(rev_no)

# in form of a list 
#  l=[]
#  for n in str(a):
#     l.append(int(n))
#  print(l[::-1])
