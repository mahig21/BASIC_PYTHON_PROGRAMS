str1=input("Enter the first string: ")
str2=input("Enter the second string: ")
str3=""
if str2[0] in str1:
    index=str1.index(str2[0])
    for i in str2:
        if i==str1[index]:
                str3+=i
        index+=1 
        if index==len(str1) :
           break
    print(str3)
else:
    print("No overlapping")

