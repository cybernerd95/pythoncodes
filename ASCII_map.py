for i in range (1,128):
   if (i%16==0):
        print(" ",)
   print("[",i,hex(i),chr(i),"]",end='')
    
#This prints the entire ASCII map and after every 16 charecters printed it goes to the nest line 
#The ASCII map which is provided in the repository is for reference only taken from wikimedia 