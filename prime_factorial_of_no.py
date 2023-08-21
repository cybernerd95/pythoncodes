a = int(input("Enter a positive integer you want prime factors for : "))
print("1")
for num in range(2, (a+1) ):
    
    prime = True
    
    for i in range(2, int(num ** 0.5) + 1):
        
        if num % i == 0:
            prime = False
            break
    
    if prime:
        if a % num == 0 :
            
            print (num)