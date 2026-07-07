string = input("Enter words separated by spaces: ")
M = string.split()

ans =""
for i in M:
    ans += i[2]
print(",".join(ans))