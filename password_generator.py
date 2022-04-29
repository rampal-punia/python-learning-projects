'''Python Project: Unique Password Generator
    => Ask user the number of letters, digits and symbols 
    required in the password.
'''
import string
import random

print("------------Password Generator---------------")

while True:
    letters = string.ascii_letters
    digits = string.digits
    symbols = [chr(i) for i in range(33, 43)]

    num_letters = int(input("Number of letters required: "))
    num_digits = int(input("Number of digits required: "))
    num_symbols = int(input("Number of symbols required: "))

    pwd_letters = [random.choice(letters) for i in range(num_letters)]
    pwd_digits = [random.choice(digits) for i in range(num_digits)]
    pwd_symbols = [random.choice(symbols) for i in range(num_symbols)]

    pwd_list = pwd_letters + pwd_digits + pwd_symbols
    k = num_letters + num_digits + num_symbols
    pwd = random.sample(pwd_list, k)
    print("".join(pwd))

    is_continue = input("Do you want to continue?(Yes/No): ")
    if is_continue.lower() == 'yes':
        continue
    else:
        break
