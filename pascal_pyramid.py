import math  as math
a=int(input("enter the level of pyramid you want : "))


print("1")
def nCr(n,r):
    f = math.factorial
    return f(n) // f(r) // f(n-r)

for n in range(2,(a+1)):
    for r in range(0,(n+1)):
        print(nCr(n,r), end=' ')
    print(" ")
  