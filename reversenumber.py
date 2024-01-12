# Program to reverse a number given by the user

# Function to reverse the number
def reverse(digit):
  reversed_digit = 0
  tem = 0
  while digit != 0:
    tem = digit % 10
    reversed_digit = (reversed_digit * 10) + tem
    digit = digit // 10
  return reversed_digit

# main function
def main():
  user_input = int(input("Enter the number: "))
  print(f'Reversed number: {reverse(user_input)}')
if __name__ == '__main__':
  main()