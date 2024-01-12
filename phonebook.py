# Phone book program
def Add_contact(contactbook):
  Name = input("Enter the name: ")
  number = input("Enter the number: ")
  contactbook[Name] = number
def Search_contact(contactbook):
  search_element = input("Enter the name wish to search: ")
  for Name,number in contactbook.items():
    if search_element == Name:
      val = 1
  if val == 1:
    print(f'Contant available: {Name}: {number}')
  else:
    print('Contact not available')

def Updation_contact(contactbook):
  user_input = input("Enter which contact you wish to update: ")
  for Name,number in contactbook.items():
    if user_input == Name:
      up_element = input("Enter the number wish to update: ")
      contactbook[Name] = up_element
def Display(contactbook):
  print("Phone Book")
  for Name,number in contactbook.items():
    print(f'Name: {Name} Number: {number}')
def Delete(contactbook):
  delete_element = input("Enter the name: ")
  if delete_element in contactbook:
    del contactbook[delete_element]
  else:
    print('Name is not in the contact book')
contactbook = {}
while True:
  print("Phone Book")
  print('1.Add contact')
  print('2.Update contact')
  print('3.Search contact')
  print('4.Delete contact')
  print('5.Display contac')
  print('6.Exit')
  user_input = int(input("Enter the choice: "))
  if user_input == 1:
    Add_contact(contactbook)
  elif user_input == 3:
    Search_contact(contactbook)
  elif user_input == 2:
    Updation_contact(contactbook)
  elif user_input == 5:
    Display(contactbook)
  elif user_input == 4:
    Delete(contactbook)
  elif user_input == 6:
    break
