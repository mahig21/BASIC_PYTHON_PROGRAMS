string=input("Enter string: ").lower()
L=list(string)
set_a=set(L)
L1=list(set_a)
L1.sort()
for i in L1:
    if i.isalpha(): 
        countA=L.count(i)
        print(i+": "+str(countA))
