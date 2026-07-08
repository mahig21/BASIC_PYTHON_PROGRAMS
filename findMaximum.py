string = input("Enter a string of numbers separated by spaces: ")
string_list = string.split()
great=int(string_list[0])
for i in string_list:
    num = int(i)
    if num > great:
        great = num
print(great)