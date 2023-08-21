a = int(input("Enter the number till which Ramanujan Numbers are to be found"))
for i in range(1,a+1) :
    for j in range(1,a+1):
        for k in range(1, a+1):
            for l in range(1, a+1):
                if(i**3 + j**3 == k**3 + l**3):
                    print(i, j, k, l, "are Ramanujan numbers")
            l+=1
        k+=1
    j+=1
i+=1
    