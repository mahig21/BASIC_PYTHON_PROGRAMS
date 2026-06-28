students_dict = {
    "Ram": "Cricket",
    "Naresh": "Football",
    "Vani": "Tennis",
    "Rahim": "Cricket",
    "Deepak": "Boxing"
}

str=input().split()
students_dict[str[0]]=str[1]
print(students_dict)
