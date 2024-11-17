# 17. Write a program that asks for an integer and checks if it’s divisible by 2, 3, or both.
# Input number from the user
num = int(input("Enter an integer: "))

# Check divisibility by 2, 3, or both
if num % 2 == 0 and num % 3 == 0:
    print(f"{num} is divisible by both 2 and 3.")
elif num % 2 == 0:
    print(f"{num} is divisible by 2.")
elif num % 3 == 0:
    print(f"{num} is divisible by 3.")
else:
    print(f"{num} is not divisible by 2 or 3.")
# Question 18: Take a user’s score and determine if they pass or fail (pass if 50 or above).
# Input score from the user
score = int(input("Enter your score: "))

# Check if the score is 50 or above (pass) or below (fail)
if score >= 50:
    print("You pass!")
else:
    print("You fail!")
# Question 19: Check if a string input is uppercase, lowercase, or a mix.
# Input string from the user
text = input("Enter a string: ")

# Check if the string is uppercase, lowercase, or a mix
if text.isupper():
    print("The string is uppercase.")
elif text.islower():
    print("The string is lowercase.")
else:
    print("The string is mixed.")
# Question 20: Create a program that evaluates if an inputted number is prime.
# Input number from the user
num = int(input("Enter a number: "))

# Check if the number is prime
if num <= 1:
    print(f"{num} is not a prime number.")
else:
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):  # Check up to the square root of the number
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(f"{num} is a prime number.")
    else:
        print(f"{num} is not a prime number.")
