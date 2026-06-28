names1=input("Enter names for first list: ").split()
ages1=input("Enter ages for first list: ").split()
names2=input("Enter names for second list: ").split()
ages2=input("Enter ages for second list: ").split()
names1.extend(names2)
ages1.extend(ages2)
dict1={}
for i in range(len(names1)):
    dict1[names1[i]]=ages1[i]
list_a=[]
for i in dict1:
    tuple_a=[]
    for j in list_a:
        if j[0]==i:
            list_a.remove(j)
    tuple_a.append(i)
    tuple_a.append(int(dict1[i]))
    list_a.append(tuple(tuple_a))
list_a.sort()
print(list_a)