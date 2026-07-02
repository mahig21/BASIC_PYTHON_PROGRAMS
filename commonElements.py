set_a = input("Enter first number sequence: ").split(',')
set_b = input("Enter second number sequence: ").split(',')
set_1 = set(set_a)
set_2 = set(set_b)
intersect = list(set_1 & set_2)
listt = []
for i in intersect:
    num = int(i)
    listt.append(num)
listt.sort()
print(listt)
