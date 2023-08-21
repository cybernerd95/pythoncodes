a = int (input("enter the first number:"))
b = int (input("Enter the second number:"))
if a < b:
  c = a
else:
  c = b
gcd = 1
for i in range(2, c+1):
        if a % i  == 0 and b % i ==0 :
            gcd = i
        i+=1

print("GCD of ", a, "and ", b , "is ", gcd)