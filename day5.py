#Password Generator Project

#letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
#numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
#symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

## going to use a simpler way to specify these lists by importing string module

import random
import string

letters = list(string.ascii_letters)
numbers = list(string.digits) 
symbols = list(string.punctuation)


print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
# this is an easy way of doing this using strings

password = ""
for char in range(nr_letters):
    password += random.choice(letters)
for char in range(nr_symbols):
    password += random.choice(symbols)
for char in range(nr_numbers):
    password += random.choice(numbers)

print(f"Your password is: {password}")

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
#In this method we must use lists if we want to randomize the order of the characters

password_list=[]
for char in range(nr_letters):
  password_list.append(random.choice(letters))

for char in range(nr_symbols):
  password_list.append(random.choice(symbols))

for char in range(nr_numbers):
  password_list.append(random.choice(numbers))


print(password_list)
random.shuffle(password_list)
print(password_list)

## the following concatenates a list into a string "" specifies there is no seperator
hard_password = "".join(password_list)
print(hard_password)
