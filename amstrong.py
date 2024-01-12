# Program to check whether a number is an amstrong number

def main():
  user_input = int(input("Enter the number: "))
  ori = user_input
  tem = 0
  fact = 0
  while user_input != 0:
    tem = user_input % 10
    fact += pow(tem,3)
    user_input //= 10
  print(fact)
  if fact == ori:
    print("It is a amstrong number")
  else:
    print("It is not strong number")
if __name__ == '__main__':
  main()