n=int(input("Enter the value of N: "))
squares={}
for i in range(1,n+1):
    square=i*i 
    squares[i]=square 
print(squares)