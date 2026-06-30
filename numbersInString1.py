str1=input("Enter a string: ")
digits=[]
for i in str1:
    if i.isdigit():
        digits+=[int(i)]
summ=sum(digits)
avg=round(summ/len(digits),2)
print(summ)
print(avg)