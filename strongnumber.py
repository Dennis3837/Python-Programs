# Program to check whether a number is a strong number or not
import math
user_input = int(input("Enter the number: "))
ori = user_input
tem = 0
fact = 0
while user_input != 0:
  tem = user_input % 10
  fact += math.factorial(tem)
  user_input //= 10
if fact == ori:
  print("It is a strong number")
else:
  print("It is not strong number")