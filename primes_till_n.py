n = int(input("Enter a positive integer: "))
for num in range(2, n ):
    prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            prime = False
            break
    if prime:
        print(num )

