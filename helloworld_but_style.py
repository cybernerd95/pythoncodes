import time 
a=str(input("enter your name  "))
z=chr(127)
q=61
for s in a:
    t = ord(s)
    if (t!=32):
        for q in range (97,122):
            if (q!=t):
                print(z,chr(q),sep='')
                q=q+1
                time.sleep(0.07)
            else:
                print (z,chr(q),sep='')
                z=z+s
                break
    else:
        z=z+s
        print (z)