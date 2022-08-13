from random import randint

computer_guess = randint(1, 100)
max_chances = 8
count = 0
# print(computer_guess)

print("================================================")
print("Welcome to the number guessing game.")
print("I have chosen a number between 1 to 100.")
print(f"Guess the correct number in {max_chances} chances.")
print("================================================")

while count < max_chances:

    user_guess = input("Enter your guess: ")
    count = count + 1
    try:
        user_guess = int(user_guess)
    except:
        print("Wrong input. Enter an integer between 1 to 100.")
        print(f"You are left with {max_chances - count} chances.")
        continue

    if user_guess in range(1, 101):
        if user_guess == computer_guess:
            print("You win!")
            break

        elif user_guess > computer_guess:
            print("Lower than that.")

        elif user_guess < computer_guess:
            print("Higher than that.")
            print(f"You are left with {max_chances - count} chances.")

        if count >= max_chances:
            print(f"You have used {max_chances} chances.")
            print(f"I guessed {computer_guess}")
            print("Computer win!")
    else:
        print(f"You are left with {max_chances - count} chances.")
        print("Enter a number between 1 to 100.")
