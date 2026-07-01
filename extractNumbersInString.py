L=input("Enter elements separated by commas: ").split(",")
L1=[]
for i in L:
    if i.isdigit():
        L1+=[int(i)]
print(L1)