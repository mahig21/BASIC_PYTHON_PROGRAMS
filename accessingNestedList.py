list_a = [('apple', 'banana', 'orange', 'grapes'), ('cricket', 'football', 'hockey'), ('car', 'bicycle', 'bus')]
n = int(input("Enter n: "))
L = []
finalList=[]
for i in range(n):
    L =input("Enter indexes: ").split()
    j=int(L[0])
    k=int(L[1])
    finalList+=[list_a[j][k]]
print(finalList)




