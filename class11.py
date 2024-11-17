# Take two numbers and an operator (+, -, *, /) as input and perform the corresponding operation.
num1 = int(input("enter num1:"))
num2 = int(input("enter num2:"))
operator = input("enter the operator:")

if operator == "+":
    result = num1 + num2
    print(result)
elif operator == "-":
    result = num1 - num2
    print(result)
elif operator == "/":
    result = num1 // num2
    print(result)
elif operator == "*":
    result = num1 * num2
    print(result)
