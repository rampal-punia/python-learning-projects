'''Python Quick Codes: Generate table of a given number.'''


print("Enter a number and I will print it's table.")
print("Enter 'quit' to end the program.")


# def get_table(number):
#     return [num for num in range(number, ((number*10)+1), number)]

def get_table(number):
    for count in range(1, 11):
        print(f"{number} X {count} = {count*number}")


while True:
    text = input("Enter a number: ")

    if text.lower() == "quit":
        break
    else:
        number = int(text)
        table = get_table(number)
