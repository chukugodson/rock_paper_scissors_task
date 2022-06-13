import random

print("Welcome!!! Have fun while playing")
print(" R stands for Rock \n P stands for Paper \n S stands for Scissors ")
player_name = input("What's your name :")
while True:
    user_action = input("Enter a choice (R, P, S): ")
    possible_actions = ["R", "P", "S"]
    computer_action = random.choice(possible_actions)
    print(f"\n {player_name} ({user_action}) : CPU ({computer_action}).\n")
    if user_action not in possible_actions:
        print("option invalid!!! choose from the options given ")
    else:
        if user_action == computer_action:
            print(
                f"Both players selected {user_action}. It's a tie!\n Select another choice"
            )
            continue
        elif user_action == "R":
            if computer_action == "S":
                print("Rock smashes scissors! You win!")
            else:
                print("Paper covers rock! You lose.")

        elif user_action == "P":
            if computer_action == "R":
                print("Paper covers rock! You win!")
            else:
                print("Scissors cuts paper! You lose.")

        elif user_action == "S":
            if computer_action == "P":
                print("Scissors cuts paper! You win!")
            else:
                print("Rock smashes scissors! You lose.")
        break