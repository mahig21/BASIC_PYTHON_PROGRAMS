n=int(input("Enter the number of sets: "))
main_list=[]
def convet_to_int(sets):
    int_set=[]
    for i in sets:
        int_set+=[int(i)]
    return int_set
for i in range(n):
    sets=input("Enter elements of set " + str(i+1) + ": ").split()
    sets=convet_to_int(sets)
    main_list.append(sets)

set_a=set()
for i in range(n-1):
    set_a=set(main_list[i]) & set(main_list[i+1])
final_list=list(set_a)
if n==1:
    final_list=main_list[0]
final_list.sort()
print(final_list)
    