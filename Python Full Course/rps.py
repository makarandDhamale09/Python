import random
import sys

print("Welcome to Rock, Paper, Scissors! 🎮")
while True:
    print("---------------------------------")
    player_choice = input("\nPlease enter.... 1 for rock 🪨\t 2 for paper 📄\t 3 for scissors ✂️\t 0 to exit ❌\n").lower()
    choices = {1: "🪨", 2: "📄", 3: "✂️"}

    player = int(player_choice)

    if player < 0 or player > 3:
        sys.exit("Invalid choice ❌. Please enter a number between 1 and 3.")
    elif player == 0:
        sys.exit("Thanks for playing! 👋")


    print(f"\nYou chose: {choices[player]}")

    computer = random.choice("123")
    print(f"Computer chose: {choices[int(computer)]}")

    computer = int(computer)
    if player == computer:
        print("It's a tie! 🤝")
    elif (player == 1 and computer == 3) or (player == 2 and computer == 1) or (player == 3 and computer == 2):
        print("You win! 🎉")
    else:
        print("You lose! 😢")