a = int (input("enter the first number:"))
b = int (input("Enter the second number:"))
if a < b:
  min_no = a
  max_no = b
else:
  min_no = b
  max_no = a

gcd = max_no % min_no
while(True):
      if(max_no%gcd == 0 and min_no%gcd ==0):
        break
      else:
          gcd = min_no%gcd
    
print("GCD of ",a," and ", b, "is ", gcd)