#Password Generator Project

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")

# these while loops validate user input and retry on error
while True:
    try:
        nr_letters = int(input("\nHow many letters would you like in your password?\n"))
        break
    except ValueError:
        print('Error:  Not a valid choice.  Please try again.\n')

while True:
    try:
        nr_symbols = int(input(f"How many symbols would you like?\n"))
        break
    except ValueError:
        print('Error:  Not a valid choice.  Please try again.\n')

while True:
    try:
        nr_numbers = int(input(f"How many numbers would you like?\n"))
        break
    except ValueError:
        print('Error:  Not a valid choice.  Please try again.\n')

password = '' # initialize variable

# generates user-defined random choice of letters, symbols, and numbers
for letter in range(1, nr_letters + 1):
    password += random.choice(letters)

for symbol in range(1, nr_symbols + 1):
    password += random.choice(symbols)

for number in range(1, nr_numbers + 1):
    password += random.choice(numbers)

pw_list = [] # initialize list variable
for pw in password: # add each character from password string to a list
  pw_list.append(pw)

random.shuffle(pw_list) # randomize order of characters in list

rand_pass = '' # initialize variable for the randomized password
for i in pw_list: # convert list back to string
  rand_pass += i
  
print(f'Your password is:  {rand_pass}')