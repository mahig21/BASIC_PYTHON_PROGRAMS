str=input("Enter numbers separated by spaces: ")
L=str.split()
newList=[]
for i in L:
    num=int(i)
    newList+=[num]
print(newList)