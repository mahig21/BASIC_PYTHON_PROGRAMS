import math
str=input("Enter String: ")
L=str.split()
length=len(L)
half=math.ceil(length/2)
print(L[0:half])
