# 11. Check if a given number is a multiple of both 3 and 5.
num = int(input("enter a number:"))
if num % 3 == 0 and num % 5 == 0:
    print("The number you entered is a multiple of both 3 and 5")
elif num % 3 == 0:
    print("The number you entered is a multiple of 3")
elif num % 5 == 0:
    print("The number you entered is a multiple of 5")
else:
    print("The number you entered is not a multiple of both 3 and 5")
