#Create a program that checks if a given string is a palindrome.
# Input a string from the user
user_input = input("Enter a string: ")

# Remove spaces and convert the string to lowercase for accurate comparison
processed_string = user_input.replace(" ", "").lower()

# Check if the string is a palindrome
if processed_string == processed_string[::-1]:
    print(f"'{user_input}' is a palindrome!")
else:
    print(f"'{user_input}' is not a palindrome.")