str=input("Enter String: ")
L=str.split()
newStr=[]
for word in L:
    rev=word[::-1]
    newStr+=rev+" "
print("".join(newStr))
