num=input("Enter the numbers (comma-separated): ").split(",")
num_list=[]
for i in num:
    num_list+=[int(i)]
print(num_list)
def sum_of_list(num_list):
    if len(num_list)==1:
        return
    sumL=[]
    for i in range(len(num_list)-1):
        summ=num_list[i]+num_list[i+1]
        sumL.append(summ)
    print(sumL)
    return sum_of_list(sumL)
        
sum_of_list(num_list)