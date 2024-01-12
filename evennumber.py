# Program to find the sum of the even numbers in the list
my_list = [int(input(f"Enter the element {n}")) for n in range(1,int(input("Enter the number of elements: "))+1)]
Sum = 0
print(f'Sum:{sum([(digit) for digit in my_list if digit % 2 == 0])}')