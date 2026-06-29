str1=input("Enter a string: ").split()
n=int(input("Enter length: "))
output=""
for i in str1:
    if len(i)!=n:
        output+=i+" "
print(output)