def convert_string_to_int(list_a):
    new_list = []
    for item in list_a:
        num = int(item)
        new_list.append(num)
    return new_list


m, n = input("Enter rows and column: ").split()
m, n = int(m), int(n)
num_list = []

for i in range(m):
    list_a = input("Enter matrix: ").split()
    list_a = convert_string_to_int(list_a)
    num_list.append(list_a)
maxL=num_list[0][0]
minL=num_list[0][0]
sumL=0
for i in num_list:
    for j in i:
        sumL+=j 
        if maxL<j:
            maxL=j 
        if minL>j:
            minL=j
print(maxL)
print(minL)
print(sumL)