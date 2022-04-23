'''Python Project: 
Calculate Movie ticket price.
    * Ask user's age.
    * If the age is less than 3 the ticket is free.
    * If the age is between 4 - 12 the amount is 50%.
    * If the age is more than 12, the amount is 100%
    * Catch the error if the user inputs any wrong data.
'''


def msgs_to_user():
    print("Enter age to get the ticket price.")
    print("Press 'q' to end the program.")
    print("==================================")


def get_ticket_amount(age, ticket_price):
    if 0 < int(age) < 4:
        print(f"The ticket amount is ZERO.")
    elif int(age) > 130:
        print(
            f"Are you sure the age is {age}. Please enter the age again.")
    elif 3 < int(age) < 13:
        print(f"The ticket amount is {ticket_price/2}.")
    else:
        print(f"The ticket amount is {ticket_price}.")


msgs_to_user()
while True:
    age = input("Enter age: ")
    ticket_price = 100
    if age.lower() == "q":
        break
    else:
        if age.isdigit():
            get_ticket_amount(age, ticket_price)
        else:
            print(
                f"**Age must be a positive integer(eg.25), but received '{age}'.")
