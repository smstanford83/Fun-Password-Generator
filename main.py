#Password Generator Project

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("\nHow many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password = '' # initialize variable


for letter in range(1, nr_letters + 1):
  nr_rand = random.randint(0, len(letters) - 1)
  char = letters[nr_rand]
  password = password + char
  # alternative method
  # password += random.choice(letters)

for symbol in range(1, nr_symbols + 1):
  nr_rand = random.randint(0, len(symbols) - 1)
  char = symbols[nr_rand]
  password = password + char
  
for number in range(1, nr_numbers + 1):
  nr_rand = random.randint(0, len(numbers) - 1)
  char = numbers[nr_rand]
  password = password + char

pw_list = [] # initialize list variable
for pw in password: # add each character from password string to a list
  pw_list.append(pw)

random.shuffle(pw_list) # randomize order of characters in list

rand_pass = '' # initialize variable for the randomized password
for i in pw_list: # convert list back to string
  rand_pass += i
  
print(f'Your password is:  {rand_pass}')