# Program to print the biggest element number in a list

# take input from the user
my_list = input("Enter the elements seperated by space: ").split()
my_list = [int(n) for n in my_list]
big = my_list[0]
for digit in range(1,len(my_list)):
  if my_list[digit] > big:
    big = my_list[digit]
print(f'Biggest number: {big}')