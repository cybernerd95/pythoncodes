s=str(input("Enter the sentence: "))
e=str(input("Enter the letter you want to check the number of times it has occoruced for in the sentence :- "))
b=0
for a in s:
	if e in a:
		b=b+1
print ("the number of" ,e+ "'s in the sentence is:-",b )