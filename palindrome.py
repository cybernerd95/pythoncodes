a=str(input("Enter a word to check for palindrome : "))
l=[]
for n in str(a):
    l.append(ord(str(n)))
c="".join(str(x) for x in l)
d=l[::-1]
e="".join(str(x) for x in d)
if e==c:
    print("it is a palindrome ")
else:
    print("its not a palindrome ")