# Write a program to check if a number is within a specified range. for a beginner
number = float(input("Enter a number: "))
lower_limit = float(input("Enter the lower limit of the range: "))
upper_limit = float(input("Enter the upper limit of the range: "))

if number < lower_limit:
    print(f"{number} is below the range {lower_limit} to {upper_limit}.")
elif number > upper_limit:
    print(f"{number} is above the range {lower_limit} to {upper_limit}.")
else:
    print(f"{number} is within the range {lower_limit} to {upper_limit}.")
