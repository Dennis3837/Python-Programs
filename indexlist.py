# Program to find the index of the given user input
my_list = [int(input("Enter the element: ")) for x in range(1,int(input("Enter the number of elements: "))+1)]
print(my_list)
count = 0
user_input = int(input("Enter the element you wish to search: "))
for digit in my_list:
  if digit == user_input:
    break
  else:
    count += 1
if count == 0:
  print(f'{user_input} is in the {count} index')
else:
  print(f'{user_input} is in the {count} index')