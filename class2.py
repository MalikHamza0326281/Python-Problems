#Write a program that checks if a given year is a leap year.
year = int(input("enter the checking year: "))
if year%400==0 and year%100==0:
    print("the yaer is leap!")
elif year%4==0 and year % 100!=100:
    print("the yaer is leap!")
else:
    print("the yaer is not leap!")