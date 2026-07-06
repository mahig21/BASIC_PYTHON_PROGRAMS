str=input("Enter String: ")
L=str.split()
for i in L:
    if i[0].lower()==i[-1].lower():
        print(True)
    else:
        print(False)
