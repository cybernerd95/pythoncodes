#Using lists 
a= int(input("enter the number  "))
b= int(input ("enter power of the number  "))
c=a**b
l=[]
for n in str(c):
   l.append(n)
   print(len(l)) 
print("Are the number of digits in a^b" ,a,b )
print(c)



# #Alternate method using logarithm
# import math
# a= int(input("enter the number  "))
# b= int(input ("enter power of the number  "))
# p = b*math.log10(a)
# print(a, "power", b , " has ", int(p) +1 , "digits")


#Another method would be continuously dividing it by 10 with giving a predefined i=0 and then adding +1 for 
#for everytime the number is divided i=i+1 and until the number is less than 1 and then printni 