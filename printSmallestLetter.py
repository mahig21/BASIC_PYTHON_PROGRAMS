# This program takes a string input from the user and prints the smallest letter in the string based on Unicode values.
s=input("Enter a string: ")
flag=ord(s[0])
for i in range(len(s)):
    uni=ord(s[i])
    if(flag>uni):
        flag=uni
print(chr(flag))