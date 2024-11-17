#Part 2
#Question 1: Print numbers from 1 to 20 using a for loop.
for i in range(1, 21):
    print(i)

#Question 2: Use a while loop to print even numbers from 1 to 50.
i = 2  
while i <= 50:
    print(i)
    i += 2  

# Question 3: Write a program to calculate the sum of all numbers between 1 and 100.
total = 0
i = 1
while i <= 100:
    total += i  
    i += 1      
print("The sum is:", total)

# Question 4: Print the multiplication table of a given number.
number = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")

# Question 5: Print all odd numbers between 1 and 100 using a loop.
i = 2  
while i <= 100:
    print(i)
    i += 2    

# Question 6: Use a for loop to print each character of a string.
text = input("Enter a string: ")
for char in text:
    print(char)

# Question 7: Find the factorial of a number using a while loop.

number = int(input("Enter a number: "))
factorial = 1
i = 1
while i <= number:
    factorial *= i  
    i += 1          
print(f"The factorial of {number} is: {factorial}")

# Question 8: Use a for loop to print numbers from 10 down to 1.
for i in range(10, 0, -1):
    print(i)

# Question 9: Write a program to print the first 10 Fibonacci numbers.

a, b = 0, 1
for _ in range(10):
    print(a)
    a, b = b, a + b  



# Question 10: Use a loop to count the number of digits in an integer.
number = int(input("Enter a number: "))
count = 0
while number != 0:
    number //= 10  
    count += 1    

print(f"The number of digits is: {count}")

# Question 11: Print the reverse of a given number.
number = int(input("Enter a number: "))
reverse = 0
while number != 0:
    digit = number % 10      
    reverse = reverse * 10 + digit  
    number //= 10            

print(f"The reverse of the number is: {reverse}")

#Question 12: Print all prime numbers between 1 and 50.

for num in range(1, 51):
    is_prime = True 
    for i in range(2, num):
        if num % i == 0:  
            is_prime = False
            break
    if is_prime and num > 1:
        print(num)

#Question 13: Use nested loops to print a pyramid pattern of *.

rows = 5

for i in range(1, rows + 1):
    
    for j in range(rows - i):
        print(" ", end="")  
    
    
    for k in range(2 * i - 1):
        print("*", end="")  
    
    
    print()

# Question 14: Write a program that breaks the loop when a certain condition is met.
for i in range(1, 11):
    if i == 6:  # Condition to break the loop
        print("Breaking the loop at number", i)
        break
    print(i)

# Question 15: Print the sum of even and odd numbers separately up to a given number.
n = int(input("Enter a number: "))
even_sum = 0
odd_sum = 0
for i in range(1, n + 1):
    if i % 2 == 0:  
        even_sum += i
    else:  
        odd_sum += i
print("Sum of even numbers:", even_sum)
print("Sum of odd numbers:", odd_sum)

# Question 16: Create a program to calculate the sum of the digits of an inputted integer.
number = int(input("Enter an integer: "))
digit_sum = 0
while number != 0:
    digit_sum += number % 10  
    number //= 10  

print("The sum of the digits is:", digit_sum)

# Question 17: Write a program that continues to ask for a number until the correct number is guessed.
correct_number = 7

while True:
    
    guess = int(input("Guess the number: "))
    
    if guess == correct_number:
        print("Congratulations! You guessed the correct number.")
        break  
    else:
        print("Incorrect guess. Try again.")

# Question 18: Use a loop to print numbers in reverse order within a given range.
start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))
for i in range(end, start - 1, -1):
    print(i)

# Question 19: Use a for loop to print the square of each number from 1 to 10.
for i in range(1, 11):
    print(f"The square of {i} is {i ** 2}")

# Question 20: Create a program that simulates a countdown timer starting from a given number down to zero.
start = int(input("Enter the starting number for the countdown: "))
for i in range(start, -1, -1):
    print(i)




    
        



    




