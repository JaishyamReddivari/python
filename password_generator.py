import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '&', '(', ')', '*', '+']

print("Welcome to Py Password Generator!")
in_letters = int(input("How many letters would you like in your password? "))
in_numbers = int(input("How many numbers would you like in your password? "))
in_symbols = int(input("How many symbols would you like in your password? "))

l = random.choices(letters, k=in_letters)
n = random.choices(numbers, k=in_numbers)
s = random.choices(symbols, k=in_symbols)

password = l + n + s
random.shuffle(password)
print(''.join(password))
