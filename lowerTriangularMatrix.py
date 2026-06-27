def print_lower_triangle(matrix,m,n):
    for i in range(m):
        lower_triangle=[]
        for j in range(n):
            if j<=i:
                lower_triangle.append(matrix[i][j])
        print(lower_triangle)

def convert_string_to_int(list_a):
    new_list = []
    for item in list_a:
        num = int(item)
        new_list.append(num)
    return new_list


m, n = input("Enter rows and columns: ").split()
m, n = int(m), int(n)
num_list = []

for i in range(m):
    list_a = input("Enter matrix: ").split()
    list_a = convert_string_to_int(list_a)
    num_list.append(list_a)

print_lower_triangle(num_list,m,n)