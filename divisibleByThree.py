string = input("Enter numbers separated by spaces: ")
string_list = string.split()

int_list = []
for i in string_list:
    i = int(i)
    if (i % 3) == 0:
        int_list += [i]
print(int_list)