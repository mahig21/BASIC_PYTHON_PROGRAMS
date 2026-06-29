matrix=[]
winner=""
def abhinav_or_anjali(var):
    if var=='O':
        return "Abhinav Wins"
    else:
        return "Anjali Wins"
for i in range(3):
    row=input().split()
    matrix+=[row]

#CHECK ROWS
for i in matrix:
    if i[0]==i[1]==i[2]:
        winner=abhinav_or_anjali(i[0])
#CHECK COLUMN        
for i in range(3):
    if matrix[0][i]==matrix[1][i]==matrix[2][i]:
        winner=abhinav_or_anjali(matrix[0][i])

#CHECK DIAGONALS
if matrix[0][0]==matrix[1][1]==matrix[2][2]:
    winner=abhinav_or_anjali(matrix[0][0])
elif matrix[2][0]==matrix[1][1]==matrix[0][2]:
    winner=abhinav_or_anjali(matrix[2][0])
#TO CHECK TIE
if winner=="":
    print("Tie")
else:
    print(winner)