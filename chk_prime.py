
a = int(input("Enter a number: "))
is_prime = 1
    
for i in range(2, int(a**0.5)+1):
        if a % i == 0:
            is_prime = 0
            break
        

if (is_prime):
    print("it is a prime number.")

else:
    print(" it is not a prime number.")