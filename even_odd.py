'''Python Project: 
Option 1: Print a list of even numbers up to nth term.
Option 2: Print a list of odd numbers up to nth term.
Option 3: Check if a number is even or odd.
Run the project in a loop, until user enters 'q'.
'''

while True:
    print("=====================================================")
    print("Option 1: Print a list of even numbers up to nth term.")
    print("Option 2: Print a list of odd numbers up to nth term.")
    print("Option 3: Check if a number is even or odd.")
    print("Enter 'q' to end the program.")
    print("=====================================================")

    user_option = input("Select an option: ")

    if user_option.lower() == 'q':
        break

    else:
        if user_option.isdigit():
            user_option = int(user_option)

            if user_option == 1:
                nth_term = int(input("Required number of elements: "))
                even_list = [i for i in range(1, (nth_term*2)+1) if i % 2 == 0]
                print(
                    f"Here is your Even numbers list with {nth_term} elements:\n{even_list}")

            elif user_option == 2:
                nth_term = int(input("Required number of elements: "))
                odd_list = [i for i in range(1, (nth_term*2)+1) if i % 2 == 1]
                print(
                    f"Here is your Odd numbers list with {nth_term} elements:\n{odd_list}")

            elif user_option == 3:
                number = int(input("Enter a number: "))
                if number % 2 == 0:
                    print(f"{number} is an EVEN number.")
                elif number % 2 == 1:
                    print(f"{number} is an ODD number.")

            else:
                print(
                    f"Required options 1, 2 or 3. But received {user_option}.")

        else:
            print(
                f"Required options must be a positive integer only. But received {user_option}.")
