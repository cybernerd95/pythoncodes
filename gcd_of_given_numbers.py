a = int (input("enter the first number:"))
b = int (input("Enter the second number:"))
if a < b:
  c = a
else:
  c = b

while True:
  if a % c  == 0 and b % c == 0:
    print(c)
    break
  c+=1
    

