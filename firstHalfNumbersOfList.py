import math
str=input("Enter String: ")
L=str.split()
length=len(L)
half=math.ceil(length/2)
newList=[]
for i in range(half):
    num=int(L[i])
    newList+=[num]
print(newList)
