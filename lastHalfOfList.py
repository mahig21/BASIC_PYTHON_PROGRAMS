n=int(input("Enter the number of elements in the list: "))
L=[]
newList=[]
str=input("Enter the elements of the list separated by spaces: ")
L=str.split()
half=int(n/2)
for i in range(-half,0):
    num=int(L[i])
    newList+=[num]
print(newList)
