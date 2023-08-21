import math
a=int(input("Enter the number until which you want Pythogoras triplets :"))
for i in range(2,a):
    for j in range(2,a):
       k = i**2 + j**2 
       if ( (math.sqrt(k) % 1) == 0):
           print(i, j, math.sqrt(k))
    