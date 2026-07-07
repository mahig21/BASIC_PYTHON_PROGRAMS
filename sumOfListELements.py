string = input()
string_list = string.split()

summ = 0
int_list = []
for i in string_list:
    i = int(i)
    summ += i
print(summ)