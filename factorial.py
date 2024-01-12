# Program to find the factorial of a number using recursion
def factorial(digit):
  if digit == 0 or digit == 1:
    return 1
  else:
    return digit * factorial(digit-1)

user_input = int(input("Enter the number: "))
factorial(user_input)