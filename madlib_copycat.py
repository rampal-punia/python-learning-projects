'''Python Project:
Game 1: Play Copy Cat.
Game 2: Play Madlib.
Run the program in a loop, until user enters 'q'.
'''
# Madlibs are short amusing stories made up by taking few inputs from someone,
# After placing those inputs in a pre-written story, It is read aloud for fun.


def msgs_to_user():
    print("=====================================================")
    print("Game 1: Play Copy Cat.")
    print("Game 2: Play Madlib.")
    print("Enter 'q' to end the program.")
    print("=====================================================")


def play_copycat_game():
    print("I am a copy cat! I will repeat whatever you type.")
    print("I am a copy cat! I will repeat whatever you type.")
    print("Enter 'q' to end the program.")
    while True:
        text = input("What do you have to say?: ")

        if text.lower() == "q":
            break
        else:
            print(f"{text.upper()}!!!")


def play_madlib_game():
    print("A magic book madlib game. Give inputs, read story, Enjoy!!!.")
    while True:
        name1 = input("Enter any name: ")
        name2 = input("Enter another name: ")
        color = input("Enter any color: ")
        new_old = input("New/old: ")
        emotion = input("Enter any emotion: ")
        place = input("Enter any place: ")
        a_magic_book = f'''
                    {name1.title()} found a {color} book inside {new_old} trunk.
                    He called {name2.title()}. They wanted to check the book but 
                    {name2.title()} stopped him, because he was very {emotion}. 
                    In the night {name1.title()} thought it would be nice if
                    he went to {place.title()} and read that book. Next morning,
                    to his {emotion} he found himself in {place.title()},
                    with that {color} book.
                    '''
        print(a_magic_book)
        is_continue = input("Do you want to continue?(yes/no): ")
        if is_continue.lower() == "yes":
            continue
        else:
            break


def get_user_input():
    user_option = input("Select a game to play: ")
    return user_option


while True:
    msgs_to_user()

    user_option = get_user_input()

    if user_option.lower() == 'q':
        break

    else:
        if user_option.isdigit():
            user_option = int(user_option)
            if user_option == 1:
                play_copycat_game()

            if user_option == 2:
                play_madlib_game()

            else:
                print("Select option 1 or 2.")
                continue

        else:
            print(
                f"Required a positive integer only. But received {user_option}.")
