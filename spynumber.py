# Program to check whether a number is a spy number
from math import prod
user_input = input("Enter the number: ")
is_spy = prod(map(int, user_input)) == sum(map(int, user_input))
print(f'{user_input} is a spy number' if is_spy else f'{user_input} is not a spy number')