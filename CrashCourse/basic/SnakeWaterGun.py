import random

'''
The win matrix will look like below for the player vs Computer

Comp    =       S   W   G
player  =   S   0   1  -1   
            W  -1   0   1   
            G   1  -1   0
'''
win_matrix = [[0, 1, - 1], [-1, 0, 1], [1, -1, 0]]
computer_score = 0
user_score = 0
user_selection = 0
game_counts = 10


def get_win_result(user, comp) -> str:
    """returns the result based on user and computer selection and also updates the score"""

    global user_score
    global computer_score

    match win_matrix[user - 1][comp - 1]:
        case 0:
            return "DRAW"
        case 1:
            user_score += 1
            return "WIN"
        case -1:
            computer_score += 1
            return "LOSS"


while user_selection != 4 and game_counts > 0:
    game_counts -= 1
    print(f"\nGame No : {10 - game_counts}")
    user_selection = int(input("Choose your option. \nSnake = 1, Water = 2, Gun = 3, Quit = 4 \n"))

    if user_selection != 4:
        computer_selection = random.randint(1, 3)
        print(f"computer selection : {computer_selection}")

        result = get_win_result(user_selection, computer_selection)

        print(f"Result  : {result}")
        print(f"Scores are player : {user_score}, computer : {computer_score}")
        print("------------------------------------------")

print("Quiting Game")
