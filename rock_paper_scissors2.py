'''Python Tutorial: Rock, Paper Scissors Game
Can be used for Water, Snake, Gun game also
# rock/paper/scissors/lizard/Spock...@Darrell Gregg: facebook
'''

import random
choices = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]
wins = {
    "Rock": "ScissorsLizard",
    "Paper": "RockSpock",
    "Scissors": "PaperLizard",
    "Lizard": "PaperSpock",
    "Spock": "ScissorsRock"
}
score = {"robo": 0, "human": 0}


def quitter():
    print("\nQuitters never win!")
    print("Score" + ("-" * 5))
    print(f"🧍: {score['human']}, 🤖: {score['robo']}")
    exit()


print("Let's play Rock Paper Scissors Lizard Spock!")
while True:
    inp = input("Press 'R' for rules, 'P' to play, 'Q' to quit\n").lower()
    if inp == "r":
        print("\nRules:\n"
              "rock crushes scissors\n"
              "rock crushes lizard\n"
              "paper covers rock\n"
              "paper disproves Spock\n"
              "scissors cuts paper\n"
              "scissors decapitates lizard\n"
              "lizard poisons Spock\n"
              "lizard eats paper\n"
              "Spock smashes scissors\n"
              "Spock vaporizes rock\n")
        continue
    elif inp == "q":
        quitter()
    elif inp == "p":
        break

"""
Begin gameplay code
"""
human = ""
while True:
    inp = input("r, p, s, l, sp... Your guess, or quit: ").lower()
    if inp == "q":
        quitter()
    if inp not in ["r", "p", "s", "l", "sp"]:
        print("Invalid guess! Try again!")
        continue
    if inp == "sp":
        human = "Spock"
    else:
        for i in choices:
            if inp == i[0].lower():
                human = i
                robo = random.choice(choices)
                print(f"🧍: {human} vs. 🤖: {robo}")
            if human == robo:
                print("Tie, no points!")
            if robo in wins[human]:
                print("You win a point!")
                score["human"] += 1
            elif human in wins[robo]:
                print("The robot wins a point!")
                score["robo"] += 1
                print(f"🧍: {score['human']}, 🤖: {score['robo']}")
                print()
