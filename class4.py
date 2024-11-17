#Ask the user for a grade percentage and display the corresponding letter grade (A, B, C, D, F).
percentage=int(input("Enter percentage: "))
if percentage >=80 :
    print ("the grade is 'A'")
elif percentage>=70:
    print ("the grade is 'B'")
elif percentage>=60:
    print ("the grade is 'C'")
elif percentage>= 50:
    print ("the grade is 'D'")
else:
    print("the grade is 'F'") 