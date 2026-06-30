str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")
index = str1[0]
if index in str2 and len(str1)==len(str2):
    ans = str2.index(index)
    print(ans)
else:
    print("No Match")
