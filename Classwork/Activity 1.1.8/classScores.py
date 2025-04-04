myClasses = ["Robotics: ", "Government: ", "Math: ", "Finance: ", "Physics: ", "Comp Science: ", "English: "]
classScores = []

for i in myClasses:
    grade = int(input("Enter score for "+i))
    classScores.append(grade)

    if grade>=90:print("A") # show grade is greater than 90 if greater than 90
    elif grade>=80:print("B") # if not then show it is greater than 80 if greater than 80 
    elif grade>=70:print("C") # if not then show it is greater than 70 if greater than 70 
    elif grade>=60:print("D") # if not then show it is greater than 60 if greater than 60
    else:print("F") # if not then show it is less than 60

gpa=0
for i in range(len(classScores)):gpa+=classScores[i-1]/100*4/7
print("GPA: ",gpa)