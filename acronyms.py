str=input("Enter String: ")
L=str.split()
newL=[]
for i in L:
    newL+=i[0]
print(".".join(newL))