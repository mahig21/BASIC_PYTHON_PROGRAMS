str=input("Enter String: ")
L=str.split()
large=L[0]
for i in L:
    num=int(i)
    sum=sum+num
avg=round(sum/n,2)
print(avg)
