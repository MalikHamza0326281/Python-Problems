# Check if a year input by the user is a century year.
year = int(input("enter a year:"))
if year % 100 == 0:
    print("this year is a century year")
else:
    print("the year is not a century year")
