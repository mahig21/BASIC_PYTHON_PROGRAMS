bag=input("Enter the bag of scores (comma-separated): ").split(",")
score_dict=[]
final=[]
set_a=set()
for i in bag:
    tuple_a=[]
    tuple_a.append(i[0])
    tuple_a.append(i[2:])
    set_a.add(i[0])
    score_dict.append(tuple_a)
set_a=list(set_a)
set_a.sort()
for i in set_a:
    summ=0
    for j in score_dict:
        if j[0]==i:
            summ+=int(j[1])
    tuple_b=[]
    tuple_b.append(i)
    tuple_b.append(summ)
    final.append(tuple(tuple_b))
print(final)
    