import string 
i=str(input("enter charecter : "))
j= (ord(i))
if (j>=65 and j<=90):
 print ("UPPER CASE LETTER ")
else: 
 if (j>=97 and j<=122):
      print("Lower case letter ",END='')
 else: 
      print("Input is not correct")

k=hex(j)
l=[]
n=[] 
for n in str(k):
  l.append(n)
n=l[2:5]
print("".join(str(x) for x in n))

