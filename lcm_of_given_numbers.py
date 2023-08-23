a = int(input('Enter a  '))
b = int(input('Enter b  '))
if a > b:
    c = a
else:
    c= b  
while True:
    if c % a == 0 and c  % b == 0:
        print(c)
        break
    c =c+ 1