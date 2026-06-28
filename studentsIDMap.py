names=input("Enter student names (comma-separated): ").split(",")
ids=input("Enter student IDs (comma-separated): ").split(",")
student_dict={}
for i in range(len(names)):
    student_dict[names[i]]=ids[i]
names.sort()
for i in names:
    print(i+" "+student_dict[i])