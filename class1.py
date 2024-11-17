#Take a user’s age as input and display whether they are a minor, adult, or senior citizen.
age= int(input("Enter the age citizen: "))
if age<18:
    print("The citizen is minor!")
elif age>=18 and age<40:
    print("The citizen is adult!")
elif age>=40:
    print("The citizen is senior!")