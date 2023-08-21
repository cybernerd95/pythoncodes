#import numpy as np
x=[]
sum = 0
sd = 0
sd_sum = 0

n = int(input("Enter the number of elements "))
for i in range(0,n):
   l = int(input())
   x.append(l)
   sum = sum + x[i]
   sd_sum = sd_sum + x[i]**2 


avg = sum/n
sd = sd_sum/n - avg**2
print(" Average is ", avg, "STD DEVN is ", sd)
