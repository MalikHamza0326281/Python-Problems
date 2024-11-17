#Write a program to determine if a given character is a vowel or consonant.
# Input a character from the user
char = input("Enter a character: ").lower()  # Convert input to lowercase for simplicity

# Check if the character is a vowel or consonant
if char in 'aeiou':
    print(f"{char} is a vowel.")
elif char.isalpha():  # Check if it's a letter (not a number or symbol)
    print(f"{char} is a consonant.")
else:
    print("Invalid input. Please enter a letter.")