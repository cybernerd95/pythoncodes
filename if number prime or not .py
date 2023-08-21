
a = int(input("Enter a number: "))
is_factor = 0
    
for i in range(2, a-1):
        if a % i == 0:
            is_factor = 1 
            break
        

if (is_factor):
    print("it is not a prime number.")
else:
    print(" it is a prime number.")


