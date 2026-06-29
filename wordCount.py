strr = input("Enter a string: ").split()
dict_a = {}
for i in strr:
    dict_a[i] = int(strr.count(i))
for i in dict_a:
    print(i+": "+str(dict_a[i]))